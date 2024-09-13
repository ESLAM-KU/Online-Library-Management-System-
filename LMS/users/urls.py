from django.urls import path
from .views import *
from django.contrib.auth.views import  LogoutView, PasswordChangeView, PasswordChangeDoneView

urlpatterns = [
    path('register/student/',register_student, name='register_student'),
    path('register/mod/',register_mod, name='register_mod'),
    path('', users_login, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('profile/', profile, name='profile'),
    path('profile/edit/', edit_user_profile, name='edit_user_profile'),
    path('password_change/', PasswordChangeView.as_view(template_name='users/password_change.html'), name='password_change'),
    path('password_change/done/', PasswordChangeDoneView.as_view(template_name='users/password_change_done.html'), name='password_change_done'),
    path('students/',student_list, name='student_list'),
    path('borrowlist/',borrow_list, name='borrow_list'),

]
