from django.urls import path
from billingApp.views import generateBill,billingpage

urlpatterns = [
   path("",generateBill,name="generateBill"),
   path("invoice/<int:id>",billingpage,name="billingpage")
]
