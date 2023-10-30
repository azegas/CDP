from django.shortcuts import render


def HomePageView(request):
    return render(request, "welcome/home.html")


def AboutPageView(request):
    return render(request, "welcome/about.html")
