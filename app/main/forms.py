from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)
    username = forms.CharField(label="Username", required=True)
    first_name = forms.CharField(label="First Name", required=False)
    last_name = forms.CharField(label="Last Name", required=False)


    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name", "password1", "password2"]