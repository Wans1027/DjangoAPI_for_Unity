from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, primary_key=True)
    nickname = models.CharField(max_length=128, default='')
    position = models.CharField(max_length=128,null=True,default='')
    # subjects = models.CharField(max_length=128,null=True,default='')
    score = models.IntegerField(default = 0)
    image = models.ImageField(upload_to='profile/', default='default.jpg')
    #complete = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
