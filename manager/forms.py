from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from tempus_dominus.widgets import DatePicker 
from .models import Order

class OrderForm(forms.Form):
    # class Meta:
    #     model = Order
    #     fields = ('order_name', 'customer', 'phone_number', 'deadline_date', 'price')

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.helper = FormHelper()
    #     self.helper.form_method = 'post'
    #     self.helper.add_input(Submit('submit', 'Add'))

    order_name = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Order name'}))
    customer = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Customer'}))
    phone_number = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Phone'}))
    status = forms.ChoiceField(choices=Order.ORDER_STATUSES) 
    deadline_date = forms.DateField(widget=DatePicker())
    price = forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Price'}))