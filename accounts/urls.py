from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('', home, name='home'),
    path('products/', products, name='products'),
    path('customer/<str:pk_test>/', customer, name='customer'),
    path('create_order/', createOrder, name="create_order"),
]