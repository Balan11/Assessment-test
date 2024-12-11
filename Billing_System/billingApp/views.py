from django.shortcuts import render,redirect
from billingApp.models import BillInfo,Product,Denomination,BillDetails
from billingApp.forms import  CustomerForms,DenominationForms,BillItemFormSet

def generateBill(request):
    customform =CustomerForms()
    denominationForms = DenominationForms()
    content={
        'customform':customform,
        'denominationForms':denominationForms,
        'BillItemFormSet':BillItemFormSet()
    }
    if request.method =="POST":
        return redirect("billingpage",id)    
    return render(request,"generateInvoice.html",content)
def billingpage(request,id):
    bill=BillInfo.objects.get(id=id)
    billinfo = BillDetails.objects.get(billno=bill)
    content={}
    return render(request,"invoice.html",content)
