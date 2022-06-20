from django.urls import path
from django.contrib.auth.decorators import login_required

from .views import (login, logout )

urlpatterns = [
    path('login', login, name='login'),  
    path('logout', logout, name='logout'),
    
]
