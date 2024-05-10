from django.shortcuts import render,HttpResponse

# Create your views here.
def pay(request):
    return render(request,'pay.html')

def pay1(request):
    return render(request,'pay1.html')

def saveMarchant(request):
    return render(request,'pay1.html')

def our_members(request):
    return render(request,'our_members.html')