from django.db import models
from django.contrib.auth import get_user_model
from django.db.models import Q



# Create your models here.

class ThreadManager(models.Manager):
    def by_user(self, **kwargs):
        user = kwargs.get('user')
        lookup = Q(first_person=user) | Q(second_person=user)
        qs = self.get_queryset().filter(lookup).distinct()
        return qs
    
    def get_or_create_thread(self, user1, user2):
        thread = self.filter(
            Q(first_person=user1, second_person=user2) |
            Q(first_person=user2, second_person=user1)
        ).first()
        
        if thread:
            return thread, False
        else:
            thread = self.create(first_person=user1, second_person=user2)
            return thread, True


class Thread(models.Model):
    first_person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True, related_name='thread_first_person')
    second_person = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, null=True, blank=True,
                                     related_name='thread_second_person')
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    objects = ThreadManager()
    class Meta:
        unique_together = ['first_person', 'second_person']


    

    def __str__(self):
        return f'[{self.first_person} , {self.second_person}]'


class ChatMessage(models.Model):
    thread = models.ForeignKey(Thread, null=True, blank=True, on_delete=models.CASCADE, related_name='chatmessage_thread')
    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    message = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)


