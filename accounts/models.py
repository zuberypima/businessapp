from django.db import models
from register.models import Order
# Create your models here.

class Invoice(models.Model):
    invoiceNo= models.CharField(max_length=255,unique=True)
    orderDetails=models.ForeignKey(Order,on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.invoiceNo
    



# class Transaction(models.Model):
#     transId= models.CharField(max_length=255,unique=True)
#     orderDetails=models.ForeignKey(Order,on_delete=models.DO_NOTHING)
#     customerDetails=models.ForeignKey()

#     def __str__(self):
#         return self.invoiceNo
    