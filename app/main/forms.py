from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Story

class RegisterForm(UserCreationForm):
    email = forms.EmailField(label="Email", required=True)
    username = forms.CharField(label="Username", required=True)
    first_name = forms.CharField(label="First Name", required=False)
    last_name = forms.CharField(label="Last Name", required=False)


    class Meta:
        model = User
        fields = ["email", "username", "first_name", "last_name", "password1", "password2"]


class SingleplayerForm(forms.Form):
    story_choice = forms.ModelChoiceField(queryset=Story.objects.values_list('title', flat=True).order_by('title'), label = "Story Choice")