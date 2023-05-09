from django.urls import path
from . import views

urlpatterns = [
    
    path('summary/', views.summary, name='summary'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('myhome/', views.myhome, name='myhome'),
    path('view/',views.view, name='view'),
    path('', views.home, name='home'),
]
