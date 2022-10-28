from django.urls import path 
from .views import book_add_view, book_detail_view,books_list_view
app_name = 'books'

urlpatterns = [
    path('',books_list_view,name='books_list'),
    path('<slug:slug>/',book_detail_view,name='book_detail'),
    path('add/',book_add_view,name='book_add'),
]