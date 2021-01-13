from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.views.generic import FormView
from django.utils import timezone
from django.urls import reverse, reverse_lazy
from django.http import HttpResponseRedirect
from .models import Order, Customer
from .forms import OrderForm


def index(request):
    lastest_orders_list = Order.objects.filter(
        add_date__lte=timezone.now()).order_by('-add_date')[:10]
    context = {'latest_orders_list': lastest_orders_list}
    return render(request, 'manager/last_orders.html', context)


def all_orders(request):
    all_orders_list = Order.objects.all()
    context = {'all_orders_list': all_orders_list}
    return render(request, 'manager/all_orders.html', context)


def all_customers(request):
    all_customer_list = Customer.objects.all()
    context = {'all_customer_list': all_customer_list}
    return render(request, 'manager/all_customers.html', context)


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'manager/order_detail.html'


class CustomerDetailView(generic.DetailView):
    model = Customer
    template_name = 'manager/customer_detail.html'


# class EditView(generic.TemplateView):


class AddOrder(FormView):
    form_class = OrderForm
    success_url = reverse_lazy('order_detail')
    template_name = 'manager/add_form.html'


# def add_order(request):
#     new = Order(order_name=request.POST['ordername'], customer=request.POST['ordercustomer'],
#                 phone_number=request.POST['ordercustomercontact'], deadline_date=request.POST['orderdeadline'], price=request.POST['orderprice'])
#     new.save()
#     return HttpResponseRedirect(reverse('orders:detail', args=(new.id,)))
