from django.forms import ModelForm, TextInput, Textarea, ModelChoiceField
from .models import Order, Customer


class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ['name', 'desc', 'customer', 'deadline_date', 'price']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            "desc": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            "customer": ModelChoiceField(queryset=Customer.objects.all(), to_field_name="name"), 
            # attrs={
            #     'class': 'form-control',
            #     'placeholder': 'Description'
            # }),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price'
            }),
        }
