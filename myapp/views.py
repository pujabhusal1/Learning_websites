from django.shortcuts import render, redirect
from datetime import datetime
from myapp.models import Contact
from django.utils import timezone
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .forms import LoginForm, SignUpForm
from django.shortcuts import render





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

def signup(request):
    return render(request, "signup.html")



def contact(request):#corrested
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date=timezone.now())
        contact.save()
        
        return redirect('contact')  # Redirect to the contact page or another page after successful submission

    return render(request, 'contact.html')# end corrected




# myapp/views.py



# myapp/views.py

#login/signup

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            # Process login
            pass
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})

def signup_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            # Process signup
            pass
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})


#login/signup

# Define other view functions like index, services, about, contact as needed


# Define other view functions like index, services, about, contact as needed
