from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
# Create your views here.



def registerPage(request):
    form = CreateUserForm()
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            messages.success(request, user + 'is created ')
            return redirect('Login_Page')
            

    context = {'form':form}
    return render (request, 'accounts/registerPage.html', context)


def loginPage(request):
    if request.method =='POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username = username, password=password)

        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            messages.info(request, 'USERNAME or PASSWORD is wrong')

    
    context = {}
    return render (request, 'accounts/loginPage.html', context)


def logoutUser(request):
    logout(request)
    return redirect('Login_Page')