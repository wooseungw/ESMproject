from django.shortcuts import render, redirect
from .models import TUser
from django.http import HttpResponse
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect# 홈으로 이동하기 위해 redirect 추가로 적어준다

# Create your views here.
def home(request):
    
        return render(request, 'home.html')



def summary(request):
    return render(request, 'summary.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['id']
        password = request.POST['pwd']
        # user = authenticate(request, username=TUser.us_id, password=TUser.us_pw)

        # if user is not None:
        #     login(request, user)
        return redirect('/')  # 루트 위치로 리다이렉트합니다.
        
    else:
        return render(request, 'login.html')

def community(request):
    return render(request, 'community.html')


def myhome(request):
    return render(request, 'myhome.html')

