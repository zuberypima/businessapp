from django.shortcuts import render
from .models import Product,Order
from .forms import OrderForm,TransactForm,ProductForm
# Create your views here.

def product_list(request):
    orders =Order.objects.all()
    return render(request,'orderlist.html',{'orders':orders})


def trans_list(request):
    orders =Order.objects.all()
    return render(request,'orderlist.html',{'orders':orders})


def order_list(request):
    orders =Order.objects.all()
    return render(request,'orderlist.html',{'orders':orders})

def createOrder(request):
    if request.method =='POST':
       form =OrderForm(request.POST)
       if form.is_valid():
           form.save()
           #return redirect('success_page')
           print('Succsessfully')
    else:
        form=OrderForm()
    return render(request,'create_order.html', {'form': form} )



def recodtrans(request):
    if request.method =='POST':
       form =TransactForm(request.POST)
       if form.is_valid():
           form.save()
           #return redirect('success_page')
           print('Succsessfully')
    else:
        form=TransactForm()
    return render(request,'rec_transctions.html', {'form': form} )


def regproduct(request):
    if request.method =='POST':
       form =ProductForm(request.POST)
       if form.is_valid():
           form.save()
           #return redirect('success_page')
           print('Succsessfully')
    else:
        form=ProductForm()
    return render(request,'registerproduct.html', {'form': form} )
