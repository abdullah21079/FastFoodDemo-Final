from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse

def contact(request):
    if request.method == "POST":
        data = Contact()
        data.name = request.POST.get('name')
        data.email = request.POST.get('email')
        data.address = request.POST.get('address')
        data.message = request.POST.get('message')
        data.save()
        return render(request, 'index1.html')  # Corrected line: render 'index1.html' template
        
    return render(request, 'contact.html')
