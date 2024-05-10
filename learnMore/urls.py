from django.urls import path
from .views import learnMore

urlpatterns = [
    path('learnMore', learnMore, name='learnMore'),
]