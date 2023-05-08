from django.shortcuts import render, redirect
from .models import TUser, TInput
from django.contrib import messages
from django.http import HttpResponse
from django.template import loader
from django.core.files.storage import FileSystemStorage
from home.fileConverter import convert
from home.contentsMaker import contentsMaker



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
        fs = FileSystemStorage(location='./home/inputfile')#homelocation추가
        
        filename = fs.save(file.name, file)
        file_url = fs.url(filename)
        filename , file_url= convert()
        
        contentsmaker = contentsMaker
        index = f"[서론]\n\n[Chapter.1] 딥러닝 기반 R-CNN 알아보기\n- 딥러닝이란?\n- R-CNN의 개념과 특징\n- 바이너리 악성코드 분류하기\n\n[Chapter.2] 딥러닝으로 악성코드 이미지화하기\n- 악성코드 이미지화란?\n- CNN을 이용한 악성코드 이미지화 과정\n- 이미지 데이터 전처리\n\n[Chapter.3] 악성코드 특징 추출하기\n- R-CNN을 이용한 악성코드 특징 추출이란?\n- CNN과 R-CNN의 차이점\n- 악성코드 패밀리 분류\n\n[Chapter.4] 실험 결과와 분석\n- 제안 기법의 검출율과 정확도 평가\n- CNN 처리속도와 R-CNN 처리 속도 비교\n\n[결론]"
        #contentsMaker.index()
        
        contents = ['[서론]\n최근 악성코드의 발생빈도가 증가하면서 이를 대처하기 위한 다양한 방법들이 연구되고 있다. 그 중에서도 딥러닝은 뛰어난 성능으로 주목받고 있다. 이번 글에서는 딥러닝을 이용한 악성코드 대응 기술 중 하나인 R-CNN을 중심으로 알아보고자 한다.', '[Chapter.1] 딥러닝 기반 R-CNN 알아보기\n딥러닝이란, 이미지 처리에 있어 뛰어난 성능을 보이는 인공지능 기술이다. 이를 바탕으로 R-CNN(Rich feature Hierarchical Convolutional Neural Network)은 이미지 내부의 다양한 객체들을 인식하고 분류하는 데 있어서 상당한 향상을 보였다. R-CNN은 입력 이미지에 대해 먼저 선택적인 객체 검출 후 개별 객체를 인식하고 분류한다. 이러한 특징으로 인해 R-CNN은 객체 검출과 이미지 분류 분야에서 뛰어난 성능을 발휘하였고, 특히 바이너리 악성코드 분류와 같은 분야에서도 큰 역할을 하고 있다.', '[Chapter.2] 딥러닝으로 악성코드 이미지화하기\n악성코드 이미지화는 악성코드의 트레이스백 및 분류, 이상 탐지 등에서 활용되며, 악성코드에 대한 정보를 더욱 직관적으로 파악할 수 있게 해준다. 이를 위해 CNN(Convolutional Neural Network)을 이용하여 악성코드의 이미지화를 진행하였다. 악성코 드 이미지화 과정에서는 이미지 데이터 전처리 작업이 여러 번 반복되며, CPU 및 GPU 자원 활용량이 매우 높아진다.', '[Chapter.3] 악성코드 특징 추출하기\nR-CNN을 이용하여 악성코드의 특징 추출을 진행하는 방식은 이전과는 다른 접근 방식을 활용한다. CNN에서 이미지 데이 터를 직접 학습하는 방식과는 달리, R-CNN에서는 추출된 객체 이미지 데이터를 기반으로 해당 객체의 특징을 추출한다. CNN과 R-CNN의 차이점을 이해하는 것은 모델링 수행 시 분명한 차이를 가져올 수 있다. 이는 악성코드 패밀리를 분류할 수 있는 능력과 높은 정확도를 갖게 된다.', '[Chapter.4] 실험 결과와 분석\n제안 기법의 검출율과 정확도를 평가함으로써 딥러닝 기반 R-CNN에서의 성능을 측정하고, 그 결과를 분석하였다. 이때 CNN 처리속도와 R-CNN 처리 속도의 비교도 진행하였다. 실험 결과, R-CNN은 기존 다른 기술들과 비교하여 높은 검출율과 매우 높은 정확도를 보여주며, CNN에 비해 실행 시간이 길다는 한계가 있었다.', '[결론]\n악성코드의 증가로 인해, 대응 기술 발전도 더 욱 중요해졌다. 이번 글에서는 딥러닝을 이용한 악성코드 대응 기술 중 하나인 R-CNN에 대해 알아보았는데, R-CNN은 악성코드의 특징을 추 출하고 분류하는 데 있어서 매우 뛰어난 성능을 보인다는 것을 확인하였다. 따라서 앞으로도 R-CNN과 같은 딥러닝 기술을 활용하여 보다 안전한 인터넷 환경을 위한 대응 기술들이 개발될 것으로 기대해 본다.']
        #contentsmaker.contents(index)
        
        
        title =  "R-CNN과 바이러스"#contentsmaker.title
        data = {'title':title,'index':index,'contents':contents}
        
        return render(request,'summary.html',{'data':data})
    
    return render(request, 'home.html')


def summary(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        contents = request.POST.get('contents')
        
        data = data = {'title':title,'contents':contents}
        return render(request,'view.html',{'data':data})
    if request.method == 'GET':
        
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

def view(request):
    
    
    return render(request,'view.html')