from django.db import models
from django.contrib.auth.models import User, AbstractBaseUser
from django.contrib import admin




# class User(AbstractBaseUser):
#     username = models.CharField(null=False, max_length=50)
#     email = models.EmailField(blank=True, null=True)
#     # phone = models.CharField(max_length=10, blank=True, null=True)
#     is_active= models.BooleanField(default=False)

# class User(models.Model):
#     username = models.CharField(max_length=50)
#     email = models.EmailField(unique=True)
#     phone = models.CharField(max_length=10, unique=True)

#     USERNAME_FIELD = 'username'


class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    phone = models.CharField(max_length=10, unique=True)
    is_spam = models.BooleanField(default=False)


class Name(models.Model):
    name = models.CharField(null=False, max_length=50)
    profile = models.ForeignKey(Profile, on_delete=models.SET_NULL, null=True)

	# def __str__(self):
    #     return self.name

admin.site.register(Profile)
admin.site.register(Name)
