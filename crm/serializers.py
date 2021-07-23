from crm.models import Customer, Order
from rest_framework import serializers


class CustomerSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Customer
        fields = ['id', 'name', 'phone', 'insta']


class OrderSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Order
        fields = ['id', 'name', 'desc', 'customer', 'status', 'add_date', 'deadline_date', 'price']
