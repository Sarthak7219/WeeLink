from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from core.views import Profile
from .models import Thread




# Create your views here.



@login_required
def messages_page(request, thread_id):

    if thread_id == 0:
        messages.error(request, "No chats found!")
        return redirect('home')

    user_profile = request.user.profile
    user_followed_profiles = user_profile.follows.exclude(pk=user_profile.pk)

    is_following = True

    thread = Thread.objects.get(id=thread_id)

    second_person = thread.second_person if thread.first_person == request.user else thread.first_person

    if second_person.profile not in user_followed_profiles:
        is_following = False


    chat_messages = thread.chatmessage_thread.all()

    context = {
        'thread_id': thread_id,
        'second_person': second_person,
        'chat_messages': chat_messages,
        'is_following':is_following
    }
    return render(request, 'chatroom.html', context)

def create_thread(request, profile_id):

    profile = Profile.objects.get(id =profile_id)
    user_profile = request.user.profile

    if profile == user_profile.id:
        return redirect('profile', id=user_profile.id)
    
    user_followed_profiles = user_profile.follows.exclude(pk=user_profile.pk)

    

    if profile in user_followed_profiles:
        thread, created = Thread.objects.get_or_create_thread(
            request.user,
            profile.user
        )
        thread_id=thread.id
    else:
        messages.error(request, "Follow Profile to send message")
        thread_id = 0

    return redirect('chatroom', thread_id = thread_id)




