from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .forms import *
# Create your views here.

def customer_registration(request):    
    ECFO = CustomerForm()
    if request.method == "POST":
        CFDO = CustomerForm(request.POST)
        if CFDO.is_valid():
            pw = CFDO.cleaned_data['password']
            MCFDO = CFDO.save(commit=False)
            MCFDO.set_password(pw)
            MCFDO.save()
            return HttpResponseRedirect(reverse('customer_login'))

    context = {
        'ECFO': ECFO
    }
    
    return render(request, 'customer_registration.html',context)
def customer_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)
        print(user)

        if user and user.is_active:
            login(request, user)
            request.session['username'] = username
            return HttpResponseRedirect(reverse('home'))

    return render(request, 'customer_login.html')
def customer_dashboard(request):
    
    return render(request, 'home.html')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))