from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib import messages
from .forms import RegistrationForm, LoginForm
def register_view(request):
    if request.user.is_authenticated: return redirect('/profile/')
    if request.method=='POST':
        form=RegistrationForm(request.POST)
        if form.is_valid():
            user=form.save(); login(request,user)
            messages.success(request,f'Welcome, {user.username}!')
            return redirect('/profile/')
    else: form=RegistrationForm()
    return render(request,'accounts/register.html',{'form':form})
def login_view(request):
    if request.user.is_authenticated: return redirect('/profile/')
    if request.method=='POST':
        form=LoginForm(request,data=request.POST)
        if form.is_valid(): login(request,form.get_user()); return redirect('/profile/')
        messages.error(request,'Invalid credentials.')
    else: form=LoginForm()
    return render(request,'accounts/login.html',{'form':form})
def logout_view(request):
    logout(request); return redirect('/')
