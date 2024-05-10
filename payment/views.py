from django.shortcuts import render
from .models import Payment
from django.http import HttpResponse

def payment(request):
    if request.method == "POST":
        data = Payment()
        data.name = request.POST.get('name')
        data.epin = request.POST.get('epin')
        data.save()
        return render(request, 'index1.html')  # Corrected line: render 'index1.html' template
        
    return render(request, 'payment.html')
