from django.contrib import admin
from .models import Order

class OrderAdmin(admin.ModelAdmin):
    list_display = ('order_name', 'customer', 'add_date', 'days_left')
    list_filter = ['add_date']
    search_fields = ['order_name']

admin.site.register(Order, OrderAdmin)
