from django.urls import path
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

    path('', home, name='home'),
    path('user/', userPage, name='user_page'),
    path('products/', products, name='products'),
    path('customer/<str:pk_test>/', customer, name='customer'),

    path('create_order/<str:pk>/', createOrder, name="create_order"),
    path('update_order/<str:pk>/', updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', deleteOrder, name='delete_order'),
]