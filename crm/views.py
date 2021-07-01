from django.shortcuts import render, get_object_or_404, redirect
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
    return render(request, 'crm/last_orders.html', context)


def all_orders(request):
    all_orders_list = Order.objects.all()
    context = {'all_orders_list': all_orders_list}
    return render(request, 'crm/all_orders.html', context)


def all_customers(request):
    all_customer_list = Customer.objects.all()
    context = {'all_customer_list': all_customer_list}
    return render(request, 'crm/all_customers.html', context)


class OrderDetailView(generic.DetailView):
    model = Order
    template_name = 'crm/order_detail.html'


class CustomerDetailView(generic.DetailView):
    model = Customer
    template_name = 'crm/customer_detail.html'


def addorder(request):
    error = ''
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crm:index')
        else:
            error = 'Form error'

    form = OrderForm()
    context = {
        'form': form,
        'error': error
    }
    return render(request, 'crm/add_form.html', context)