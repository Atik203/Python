
from django.urls import path

from . import views

urlpatterns = [
    path('about/', views.about, name='about'),
    path('form/', views.form, name='form'),
    path('form2/', views.form2, name='form2'),
    path('DjangoForm/', views.PasswordForm, name='DjangoForm')
]
