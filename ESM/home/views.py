from django.shortcuts import render, redirect
from .models import TUser, TInput
from django.contrib import messages
from django.core.files.storage import FileSystemStorage

def register(request):
    if request.method == 'POST':
        user = TUser()
        user.us_username = request.POST.get('id')
        user.us_pw = request.POST.get('pwd')
        user.us_api = request.POST.get('api')
    
       
        
        user.save()
        return redirect('/')
    
    return render(request, 'register.html')

# Create your views here.
def home(request):
    if request.method == 'POST' and request.FILES.get('file'):
        file = request.FILES.get('file')
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
        return render(request, 'summary.html', {'file_url': file_url})
    
    return render(request, 'home.html')


def summary(request):
    
       return render(request, 'summary.html')


def login(request):
    if request.method == 'POST':
        username = request.POST.get('id')
        password = request.POST.get('pwd')
        
        try:
            user = TUser.objects.filter(us_username=username, us_pw=password)
            if len(user) > 0:
            # 로그인 성공 시 다른 페이지로 이동
                return redirect('/')
            
        except TUser.DoesNotExist:
            # 로그인 실패 시 에러 메시지와 함께 로그인 페이지 보여줌
            messages.error(request, '아이디 또는 비밀번호가 올바르지 않습니다.')
            return render(request, 'login.html')
        
    else:
        return render(request, 'login.html')

def community(request):
    return render(request, 'community.html')


def myhome(request):
     if request.method == 'POST':
        return redirect('/myhome')
     else:
         return render(request, 'myhome.html')

