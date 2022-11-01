from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.urls import reverse

# Create your models here.
User = get_user_model()

def upload_to(instance,filename):
    return "profile/"+instance.user.username+"/"+filename

class Profile(models.Model):
    user = models.OneToOneField(User,unique=True,on_delete=models.CASCADE,related_name='profile')
    image = models.ImageField(upload_to=upload_to,blank=True,null=True)
    date_of_birth = models.DateTimeField(blank=True,null=True)
    following = models.ManyToManyField('self',through='accounts.Contact',related_name='followers',symmetrical=False)

    def __str__(self) -> str:
        return self.user.username 
    def get_absolute_url(self):
        return reverse("accounts:profile",args=[self.user.username])
    
    def get_image_absolute_url(self):
        if self.image:
            return self.image.url
        return None


class Contact(models.Model):
    user_from= models.ForeignKey(Profile,related_name='rel_from_set',on_delete=models.CASCADE)
    user_to  = models.ForeignKey(Profile , related_name='rel_to_set',on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user_from.user.username+" follows " +self.user_to.user.username

    class Meta:
        ordering  = ('-created',)

@receiver(post_save,sender=User)
def create_profile(instance,created,*args, **kwargs):
    if created:
        profile = Profile(user=instance)
        profile.save()
