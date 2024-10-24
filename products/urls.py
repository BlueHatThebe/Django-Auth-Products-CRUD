from django.urls import path
from django.contrib.auth import views as auth_views
from .views import product_list, product_create, product_update, product_delete, register

urlpatterns = [
    path('register/', register, name='register'),
    path('', product_list, name='product_list'),
    path('create/', product_create, name='product_create'),
    path('update/<int:pk>/', product_update, name='product_update'),
    path('delete/<int:pk>/', product_delete, name='product_delete'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),  # Add this line
    path('accounts/login/', auth_views.LoginView.as_view(template_name='products/login.html'), name='login'),
]

 