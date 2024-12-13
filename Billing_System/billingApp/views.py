from django.shortcuts import render,redirect
from billingApp.models import BillInfo,Product,Denomination,BillDetails
from billingApp.forms import  CustomerForms,DenominationForms,BillItemFormSet

def generateBill(request):
    customform =CustomerForms()
    denominationForms = DenominationForms()
   
    if request.method =="POST":
        customform =CustomerForms(request.POST)
        denominationForms = DenominationForms(request.POST)
        billdetails=BillItemFormSet(request.POST, queryset=BillDetails.objects.none())
        if  customform.is_valid() and billdetails.is_valid() and denominationForms.is_valid():
            billid=customform.save()
            for product in billdetails:
                if product.cleaned_data:
                    newItem = product.save(commit=False)
                    newItem.billno = billid
                    newItem.save()
            denomination=denominationForms.save(commit=False)
            denomination.billno=billid
            denomination.save()
        return redirect("generateBill")    
    content={
        'customform':customform,
        'denominationForms':denominationForms,
        'BillItemFormSet':BillItemFormSet(queryset=BillDetails.objects.none())
    }
    return render(request,"generateInvoice.html",content)
def billingpage(request,id):
    bill=BillInfo.objects.get(id=id)
    cust= BillInfo.objects.get(id=id)
    billinfo = BillDetails.objects.get(billno=bill)
    content={"billinfo":billinfo}
    print(content.get("billinfo").billno.customer_email)
    return render(request,"invoice.html",content)
3.                                  