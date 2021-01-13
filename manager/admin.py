from django.contrib import admin
from .models import Order, Customer

class OrderAdmin(admin.ModelAdmin):
    list_display = ('name', 'customer', 'add_date', 'days_left')
    list_filter = ['add_date']
    search_fields = ['name']

admin.site.register(Order, OrderAdmin)
admin.site.register(Customer)
