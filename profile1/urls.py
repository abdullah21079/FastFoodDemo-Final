# profile1/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('profile1-form/', views.profile_form, name='profile1_form'),
    path('profile-detail/', views.profile_detail, name='profile_detail'),
]
