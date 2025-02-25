from django import forms
from orders.models import *

class OrderchangeForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'