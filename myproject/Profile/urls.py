from django.urls import path
from .views import *

urlpatterns = [
    path('', profile, name='profile'),
    path('user_logout/', user_logout, name='user_logout'),
    path('register/', user_register,name='register'),
    path('login/', user_login, name= 'login'),
]