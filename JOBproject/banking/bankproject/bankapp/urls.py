
from django.urls import path

from bankapp import views

urlpatterns = [

    path('', views.demo, name='demo'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('account/', views.account, name='account'),
]