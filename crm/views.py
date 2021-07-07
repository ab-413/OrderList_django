from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.views import generic
from django.utils import timezone
from .models import Order, Customer
from .forms import OrderForm, CustomerForm
from bootstrap_modal_forms.generic import BSModalCreateView, BSModalUpdateView, BSModalReadView, BSModalDeleteView
from django.urls import reverse_lazy
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import CustomerSerializer, OrderSerializer


class CustomerViewSet(viewsets.ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer
    permission_classes = [permissions.IsAuthenticated]


class OrdersViewSet(viewsets.ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
    permission_classes = [permissions.IsAuthenticated]


def index(request):
    lastest_orders_list = Order.objects.filter(
        add_date__lte=timezone.now()).order_by('-add_date')[:10]
    context = {'latest_orders_list': lastest_orders_list}
    return render(request, 'crm/order_last.html', context)


def all_orders(request):
    all_orders_list = Order.objects.all()
    context = {'all_orders_list': all_orders_list}
    return render(request, 'crm/all_orders.html', context)


def all_customers(request):
    all_customer_list = Customer.objects.all()
    context = {'all_customer_list': all_customer_list}
    return render(request, 'crm/all_customers.html', context)


def update_status(request, id):
    order = get_object_or_404(Order, pk=id)
    status = request.GET.get(Order.status)
    if status:
        order.status = status
        order.save()
    else:
        raise Http404
    context = {'id': order.id, 'status': order.status}
    return render(request, 'crm/all_orders.html', context)


def delete_order(request, pk):
    Order.objects.filter(id=pk).delete()
    return render(request, 'crm/all_orders.html')


class CustomerDetailView(generic.DetailView):
    model = Customer
    template_name = 'crm/customer_detail.html'


class CustomerAddView(BSModalCreateView):
    template_name = 'crm/add_customer.html'
    form_class = CustomerForm
    success_message = 'Success: Customer was added.'
    success_url = reverse_lazy('crm:index')


class OrderAddView(BSModalCreateView):
    template_name = 'crm/order_add.html'
    form_class = OrderForm
    success_message = 'Success: Order was added.'
    success_url = reverse_lazy('crm:index')


class OrderEditView(BSModalUpdateView):
    model = Order
    template_name = 'crm/order_edit.html'
    form_class = OrderForm
    success_message = 'Success: Order was edited.'
    success_url = reverse_lazy('crm:all_orders')


class OrderDetailView(BSModalReadView):
    model = Order
    template_name = 'crm/order_detail.html'


class OrderDeleteView(BSModalDeleteView):
    model = Order
    template_name = 'crm/order_delete.html'
    success_message = 'Success: Order was deleted.'
    success_url = reverse_lazy('crm:all_orders')
