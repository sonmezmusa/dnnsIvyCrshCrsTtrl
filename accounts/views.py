from django.shortcuts import render, HttpResponse, redirect
from .models import *
from .forms import *
from django.forms import inlineformset_factory

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


def createOrder(request, pk):
    #if request.method == 'POST':
    #    print('Printing POST:', request.POST)

    OrderFormSet = inlineformset_factory(Customer, Order, fields=('product', 'status'), extra=10)
    customer = Customer.objects.get(id=pk)
    formset = OrderFormSet(queryset=Order.objects.none(), instance=customer)
    #form = OrderForm(request.POST or None, initial={'customer' : customer})
    if request.method == 'POST':
        formset = OrderFormSet(request.POST, instance=customer)
        if formset.is_valid():
            formset.save()
            return redirect('/')
    context = {
        'formset' : formset
    }
    return render(request, 'accounts/order_form.html', context)


def updateOrder(request, pk):
    order = Order.objects.get(id=pk)
    form = OrderForm(request.POST or None, instance=order)
    if form.is_valid():
        form.save()
        return redirect('/')
    context = {
        'form' : form
    }
    return render(request, 'accounts/order_form.html', context)


def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    context = {
        'item' : order
    }
    return render(request, 'accounts/delete.html', context)