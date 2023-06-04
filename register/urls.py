import statistics
from django.urls import path
from django.conf.urls.static import static
from core import settings
from .views import product_list,createOrder,recodtrans,regproduct,order_list,trans_list,customerdash,myorders,productview, accountsdash


urlpatterns = [
    path('orders/',order_list, name='orders'),
    path('allproducts/',product_list, name='allproducts'),
    path('transactions/',order_list, name='transactions'),
    path('orders/',order_list, name='orders'),
    path('createorders/',createOrder ,name='createorder'),
    path('recordtransctions/',recodtrans ,name='recordtransctions'),
    path('registerproduct/',regproduct,name='registerproduct'),
    path('customer',customerdash,name='customer'),
    path('productview/<str:pk>/',productview,name='productview'),
    path('myorders',myorders,name='myorders'),
    path('accounts',accountsdash,name='accounts')
] 
# + statistics(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
