from django.dispatch import receiver
from django.db.models.signals import m2m_changed
from .models import Book

@receiver(m2m_changed,sender=Book.likes.through)
def likes_change(sender,instance,*args, **kwargs):
    instance.total_likes = instance.likes.count()
    instance.save()