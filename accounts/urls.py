from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (login, logout )

urlpatterns = [
    path('login', login, name='login'),  
    path('register', register, name='register'),
    path('logout', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    path('profile/<int:pk>', login_required(
         ProfileUpdateView.as_view()), name='profile')
    
]
