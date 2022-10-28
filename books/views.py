from django.shortcuts import get_object_or_404, render

from .models import Book
from .forms import BookAddForm,BookImageForm

# Create your views here.

def books_list_view(request):
    books = Book.objects.all()
    context ={
        'books':books
    }
    return render(request,'books/list.html',context)
def book_detail_view(request,slug):
    book = get_object_or_404(Book,slug=slug)
    context ={
        'book':book
    }
    return render(request,'books/detail.html',context)

def book_add_view(request):
    book_add_form = BookAddForm()
    book_image_form = BookImageForm()

    if request.method=="POST":
        book_add_form = BookAddForm(data=request.POST)
        book_image_form = BookImageForm(files=request.FILES)

        if book_add_form.is_valid() and book_image_form.is_valid():
            book = book_add_form.save(commit=False)
            image = book_image_form.save(commit=False)
            book.owner = request.user.profile 
            image.book = book

            print(book)
            print(image)


            book.save()
            image.save()

    context ={
        'book_add_form':book_add_form,
        'book_image_form':book_image_form
    }
    return render(request,'books/add.html',context)


