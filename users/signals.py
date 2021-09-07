from django.db.models.signals import post_save # when a user is created, it uses this signal
from django.contrib.auth.models import User
from django.dispatch import receiver # this gets the signal and performs a task --> 
from .models import Profile


@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_profile(sender, instance, **kwargs):
    instance.profile.save()