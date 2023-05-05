from django.shortcuts import render, redirect
from .models import TUser


# Create your views here.
def home(request):
     if request.method == 'POST':
        return redirect('/summary')
     else:
         return render(request, 'home.html')


def summary(request):
    
       return render(request, 'summary.html')


def login(request):
     if request.method == 'POST':
        user = TUser()
        user.us_id = request.POST['id']
        user.us_pw = request.POST['pwd']
        user.save()
        return redirect('/')
     else:
        return render(request, 'login.html')


def community(request):
    return render(request, 'community.html')


def myhome(request):
     if request.method == 'POST':
        return redirect('/myhome')
     else:
         return render(request, 'myhome.html')

