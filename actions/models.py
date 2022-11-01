from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType
from accounts.models import Profile

# Create your models here.
class Action(models.Model):
    profile = models.ForeignKey(Profile,related_name='actions',db_index=True,on_delete=models.CASCADE)
    body  = models.CharField(max_length=300)
    created = models.DateTimeField(auto_now_add=True,db_index=True)

    target_ct = models.ForeignKey(ContentType,blank=True,null=True,on_delete=models.CASCADE,related_name='target_obj')
    target_id = models.PositiveIntegerField(null=True,blank=True,db_index=True)
    target = GenericForeignKey('target_ct','target_id')

    class Meta:
        ordering = ("-created",)
