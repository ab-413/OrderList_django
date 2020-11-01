from django.urls import path
from . import views

app_name = 'orders'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('<int:pk>/', views.DetailView.as_view(), name='detail'),
    path('all/', views.AllView.as_view(), name='all'),
    path('add/', views.add_order, name='add'),
]