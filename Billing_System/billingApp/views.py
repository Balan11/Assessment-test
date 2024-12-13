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
        return redirect("billingpage",billid.id)    
    content={
        'customform':customform,
        'denominationForms':denominationForms,
        'BillItemFormSet':BillItemFormSet(queryset=BillDetails.objects.none())
    }
    return render(request,"generateInvoice.html",content)
def billingpage(request,id):
    bill=BillInfo.objects.get(id=id)
    billinfo = BillDetails.objects.filter(billno=bill)
    billDetailsCalc=[]
    total_tax =0
    total_price = 0
    totalprice_without =0
    for i in billinfo:
        d={}
        d['item'] = i.product_ID.name 
        d['Qty'] = i.quantity
        d['unitprice'] = i.product_ID.unit_price
        d['purchaseamt'] = i.product_ID.unit_price
        d['tax'] = i.product_ID.tax_percentage
        d['taxamount'] = i.quantity * (( i.product_ID.unit_price * i.product_ID.tax_percentage)/100)
        total_tax+= i.quantity * (( i.product_ID.unit_price * i.product_ID.tax_percentage)/100)
        d['totalprice'] = (i.quantity * (( i.product_ID.unit_price * i.product_ID.tax_percentage)/100))+(i.quantity* i.product_ID.unit_price)
        totalprice_without+=(i.quantity* i.product_ID.unit_price)
        total_price+=(i.quantity * (( i.product_ID.unit_price * i.product_ID.tax_percentage)/100))+(i.quantity* i.product_ID.unit_price)
        billDetailsCalc.append(d)
    cashamt=Denomination.objects.get(billno=bill)
    balance=cashamt.cashPaidbyCustomer-total_price
    deno=calculatedenomination(cashamt.cashPaidbyCustomer,total_price)
    content={"bill":bill,'billdetails':billDetailsCalc,"totaltax":total_tax,"totalpricedetails":total_price,"balance":balance}
    content.update({"deno":deno})
    content.update({'totalprice_without':totalprice_without})
    print(content)
    return render(request,"invoice.html",content)
                              
def calculatedenomination(cash,total):
    balance = cash-total
    details=[]
    denomination = [2000,500,200,100,50,20,10,5,2,1]
    for denom in sorted(denomination, reverse=True):
        distribution = {}
        count = int(balance // denom)
        if count > 0:
            distribution["denomination"] = denom
            distribution["count"] = count
        balance = round(balance % denom, 2)
        details.append(distribution)  
    return details
    