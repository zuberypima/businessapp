from django.shortcuts import render
from .models import Product,Order
from .forms import OrderForm,TransactForm,ProductForm
# Create your views here.

def product_list(request):
    products =Product.objects.all()
    return render(request,'productslist.html',{'products':products})


def trans_list(request):
    orders =Order.objects.all()
    return render(request,'orderlist.html',{'orders':orders})


def order_list(request):
    orders =Order.objects.all()
    return render(request,'orderlist.html',{'orders':orders})

def myorders(request):
    orders =Order.objects.all()
    return render(request,'customerorders.html',{'orders':orders})

def customerdash(request):
    products =Product.objects.all()
    return render(request,'customerdash.html',{'products':products})


def accountsdash(request):
    products =Product.objects.all()
    return render(request,'accountsdash.html',{'products':products})

def servicedash(request):
    products =Product.objects.all()
    return render(request,'customerdash.html',{'products':products})


def productview(request,pk):
    product =Product.objects.get(productId=pk)
    return render(request,'productview.html', {'product':product} )

def createOrder(request):
    if request.method =='POST':
       form =OrderForm(request.POST)
       if form.is_valid():
           form.save()
           #return redirect('success_page')
           print('Succsessfully')
    else:
        form=OrderForm()
    return render(request,'productview.html', {'form': form} )



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


