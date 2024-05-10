from django.urls import path
from .views import preLoginReg

urlpatterns = [
    path('preLoginReg', preLoginReg, name='preLoginReg'),
]