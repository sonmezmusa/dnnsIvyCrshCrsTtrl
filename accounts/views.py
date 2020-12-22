from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *

# Create your views here.

# anasayfa
def home(request):
    orders = Order.objects.all()
    customers = Customer.objects.all()

    total_customers = customers.count()

    total_orders = orders.count()
    delivered = orders.filter(status='Delivered').count()
    pending = orders.filter(status='Pending').count()

    context = {
        'orders' : orders,
        'customers' : customers,
        'total_orders' : total_orders,
        'delivered' : delivered,
        'pending' : pending
    }
    return render(request, 'accounts/dashboard.html', context)


# ürünler
def products(request):
    products = Product.objects.all()
    context = {
        'products' : products
    }
    return render(request, 'accounts/products.html', context)


# müşteri
def customer(request, pk_test):
    customer = Customer.objects.get(id=pk_test)
    orders = customer.order_set.all()
    total_orders = orders.count()
    context = {
        'customer' : customer,
        'orders' : orders,
        'total_orders' : total_orders
    }
    return render(request, 'accounts/customer.html', context)


def createOrder(request):
    #if request.method == 'POST':
    #    print('Printing POST:', request.POST)

    form = OrderForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form' : form
    }
    return render(request, 'accounts/order_form.html', context)