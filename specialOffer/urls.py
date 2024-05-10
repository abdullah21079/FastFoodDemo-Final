from django.urls import path
from .views import specialOffer

urlpatterns = [
    path('specialOffer', specialOffer, name='specialOffer'),
]