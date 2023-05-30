from django.db import models
from administrator.models import BatchNumber
# Create your models here.


class  Product(models.Model):
    productId =models.CharField(max_length=255,unique=True)
    name =models.CharField(max_length=255)
    stock =models.IntegerField()
    expireDate =models.DateField()
    # batchNumber =models.ForeignKey(BatchNumber,on_delete=models.DO_NOTHING)
    costPrice=models.FloatField()
    selingPrice =models.IntegerField()
    def __str__(self):
        return self.name
    
class Customer(models.Model):
    name =models.CharField(max_length=255)
    phoneNumber =models.CharField(max_length=255)
    location =models.CharField(max_length=255)
    # custmerId =models.UUIDField()
    def __str__(self):
        return self.name
    

class Order(models.Model):
    orderNo =models.CharField(max_length=255, unique=True)
    product =models.ForeignKey(Product,on_delete=models.CASCADE)
    # customer =models.(max_length=300)
    quantity =models.IntegerField()
    # Status =(
    #     ('Pending','Pendind'),
    #     ('Full Paid','Full Paid'),
    #     ('Not Paid','Not Paid'),
    # )
    # paymentstatus=models.CharField(max_length=200,choices=Status)
    amountpaid=models.FloatField()
    # pendingamount=models.FloatField()
    transId= models.CharField(max_length=255,unique=True)
    orderstatus =models.CharField(max_length=255,blank=True, null=True)
    def __str__(self):
        return self.orderNo
    

class Transaction(models.Model):
    transId= models.CharField(max_length=255,unique=True)
    orderDetails=models.ForeignKey(Order,on_delete=models.DO_NOTHING)
    customerDetails=models.ForeignKey(Customer,on_delete=models.DO_NOTHING)
    def __str__(self):
        return self.transId
    

