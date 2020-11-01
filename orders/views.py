from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Order
from .forms import OrderForm


def index(request):
    lastest_orders_list = Order.objects.filter(add_date__lte=timezone.now()).order_by('-add_date')[:10]
    context = {'latest_orders_list': lastest_orders_list}
    return render(request, 'orders/base_last_orders.html', context)


def all_view(request):    
    all_orders_list = Order.objects.all()
    context = {'all_orders_list': all_orders_list}
    return render(request, 'orders/base_all_orders.html', context)


class DetailView(generic.DetailView):
    model = Order
    template_name = 'orders/detail.html'
    

# class EditView(generic.TemplateView):


# def add_order(request):
#     new = Order(order_name=request.POST['ordername'], customer=request.POST['ordercustomer'],
#                 phone_number=request.POST['ordercustomercontact'], deadline_date=request.POST['orderdeadline'], price=request.POST['orderprice'])
#     new.save()
#     return HttpResponseRedirect(reverse('orders:detail', args=(new.id,)))
