from django.urls import path
from . import views

app_name = 'manager'
urlpatterns = [
    path('', views.index, name='index'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('allorders/', views.all_orders, name='all_orders'),
    path('allcustomers/', views.all_customers, name='all_customers'),
    path('addorder/', views.addorder, name='add_order'),
]