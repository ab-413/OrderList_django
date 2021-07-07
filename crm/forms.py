from django.forms import  TextInput, Textarea, ModelChoiceField, DateInput
from .models import Order, Customer
from bootstrap_modal_forms.forms import BSModalModelForm


class CustomerForm(BSModalModelForm):
    class Meta:
        model = Customer
        fields = ['name', 'phone']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name'
            }),
            "phone": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone'
            }),
        }


class OrderForm(BSModalModelForm):
    class Meta:
        model = Order
        customer = ModelChoiceField(queryset=Customer.objects.all(), to_field_name="customer", required=False)
        fields = ['name', 'desc', 'customer', 'deadline_date', 'price']
        widgets = {
            "name": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Name',
                'autocomplete': 'off'
            }),
            "desc": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Description'
            }),
            "deadline_date": DateInput(attrs={
                'class':'datepicker',
                'data-date-format': 'yyyy-mm-dd',
                'autocomplete': 'off'
            }, ),
            "price": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Price',
                'autocomplete': 'off'
            }),
        }