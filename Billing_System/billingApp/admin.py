from django.contrib import admin
from billingApp.models import Product,Denomination,BillDetails,BillInfo
admin.site.register(Product)
admin.site.register(BillInfo)
admin.site.register(BillDetails)
admin.site.register(Denomination)