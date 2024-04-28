from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import CustomUserCreationForm, CustomAuthenticationForm

# Placeholder view for portfolio page
def portfolio_view(request):
    # Add your view logic here
    return render(request, 'portfolio.html')

# Placeholder view for about page
def about_page(request):
    # Add your view logic here
    return render(request, 'about.html')

# Placeholder view for contact page
def contact_page(request):
    # Add your view logic here
    return render(request, 'contact.html')

@login_required
def dashboard(request):
    # Add your view logic here
    return render(request, 'dashboard.html')

def login_view(request):
    form = CustomAuthenticationForm(request, data=request.POST or None)
    if request.method == 'POST' and form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'login.html', {'form': form})

@login_required
def logout_view(request):
    logout(request)
    messages.success(request, 'You have successfully logged out.')
    return redirect('login')

def register(request):
    form = CustomUserCreationForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, 'Registration successful. Welcome to your dashboard!')
        return redirect('dashboard')
    else:
        for field, errors in form.errors.items():
            for error in errors:
                messages.error(request, f"{field}: {error}")
    return render(request, 'register.html', {'form': form})
