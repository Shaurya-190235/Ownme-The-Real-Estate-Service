from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (login, logout, dashboard )

urlpatterns = [
    path('login', login, name='login'),  
    path('logout', logout, name='logout'),
    path('dashboard', dashboard, name='dashboard'),
    path('register', register, name='register'),
    
]
