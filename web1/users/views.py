from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect

def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('logino')
    else:
        form = CreateUserForm()
    return render(request, 'users/register.html', {'form': form})


def login_view(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('gp-index')
        else:
            messages.error(request, "Invalid username or password.")
    return render(request, 'users/logIn.html')

def logout_view(request):
    logout(request)
    return redirect('gp-index')