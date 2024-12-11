from django import forms
from billingApp.models import BillInfo,Product
class CustomerForms(forms.ModelForm):
    class Meta:
        model=BillInfo
        fields =['customer_email']
