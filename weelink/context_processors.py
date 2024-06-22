from chat.models import Thread


def base_template_data(request):

    if request.user.is_authenticated:

        threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
        
        for thread in threads:
            latest_message = thread.chatmessage_thread.order_by('-timestamp').first()
            if latest_message:
                thread.latest_message = latest_message.message[:15] + '...' if len(latest_message.message) > 15 else latest_message.message
                latest_message_thread_id = latest_message.thread.id
            else:
                thread.latest_message = None
                latest_message_thread_id = 0



        
        
        context = {
            'Threads': threads,
            'latest_message_thread_id':latest_message_thread_id
        }
        return context
    
    else:
        return {}
    
   
        