from django.urls import path
from . import views

urlpatterns=[
    path('demo/', views.index1_view, name='index1'),
    path('demo/', views.our_members, name='our_members')
]