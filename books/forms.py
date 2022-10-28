
from django import forms 
from .models import Book,BookImage

class BookAddForm(forms.ModelForm):
    class Meta:
        model  = Book
        fields = ['title','description','price_in_dz','price_as_str']
    
    def save(self,commit=True)->Book:
        book = super().save(commit=False)
        if commit:
            book.save()
        return book

class BookImageForm(forms.ModelForm):
    class Meta:
        model  = BookImage
        fields = ['image']
    
    def save(self,commit=True) -> BookImage:
        book_image = super().save(commit)
        if commit:
            book_image.save()
        return book_image
