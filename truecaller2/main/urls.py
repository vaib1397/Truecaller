from django.urls import path

from main.views import LoginView, LogoutView, NameListView, ProfileListView, RegisterView, UserlistView

urlpatterns = [
    path('login', LoginView.as_view()),
    path('logout', LogoutView.as_view()),
    path('register', RegisterView.as_view()),
    path('user', UserlistView.as_view()),
    path('name', NameListView.as_view()),
    path('profile', ProfileListView.as_view()),
    path('spam', ProfileListView.as_view()),

]