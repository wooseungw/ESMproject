from django.shortcuts import render

# Create your views here.
def home(requeset):
    return render(requeset, 'home.html')


def summary(requeset):
    return render(requeset, 'summary.html')


def login(requeset):
    return render(requeset, 'login.html')


def community(requeset):
    return render(requeset, 'community.html')