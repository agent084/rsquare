from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.db.models import Q
from django.shortcuts import render, redirect

from login.forms import SignupForm, SigninForm
# Create your views here.


def index(request):
    return render(request, "login/index.html", context=None)


def signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            messages.success(request, "User saved")
            return redirect("login:signin")
        else:
            messages.error(request, "Error in form")
    else:
        form = SignupForm()
    context = {"form": form}
    return render(request, "login/signup.html", context)


def signin(request):
    if request.method == "POST":
        form = SigninForm(request.POST)
        # username = req.POST["username"]
        # password = req.POST["password"]
        username = form["username"].value()
        password = form["password"].value()
        user = authenticate(request, username=username,  password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in")
            return redirect("login:index")
        else:
            messages.error(request, "Invalid Username or Password")
    else:
        form = SigninForm()
    context = {"form": form}
    return render(request, "login/signin.html", context)


def signout(request):
    logout(request)
    return redirect("login:signin")
