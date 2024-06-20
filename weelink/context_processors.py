from chat.models import Thread  

def base_template_data(request):
    threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
    
    for thread in threads:
        latest_message = thread.chatmessage_thread.order_by('-timestamp').first()
        if latest_message:
            thread.latest_message = latest_message.message[:15] + '...' if len(latest_message.message) > 15 else latest_message.message
        else:
            thread.latest_message = None
    
    return {
        'Threads': threads,
    }