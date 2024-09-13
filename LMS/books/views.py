from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test
from .forms import *
from .models import *
from django.contrib.auth.decorators import login_required
from datetime import date ,timedelta
from django.utils import timezone
#-----------------------------------------------------
def is_mod_or_staff(user):
    return user.is_mod or user.is_staff
#-----------------------------------------------------
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})
#-----------------------------------------------------
@user_passes_test(is_mod_or_staff)
def add_book(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
    return render(request, 'books/add_book.html', {'form': form})
#-----------------------------------------------------
@user_passes_test(is_mod_or_staff)
def update_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm(instance=book)
    return render(request, 'books/update_book.html', {'form': form, 'book': book})
#-----------------------------------------------------
@user_passes_test(is_mod_or_staff)
def delete_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == 'POST':
        book.delete()
        return redirect('book_list')
    return render(request, 'books/delete_book.html', {'book': book})
#-----------------------------------------------------
def borrow_book(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if not book.is_borrowed:
        student_email = request.user.email
        Borrow.objects.create(
            book=book,
            student_email=student_email,
            return_date=timezone.now() + timedelta(days=14))
        book.is_borrowed = True
        book.save()
    return redirect('book_list')
#-----------------------------------------------------
def borrowed_books(request):
    student_email = request.user.email
    borrowed_books = Borrow.objects.filter(student_email=student_email)
    return render(request, 'books/borrowed_books.html', {'borrowed_books': borrowed_books})
#-----------------------------------------------------
@login_required
def return_book(request, borrow_id):
    borrow_record = get_object_or_404(Borrow, id=borrow_id, student_email=request.user.email)
    book = borrow_record.book
    book.is_borrowed = False
    book.save()
    borrow_record.delete()
    return redirect('borrowed_books')
#-----------------------------------------------------
