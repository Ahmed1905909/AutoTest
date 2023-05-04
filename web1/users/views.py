from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
from.forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect



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
    return render(request, 'users/register.html', {'form': form})


def login(request):
    if request.method == 'POST':
        print('Form submitted as POST request')
        username = request.POST['username']
        password = request.POST['password1']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('gp/index.html')
        else:
         
            return redirect('login')
    else:
        return render(request, 'users/logIn.html')