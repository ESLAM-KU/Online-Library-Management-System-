from django.db import models
from django.conf import settings
from django.core.validators import EmailValidator
from django.utils import timezone
from django.contrib.auth import get_user_model
User = get_user_model()
#-----------------------------------------------------
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    published_year = models.PositiveIntegerField()
    description = models.TextField()
    is_borrowed = models.BooleanField(default=False)
    # -------------------
    def __str__(self):
        return self.title
#-----------------------------------------------------
class Borrow(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    student_email = models.EmailField(validators=[EmailValidator()],null=True,blank=True)
    borrow_date = models.DateTimeField(default=timezone.now)
    return_date = models.DateTimeField(null=True)
    # -------------------
    def __str__(self):
        student_name = User.objects.filter(email=self.student_email).first()
        if student_name:
            student_name = student_name.username
        else:
            student_name = "Unknown Student"
        return f"{student_name} borrowed {self.book.title}"
#-----------------------------------------------------
