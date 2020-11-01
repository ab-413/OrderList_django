from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from .models import Order

class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ('order_name', 'customer', 'phone_number', 'deadline_date', 'price')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Add'))