from django.shortcuts import render, redirect
from datetime import datetime
from myapp.models import Contact
from django.utils import timezone
from django.contrib import messages

def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')

from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def services(request):
    return render(request, 'services.html')

def about(request):
    return render(request, 'about.html')

def login(request):
    return render(request, 'login.html')



def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=timezone.now())
        contact.save()
        
        return redirect('contact')  # Redirect to the contact page or another page after successful submission

    return render(request, 'contact.html')
