from django.urls import path
from .views import *
urlpatterns = [
    path('<int:thread_id>/', messages_page, name='chatroom'),
    path('create_thread/<int:profile_id>', create_thread, name='create_thread'),
]