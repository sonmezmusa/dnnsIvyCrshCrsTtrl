from django.urls import path
from django.contrib.auth import views as auth_views
from .views import *

app_name = 'accounts'

urlpatterns = [
    path('register/', registerPage, name='register'),
    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

    path('', home, name='home'),
    path('user/', userPage, name='user_page'),

    path('account/', accountSettings, name='account'),

    path('products/', products, name='products'),
    path('customer/<str:pk_test>/', customer, name='customer'),

    path('create_order/<str:pk>/', createOrder, name="create_order"),
    path('update_order/<str:pk>/', updateOrder, name='update_order'),
    path('delete_order/<str:pk>/', deleteOrder, name='delete_order'),

    #path('reset_password/',
    # auth_views.PasswordResetView.as_view(template_name='accounts/password_reset.html'),
    # name='reset_password'),
    
    #path('reset_password_sent/',
    # auth_views.PasswordResetDoneView.as_view(),
    # name='password_reset_done'),
    
    #path('reset/<uidb64>/<token>/',
    # auth_views.PasswordResetConfirmView.as_view(),
    # name='password_reset_confirm'),
    
    #path('reset_password_complete/',
    # auth_views.PasswordResetCompleteView.as_view(),
    # name='password_reset_complete'),
]



# All authentication views
# https://docs.djangoproject.com/en/3.1/topics/auth/default/#all-authentication-views

# 1 - Submit email form                         //PasswordResetView.as_view()
# 2 - Email sent success message                //PasswordResetDoneView.as_view()
# 3 - Link to password Rest form in email       //PasswordResetConfirmView.as_view()
# 4 - Password successfully changed message     //PasswordResetCompleteView.as_view()