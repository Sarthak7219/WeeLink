from chat.models import Thread
from django.db.models import Q

def base_template_data(request):

    if request.user.is_authenticated:

        threads = Thread.objects.by_user(user=request.user).prefetch_related('chatmessage_thread').order_by('timestamp')
        

        if not threads.exists():
            context = {
                'threads': [],
                'latest_thread_id': 0
            }
            return context


        for thread in threads:
            latest_message = thread.chatmessage_thread.order_by('-timestamp').first()
            if latest_message:
                thread.latest_message = latest_message.message[:15] + '...' if len(latest_message.message) > 15 else latest_message.message
                
            else:
                thread.latest_message = None
                

        current_user = request.user
    
        
        latest_thread = Thread.objects.filter(
            Q(first_person=current_user) | Q(second_person=current_user)
        ).latest('timestamp')

        if latest_thread:
            latest_thread_id = latest_thread.id
        else:
            latest_thread_id=0

        
        
        context = {
            'Threads': threads,
            'latest_thread_id':latest_thread_id
        }
        return context
    
    else:
        return {}
    
   
        