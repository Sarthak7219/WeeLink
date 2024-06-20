from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

#Receiver function

@receiver(post_save, sender=User)   #--> if any object of class User is saved, then the post_save signal will be sent to the receiver function with sender, instance, created and for handling more arguments(if any) we are using kwargs. 
# 'instance': the actual object(instance being saved, in this cas a user object), 
# 'created': A boolean; True if a new record was created, False if an existing record was updated.
def create_profile(sender, instance, created, **kwargs):
    if created:
        user_profile = Profile(user = instance)    #--> create a profile instance with the created user
        user_profile.save()                        #--> save the profile instance to database
        user_profile.follows.add(instance.profile) #--> add the profile saved to the follows field of the user profile so that he follows himself automatically in start.
        user_profile.save()                        # save



# Profile model
class Profile(models.Model):
    user = models.OneToOneField(User, models.CASCADE)   #no need to write related name for one to one field, django by defauls creates a relation using the lowercase letter of the class(Profile) so we can use the user.profile
    age = models.IntegerField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="images/profile/")
    # bio = models.TextField(null=True, blank=True, max_length=150)
    follows = models.ManyToManyField(
        "self",
        related_name="followed_by",
        symmetrical=False,
        blank=True
    )

    def __str__(self):
        return self.user.username




class Post(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='post')
    body = models.CharField(null=True, blank=True, max_length=140)
    created_at = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User, null=True,blank=True, related_name='likes')

    def __str__(self):
        body_preview = self.body[:30] + "..." if self.body else "" 
        return (
            f"{self.user} "
            f"({self.created_at:%Y-%m-%d %H:%M}): "
            f"{body_preview}"
        )



class Image(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='images', null=True, blank=True)
    image = models.ImageField(upload_to='images/post/', null=True, blank=True)


    