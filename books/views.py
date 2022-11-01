from re import template
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required
from actions.utils import create_action

from common.decorators import hx_required
from common.http_helpers import is_hx_request


from .models import Book
from .forms import BookAddForm,BookImageForm

# Create your views here.
def books_list_view(request):
    books = Book.objects.all()
    template_name = 'books/list.html'
    paginator = Paginator(books,3)
    page = request.GET.get('page')
    try :
        books = paginator.page(page)
    except PageNotAnInteger:
        books = paginator.page(1)

    except EmptyPage:
        if is_hx_request(request):
            return HttpResponse("")
        books = paginator.page(paginator.num_pages)
    if is_hx_request(request):
        template_name = 'books/partials/books_list.html'

    context ={
        'books':books
    }
    return render(request,template_name,context)
def book_detail_view(request,slug):
    book = get_object_or_404(Book,slug=slug)
    context ={
        'book':book,
        'liked':request.user.profile in book.likes.all()
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


@hx_required
def book_like(request,slug):
    book = get_object_or_404(Book,slug=slug)
    profile = request.user.profile
    template = 'books/partials/like.html'
    if profile in book.likes.all():
        create_action(profile,f"you disliked this book '{book.title}' ",book)
        book.likes.remove(profile)
    else:
        book.likes.add(profile)
        create_action(profile,f"you liked this book '{book.title}' ",book)
        template = 'books/partials/dislike.html'
    return render(request,template)
