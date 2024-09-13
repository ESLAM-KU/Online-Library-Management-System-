from django import forms
from .models import *
#-----------------------------------------------------
class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'published_year','description','is_borrowed']
#-----------------------------------------------------
class BorrowBookForm(forms.ModelForm):
    class Meta:
        model = Borrow
        fields = ['book']
#-----------------------------------------------------
