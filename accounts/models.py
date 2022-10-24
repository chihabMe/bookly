from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
User = get_user_model()

def upload_to(instance,filename):
    return "profile/"+instance.user.username+"/"+filename

class Profile(models.Model):
    user = models.OneToOneField(User,unique=True,on_delete=models.CASCADE)
    image = models.ImageField(upload_to=upload_to,blank=True,null=True)
    date_of_birth = models.DateTimeField(blank=True,null=True)

    def __str__(self) -> str:
        return self.user.username 

@receiver(post_save,sender=User)
def create_profile(instance,created,*args, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
