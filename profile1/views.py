# profile1/views.py
from django.shortcuts import render, redirect
from .forms import ProfileForm
from .models import Profile

def profile_form(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile_detail')
    else:
        form = ProfileForm()
    return render(request, 'profile1_form.html', {'form': form})

def profile_detail(request):
    profiles = Profile.objects.all()
    return render(request, 'profile_detail.html', {'profiles': profiles})
