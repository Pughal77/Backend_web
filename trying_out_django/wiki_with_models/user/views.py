from django.http import  HttpResponseRedirect
from django.shortcuts import render
from .forms import login_request, create_user
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from .forms import create_user

# Create your views here.
def welcome(request):
    return render(request, "pages/welcome.html")

def login_user(request):
    invalid_user = False
    if request.method == "POST":
        login_info = login_request(request.POST)
        if login_info.is_valid():
            username1 = login_info.cleaned_data["username"]
            password1 = login_info.cleaned_data["password"]
            user = authenticate(request, username=username1, password=password1)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse("wikii:home"))
            else:
                invalid_user = True
                return render(request, "pages/login.html",{
                    "login_form": login_info,
                    "invalid_user": invalid_user
                })
    return render(request, "pages/login.html",{
        "login_form": login_request(),
        "invalid_user": invalid_user
    })
def create_use(request):
    if request.method == "POST":
        user_credentials = create_user(request.POST)
        if user_credentials.is_valid():
            user_credentials.save()
            return HttpResponseRedirect(reverse("user:login"))
        else:
            return render(request, "pages/create_user.html",{
                "create_user": user_credentials,
            })
    return render(request, "pages/create_user.html",{
                "create_user": create_user(),
            })

def logout_user():
    pass

