from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .forms import *
from master.models import Item
from django.contrib.auth.decorators import login_required
from django.contrib import messages

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



def customer_menu(request, type):
    if type == 'veg':
        items = Item.objects.filter(item_type='Veg')
    elif type == 'non-veg':
        items = Item.objects.filter(item_type='Non-Veg')
    elif type == 'all':
        items = Item.objects.all()
    d = {'items':items}
    # print(type)
    return render(request, 'customer_menu.html', d)


def addtocart(request):
    if request.method == 'POST':
        item_pk = request.POST.get('itempk')
        item_object = Item.objects.get(item_id=item_pk)
        UO = User.objects.get(username = request.session['username'])
        name = item_object.item_name
        price = item_object.item_price
        qty = request.POST.get('qty')
        print(UO)
        try:

            # cart_item = CartItems.objects.get(item_name=name)
            cart_item = CartItems.objects.get(cart_id=UO,item_name=name)
            print(cart_item)
            avl_qty = cart_item.qty    
            print(avl_qty)       
            cart_item.qty += int(qty)
            cart_item.total_price += cart_item.qty * cart_item.price
            cart_item.save()
            messages.success(request, f"Updated quantity for {name}.")
            
            return HttpResponseRedirect(reverse('view_cart'))    
        except CartItems.DoesNotExist:
            total_price = price * qty
            CO = CartItems(cart_id=UO, item_name=name, price=price, qty=qty,  inst='')
            CO.save()
            return HttpResponseRedirect(reverse('view_cart'))
login_required(login_url='customer_login')
def view_cart(request):
    # UO = request.session['username']
    UO = request.session.get('username')
    print(UO)
    if not UO:
        return redirect('customer_login')
    
    carts_items = CartItems.objects.filter(cart_id__username=UO)
        
    overall_total_price = sum(item.total_price for item in carts_items)
    print(overall_total_price)
    print(carts_items)
    context = {
        'CI': carts_items,
        'overall_total_price':overall_total_price
    }
    return render(request, 'view_cart.html', context)
