from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import RegisterForm
from django.urls import reverse
from .models import User
# Create your views here.

def index(request):
    if request.user.is_authenticated:
        user = request.user
        return render(request, "main/index.html", {"user":user})
    else:
        return redirect("accounts/login")

def register(request):
    form =RegisterForm(request.POST)
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect(reverse('index'))
    else:
        form = RegisterForm()

    return render(request, "registration/register.html", {"form":form})

def leaderboards(request):
    all_players = User.objects.order_by('-score')
    user = request.user
    context = {'players': all_players, 'user': user}
    return render(request, 'main/leaderboards.html', context)