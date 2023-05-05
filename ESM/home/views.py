from django.shortcuts import render, redirect
from .models import TUser


# Create your views here.
def home(request):
    
    if request.method  == 'post':
        user = TUser()
        user.us_id = request.post['id']
        user.us_pw = request.post['pwd']
        user.save()
        
        
    return redirect(request, 'home.html')


def summary(request):
    return render(request, 'summary.html')


def login(request):
    
        
        
    return render(request, 'login.html')


def community(request):
    return render(request, 'community.html')


def myhome(request):
    return render(request, 'myhome.html')

