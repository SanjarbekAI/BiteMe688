from django import forms
from pages.models import EmailModel, OrderModel


class EmailForm(forms.ModelForm):
    class Meta:
        model = EmailModel
        fields = ['email']


class OrderForm(forms.ModelForm):
    class Meta:
        model = OrderModel
        fields = '__all__'