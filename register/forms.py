from django import forms
from  .models import Order,Product,Transaction




class OrderForm(forms.ModelForm):
     class Meta:
          model =Order 
          fields =['orderNo','product','quantity',
                   'amountpaid', 
                   'transId']
          


class TransactForm(forms.ModelForm):
     class Meta:
          model =Transaction 
          fields =['transId','orderDetails','customerDetails',]
          

          

class ProductForm(forms.ModelForm):
     class Meta:
          model =Product 
          fields =['productId','name','stock',
                   'costPrice','selingPrice',]