from django.urls import path
from .import views

urlpatterns =[
    path('mainpage/', views.mainpage, name='mainpage'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    
]