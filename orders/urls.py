from django.urls import path
from . import views

app_name = 'crm'
urlpatterns = [
    path('', views.index, name='index'),
    path('customer/<int:pk>/', views.CustomerDetailView.as_view(), name='customer_detail'),
    path('order/<int:pk>/', views.OrderDetailView.as_view(), name='order_detail'),
    path('all/', views.all_view, name='all'),
    path('add/', views.AddOrder.as_view(), name='add'),
]