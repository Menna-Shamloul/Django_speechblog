from django import forms
from django.contrib.auth.models import User
from django.contrib.author.forms import UserCreationForm

class UserRegisterForm(UserCreationForm):
    email