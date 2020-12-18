from django.shortcuts import render, HttpResponse

# Create your views here.

# anasayfa
def home(request):
    return render(request, 'accounts/dashboard.html')


# ürünler
def products(request):
    return HttpResponse('<h1>Wellcome "products" page"</h1>')


# müşteri
def customer(request):
    return HttpResponse('<h1>Wellcome "customer" page"</h1>')