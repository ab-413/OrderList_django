from django.urls import path
from . import views

app_name = 'crm'
urlpatterns = [
    path('', views.index, name='index'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('allorders/', views.all_orders, name='all_orders'),
    path('allcustomers/', views.all_customers, name='all_customers'),
    path('addcustomer/', views.CustomerAddView.as_view(), name='add_customer'),
    path('addorder/', views.OrderAddView.as_view(), name='add_order'),
    path('update_status/<int:pk>', views.update_status),
    path('order/<int:pk>/edit/', views.OrderEditView.as_view(), name='edit_order'),
    path('order/<int:pk>/delete/', views.OrderDeleteView.as_view(), name='delete_order'),
]