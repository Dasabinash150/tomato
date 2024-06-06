from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from .forms import *
from django.contrib.auth import authenticate,login
from django.contrib import messages
# Create your views here.
def home(request):
    food_items = Item.objects.all()
    print(food_items)
    user = request.session.get('username')
    if user:
        user_object = User.objects.get(username=user)

        context = {
            'UO':user_object,
            'items':food_items
        }
        return render(request, 'home.html',context)
    return render(request, 'home.html',{'items':food_items})


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
def add_item(request):
    EIFO = AddItemForm()
    if request.method == "POST" and request.FILES:
        IFDO = AddItemForm(request.POST,request.FILES)
        if IFDO.is_valid():
            print(IFDO)
            IFDO.save()
            messages.success(request, 'Item added successfully.')
            return HttpResponseRedirect(reverse("add_item"))
        return HttpResponse('Invalid data')
    context = {
        'EIFO':EIFO
    }
    return render(request, 'master/add_item.html',context)
def master_dashboard(request):
   

    return render(request, 'master_dashboard.html')
def show_all_item(request):
    items = Item.objects.all()

    return render(request, 'master/show_all_item.html',{'items':items})

def update(request, pk):
    item = Item.objects.get(item_id=pk)
    print(item)
    # EIFO = AddItemForm(instance=item)
    if request.method == "POST":
        IFDO = AddItemForm(request.POST,request.FILES,instance=item)
        if IFDO.is_valid():
            print(IFDO)
            IFDO.save()
            messages.success(request, 'Item updates successfully.')
            return HttpResponseRedirect(reverse("show_all_item"))
        else:
            return HttpResponse('Invalid data')
    else:
        EIFO = AddItemForm(instance=item)
    context = {
        'EIFO':EIFO
    }
    return render(request, 'master/update_item.html',context)
def delete(request, pk):
    item = Item.objects.get(item_id=pk)
    item.delete()
    return HttpResponseRedirect(reverse('show_all_item'))