from django.urls import path
from .views import *
urlpatterns = [
    path('<int:thread_id>/', messages_page, name='chatroom'),
]