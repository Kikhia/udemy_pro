from django.contrib import admin
from django.urls import path
from befo_app import views

app_name = 'befo_app'

urlpatterns = [
    #path('users/',views.users,name='users'),
    path('register/',views.register,name='register'),
    path('login/',views.user_login,name='user_login'),
]
