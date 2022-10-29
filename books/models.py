from email.policy import default
from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.signals import pre_save
from django.dispatch import receiver
from random import randint
from django.urls import reverse
from django.utils.text import slugify
from PIL import Image
from accounts.models import Profile
# from cloudinary.models import CloudinaryField


# Create your models here.

class Book(models.Model):
    title = models.CharField(max_length = 150)
    slug = models.SlugField(blank=True)
    description = models.TextField()
    price_in_dz = models.PositiveIntegerField(default=0)
    price_as_str = models.CharField(max_length=150)
    owner  = models.ForeignKey(Profile,related_name='books',on_delete=models.CASCADE)
    likes = models.ManyToManyField(Profile,related_name='liked_books')
    

    def get_absolute_url(self):
        return reverse("books:book_detail",kwargs={"slug": self.slug})


    def __str__(self)->str:
        return self.title

def upload_image_to(instance,filename)->str:
    return instance.book.owner.user.username+"/books/images/"+filename

class BookImage(models.Model):
    book = models.ForeignKey(Book,related_name="images",on_delete=models.CASCADE)
    alt = models.CharField(max_length=200,blank=True)
    image = models.ImageField(upload_to=upload_image_to)
    # image = CloudinaryField("image")
    created = models.DateTimeField(auto_now_add=True)

    def save(self,*args, **kwargs):
        if not self.alt:
            self.alt = slugify(self.image.name.split(".")[0])
        super().save(*args, **kwargs)

        # if self.image:
        #     img = Image.open(self.image.path)
        #     if img.width >550 or img.height>550:
        #         size=(550,550)
        #         img.thumbnail(size)
        #         img.save(self.image.path)

    def __str__(self):
        return self.alt



@receiver(pre_save,sender=Book)
def generate_slug(instance,*args, **kwargs):
    if not instance.slug:
        extra = str(randint(100,800))
    else:
        extra = instance.slug.split("-")[0]
    instance.slug = slugify(extra+"-"+instance.owner.user.username+'-'+instance.title)
    return instance



