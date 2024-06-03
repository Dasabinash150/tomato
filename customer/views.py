from django.shortcuts import render
from django.http import HttpResponse
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
            return HttpResponse("Registration success")

    context = {
        'ECFO': ECFO
    }
    
    return render(request, 'customer_registration.html',context)