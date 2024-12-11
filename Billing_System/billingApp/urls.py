from django.urls import path
from billingApp.views import generateBill

urlpatterns = [
   path("",generateBill),
]
