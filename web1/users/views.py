from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout



def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid(): 
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}!')
            return redirect('users/logIn.html')
    else:
        form = CreateUserForm()
    return render(request, 'users/register.html', {'form': form})


def login(request):
    if request.method == 'GET':
        return render(request, 'logIn')
    elif request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            return render(request, 'gp/index.html', {'error_message': 'Invalid username or password'})
