from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

from .models import Thread

from django.db.models import Q


# Create your views here.



@login_required
def messages_page(request, thread_id):

    if thread_id == 0:
        messages.error(request, "No chats found!")
        return redirect('home')

    thread = Thread.objects.get(id=thread_id)
    second_person = thread.second_person if thread.first_person == request.user else thread.first_person
    chat_messages = thread.chatmessage_thread.all()

    context = {
        'thread_id': thread_id,
        'second_person': second_person,
        'chat_messages': chat_messages,
    }
    return render(request, 'chatroom.html', context)




