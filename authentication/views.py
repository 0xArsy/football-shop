from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

def register(request):
    form = UserCreationForm()
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Akun berhasil dibuat! Silakan login.")
            return redirect("authentication:login")
    return render(request, "register.html", {"form": form})

def login_user(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)

            response = HttpResponseRedirect(reverse("main:show_main"))
            response.set_cookie('last_login', str(user.last_login))
            return response
    else:
        form = AuthenticationForm()
    return render(request, "login.html", {"form": form})

def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse("authentication:login"))
    response.delete_cookie('last_login')
    return response
