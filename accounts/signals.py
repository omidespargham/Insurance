from django.dispatch import receiver
from .models import Profile, User
from django.db.models.signals import post_save


# signal for create profile Model for User Model 

def create_profile(sender,**kwargs):
    if kwargs["created"]:
        Profile.objects.create(user=kwargs["instance"])

post_save.connect(receiver=create_profile,sender=User)

