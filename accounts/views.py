from django.shortcuts import render, HttpResponse

# Create your views here.

# anasayfa
def home(request):
    return render(request, 'accounts/dashboard.html')


# ürünler
def products(request):
    return render(request, 'accounts/products.html')


# müşteri
def customer(request):
    return render(request, 'accounts/customer.html')