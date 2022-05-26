import imp
from django.shortcuts import render
from main.models import Profile, User, Name
from main.seralizers import (
    LoginSerializer,
    ProfileSerializer,
    UserSerializer,
    NameSerializer,
)
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from django.contrib.auth import login as django_login, logout as django_logout
from rest_framework.views import APIView
from rest_framework.authentication import TokenAuthentication, SessionAuthentication
from rest_framework import mixins, generics
from django.shortcuts import get_object_or_404, render
from rest_framework.permissions import IsAuthenticated


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        django_login(request, user)
        token, created = Token.objects.get_or_create(user=user)
        return Response({"token": token.key}, status=200)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)

    def post(self, request):
        django_logout(request)
        return Response({"Message": "successfully logout"}, status=204)


class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        return Response(serializer.errors, status=400)


class UserlistView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = UserSerializer
    permission_class = [IsAuthenticated]
    queryset = User.objects.all()

    def get(self, request, *args, **kwargs):
        params = request.query_params
        print(params)
        if not "pk" in kwargs:
            return self.list(request)
        post = get_object_or_404(User, pk=kwargs["pk"])
        return Response(UserSerializer(post).data, status=200)

    def post(self, request):
        data = request.data
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            post = serializer.save()
            return Response(UserSerializer(post).data, status=201)
        return Response(serializer.errors, status=400)


class ProfileListView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = ProfileSerializer
    permission_class = (IsAuthenticated,)
    authentication_classes = [TokenAuthentication, SessionAuthentication]
    queryset = Profile.objects.all()

    def get(self, request, *args, **kwargs):
        params = request.query_params
        print(params)
        if not "pk" in kwargs:
            return self.list(request)
        post = get_object_or_404(Profile, pk=kwargs["pk"])
        return Response(ProfileSerializer(post).data, status=200)

    def post(self, request):
        data = request.data
        serializer = ProfileSerializer(data=data)
        if serializer.is_valid():
            post = serializer.save()
            return Response(ProfileSerializer(post).data, status=201)
        return Response(serializer.errors, status=400)


class NameListView(generics.GenericAPIView, mixins.ListModelMixin):
    serializer_class = NameSerializer
    permission_class = [IsAuthenticated]
    queryset = Name.objects.all()

    def get(self, request, *args, **kwargs):
        params = request.query_params
        print(params)
        if not "pk" in kwargs:
            return self.list(request)
        post = get_object_or_404(Name, pk=kwargs["pk"])
        return Response(NameSerializer(post).data, status=200)

    def post(self, request):
        data = request.data
        serializer = NameSerializer(data=data)
        if serializer.is_valid():
            post = serializer.save()
            return Response(NameSerializer(post).data, status=201)
        return Response(serializer.errors, status=400)


class Spam_Marked_ApiView(APIView):
    # def post(self, request):
    #     data = request.data
    #     ser = ProfileSerializer(data=data)
    #     ser.is_valid(raise_exception=True)
    #     ser.save()
    #     return Response("Changed room successfully", status=201)

        def patch(self, request, pk=None):
            phone = request.data['phone']
            instance = Profile.objects.filter(phone=phone)
            # instance = self.get_object(id)
            ser = ProfileSerializer(instance, data=phone, partial=True)
            if ser.is_valid():
                ser.save()
                return Response(ser.data, status=200)
            return Response(ser.errors, status=400)