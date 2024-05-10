"""
URL configuration for myProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from demo import views
import all_in_one.views







urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index1_view, name='index1'),
    

    
    path('pay/', all_in_one.views.pay, name='pay'),
    path('pay1/', all_in_one.views.pay1, name='pay1'),
    path('savemarchant/', all_in_one.views.saveMarchant, name='savemarchant'),
    path('our_members/', all_in_one.views.our_members, name='our_members'),
    
    
    
    #path('index', views.index,'index.urls'),
    path('menu/', include('menu.urls')),
    path('login/', include('login.urls')),
    path('register/', include('register.urls')),
    path('contact/', include('contact.urls')),
    path('payment/', include('payment.urls')),
    path('about/', include('about.urls')),
    path('learnMore/', include('learnMore.urls')),
    path('preLoginReg/', include('preLoginReg.urls')),
    path('specialOffer/', include('specialOffer.urls')),
    path('profile/', include('profile1.urls')),
    
    
    

    
   
    
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)