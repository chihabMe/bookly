from re import template
from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from django.contrib.auth.decorators import login_required
from actions.utils import create_action
from django.db.models import Count

from common.decorators import hx_required
from common.http_helpers import is_hx_request

from .models import Book
from .forms import BookAddForm,BookImageForm
import redis
from django.conf import settings

r = redis.Redis(host=settings.REDIS_HOST,port=settings.REDIS_PORT,db=settings.REDIS_DB)

# Create your views here.
def books_list_view(request):
    # books = Book.objects.annotate(total_likes=Count("likes")).order_by('-total_likes')
    books = Book.objects.all().order_by("-total_likes")
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

@login_required
def book_detail_view(request,slug):
    book = get_object_or_404(Book,slug=slug)
    ##increase views
    total_views = r.incr(f"book:{book.id}:views")
    ##increase ranking
    r.zincrby("books_ranking",1,book.id)
    ##getting books by rank
    books_ranking = r.zrange("books_ranking",0,-1,desc=True)[:10]
    books_ranking_ids = [int(id) for id in books_ranking]
    most_visited = list(Book.objects.filter(id__in=books_ranking_ids))
    most_visited.sort(key=lambda x:books_ranking_ids.index(x.id))
    print(most_visited)

    context ={
        'book':book,
        'liked':request.user.profile in book.likes.all(),
        'total_views':total_views
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
