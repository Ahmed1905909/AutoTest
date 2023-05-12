from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.urls import reverse
#from .forms import CreateUserForm
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import HttpResponseRedirect
from .forms import CustomUserCreationForm

# def register(request):
#     if request.method == 'POST':
#         form = CreateUserForm(request.POST)
#         if form.is_valid(): 
#             form.save()
#             username = form.cleaned_data.get('username')
#             messages.success(request, f'Account created for {username}!')
#             return redirect('logino')
#     else:
#         form = CreateUserForm()
#     return render(request, 'users/register.html', {'form': form})


# def login_view(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')
#         user = authenticate(request, username=username, password=password)
#         if user is not None:
#             login(request, user)
#             return redirect('gp/index')
#         else:
#             messages.error(request, "Invalid username or password.")
#     return render(request, 'users/logIn.html')

# def logout_view(request):
#     logout(request)
#     return redirect('gp/index')





def signup(request):
    if request.user.is_authenticated:
        return redirect('signin')
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, f'Account created for {username}!')
            return redirect('index')
        else:
            print("error")
            return render(request, 'users/signup.html', {'form': form})
    else:
        form = CustomUserCreationForm()
        return render(request, 'users/signup.html', {'form': form})
    

def signin(request):
    if request.user.is_authenticated:
        return render(request, 'gp/index.html')
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index') #profile
        else:
            msg = 'Error Login'
            form = AuthenticationForm(request.POST)
            return render(request, 'users/login.html', {'form': form, 'msg': msg})
    else:
        form = AuthenticationForm()
        return render(request, 'users/login.html', {'form': form})
    
def signout(request):
    logout(request)
    return redirect('index')


def profile(request):
    return redirect('profile') 