from django.shortcuts import render
from billingApp.models import BillInfo,Product
from billingApp.forms import  CustomerForms

def generateBill(request):
    customform =CustomerForms()
    content={
        'customform':customform
    }
    
    return render(request,"generateInvoice.html",content)
