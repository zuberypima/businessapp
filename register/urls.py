from django.urls import path
from .views import product_list,createOrder,recodtrans,regproduct,order_list,trans_list,customerdash


urlpatterns = [
    path('orders/',order_list, name='orders'),
    path('transactions/',order_list, name='transactions'),
    # path('orders/',order_list, name='orders'),
    # path('createorders/',createOrder ,name='createorder'),
    path('recordtransctions/',recodtrans ,name='recordtransctions'),
    path('registerproduct/',regproduct,name='registerproduct'),
    path('customer',customerdash,name='customer'),
    path('productview',createOrder,name='productview')
]


