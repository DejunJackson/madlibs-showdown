from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.urls import reverse
# Create your views here.

def index(request):
    return HttpResponse('<h1>Hello World!</h1>')

def register(request):
    form =RegisterForm(request.POST)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(reverse('index'))
    else:
        form = RegisterForm()

    return render(request, "main/register.html", {"form":form})