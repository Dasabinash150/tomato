from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.contrib.auth import authenticate,login,logout
# Create your views here.
def home(request):
    
    user = request.session.get('username')
    if user:
        user_object = User.objects.get(username=user)

        context = {
            'UO':user_object
        }
        return render(request, 'home.html',context)
    return render(request, 'home.html')
def master_home(request):
    return render(request, 'home.html')

def master_registration(request):
    EMFO = MasterForm()
    if request.method == "POST":
        MFDO = MasterForm(request.POST)
        if MFDO.is_valid():
            pw = MFDO.cleaned_data.get("password")
            MMFDO = MFDO.save(commit=False)
            MMFDO.set_password(pw)
            MMFDO.is_staff = True
            MMFDO.save()
            return HttpResponseRedirect(reverse("master_login"))
        else:
            return HttpResponse("invalid data")


    context = {
        'EMFO':EMFO,
    }
    return render(request, 'master_registration.html',context)

def master_login(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")

        user = authenticate(username=username,password=password)

        if user and user.is_active:
            if user.is_staff:
                login(request, user)
                request.session['username'] = username
                return redirect("home")

    return render(request, 'master_login.html')
def master_dashboard(request):
   

    return render(request, 'master_dashboard.html')

