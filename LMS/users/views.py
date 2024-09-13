from django.shortcuts import render, redirect
from django.contrib.auth import login,authenticate
from .forms import *
from django.contrib.auth.decorators import login_required
from django.contrib.auth.decorators import user_passes_test
from django.contrib.auth.forms import AuthenticationForm
from .models import *
from books.models import *
#-----------------------------------------------------
def is_mod(user):
    return user.is_mod or user.is_staff
# -----------------------------------------------------
def register_student(request):
    if request.method == 'POST':
        form =RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_student = True
            user.save()
            login(request, user)
            return redirect('book_list')
    else:
        form =RegistrationForm()
    return render(request, 'users/register_student.html', {'form': form})
# -----------------------------------------------------
def register_mod(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_mod = True
            user.is_staff = True
            user.save()
            login(request, user)
            return redirect('book_list')
    else:
        form = RegistrationForm()
    return render(request, 'users/register_mod.html', {'form': form})
# -----------------------------------------------------
@login_required
def profile(request):
    return render(request, 'users/profile.html')
# -----------------------------------------------------
@login_required
def edit_user_profile(request):
    if request.method == 'POST':
        form = EditProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = EditProfileForm(instance=request.user)
    return render(request, 'users/edit_profile.html', {'form': form})
# -----------------------------------------------------
def users_login(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None and user.is_active:
                login(request, user)
                return redirect('book_list')
            return render(request, 'users/login.html', {'form': form, 'error': 'Invalid credentials'})
    return render(request, 'users/login.html', {'form': form})
# -----------------------------------------------------
@login_required
def student_list(request):
    i_d = request.GET.get('i_d')
    students = CustomUser.objects.filter(is_student=True)
    if i_d:
        students = students.filter(id=i_d)
    return render(request, 'users/student_list.html', {'students': students})
# -----------------------------------------------------
@user_passes_test(is_mod)
def borrow_list(request):
    borrows = Borrow.objects.all()
    students = CustomUser.objects.filter(is_student=True)
    return render(request, 'users/borrow_list.html', {'borrows': borrows, 'students': students})

# -----------------------------------------------------
