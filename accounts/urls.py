from django.urls import path
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView
from .views import RegisterView, CustomLoginView, home_view, gestionar_usuarios

urlpatterns = [
    path('', lambda request: redirect('register/')), 
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('home/', home_view, name='home'),
    path('gestionar-usuarios/', gestionar_usuarios, name='gestionar_usuarios'),
]
