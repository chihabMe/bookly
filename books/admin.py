from django.contrib import admin
from .models import Book,BookImage
# Register your models here.
@admin.register(Book)
class BookAdminManager(admin.ModelAdmin):
    def cover(self,book,*args, **kwargs):
        return book.images.all().first().alt
    list_display = ['title','cover','owner','price_in_dz','price_as_str']
    fields = ['title','slug','owner','description','price_in_dz','price_as_str']

@admin.register(BookImage)
class BookAdminManager(admin.ModelAdmin):
    fields = ['book','alt','image']

