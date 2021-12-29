from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import User, Story
from django.forms import ModelForm

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

class SingleplayerStoryForm(forms.Form):
          

    def __init__(self, story_choice):
        super(SingleplayerStoryForm, self).__init__()
        self.story_choice = story_choice
        story = Story.objects.get(title=self.story_choice)
        for question in story.questions:
            self.fields[question] = forms.CharField(required=True)
        
