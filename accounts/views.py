from django.shortcuts import render


def index(request):
    return render(request, "accounts/index.html")


def login_view(request):
    return render(request, "accounts/login.html")