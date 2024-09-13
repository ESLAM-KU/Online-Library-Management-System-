from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add_book, name='add_book'),
    path('update/<int:pk>/', update_book, name='update_book'),
    path('delete/<int:pk>/', delete_book, name='delete_book'),
    path('', book_list, name='book_list'),
    path('borrow/<int:pk>/', borrow_book, name='borrow_book'),
    path('borrowed-books/', borrowed_books, name='borrowed_books'),
    path('return_book/<int:borrow_id>/', return_book, name='return_book'),

]


