from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('summary/', views.summary, name='summary'),
    path('login/', views.login, name='login'),
    path('community/', views.community, name='community'),
    path('myhome/', views.myhome, name='myhome'),
]
