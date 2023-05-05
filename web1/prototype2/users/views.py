from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout



def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('login')
    else:
        form = CreateUserForm()
    return render(request, 'signup', {'form': form})


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password =request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect(reverse('index'))
        else:
            messages.info(request, 'Username OR password is incorrect')
    return render(request,'login',{})


