from django.shortcuts import render, get_object_or_404
from django.views import generic
from django.utils import timezone
from django.urls import reverse
from django.http import HttpResponseRedirect
from .models import Order
from .forms import OrderForm


class IndexView(generic.ListView):
    template_name = 'orders/index.html'
    context_object_name = 'latest_orders_list'

    def get_queryset(self):
        return Order.objects.filter(add_date__lte=timezone.now()).order_by('-add_date')[:10]


class AllView(generic.ListView):
    template_name = 'orders/index.html'
    context_object_name = 'all_orders'

    def get_queryset(self):
        return Order.objects.all()


class DetailView(generic.DetailView):
    model = Order
    template_name = 'order/detail.html'
    

# class EditView(generic.TemplateView):


def add_order(request):
    new = Order(order_name=request.POST['ordername'], customer=request.POST['ordercustomer'],
                phone_number=request.POST['ordercustomercontact'], deadline_date=request.POST['orderdeadline'], price=request.POST['orderprice'])
    new.save()
    return HttpResponseRedirect(reverse('orders:detail', args=(new.id,)))
