from django import forms
from django.forms import modelformset_factory
from billingApp.models import BillInfo,Product,Denomination,BillDetails
class CustomerForms(forms.ModelForm):
    class Meta:
        model=BillInfo
        fields =['customer_email']
class DenominationForms(forms.ModelForm):
    class Meta :
        model= Denomination
        exclude =["billno"]
class ProductForm(forms.ModelForm):
    class Meta:
        model=Product
        fields =['product_id']
class BillItemForm(forms.ModelForm):
    class Meta:
        model = BillDetails
        fields = ['product_ID', 'quantity']
    
BillItemFormSet = modelformset_factory(
    BillDetails,
    form=BillItemForm,
    extra=1,  # Start with one form; more can be added dynamically
)