from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
]