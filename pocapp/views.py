from django.shortcuts import render
from pocapp import poc
from pocapp import poc2
from pocapp.models import Dev_Customer, Dev_Unmask_Customer
from pocapp.models import Customer, Product, Order
from pocapp.serializers import CustomerSerializer, ProductSerializer, OrderSerializer
from rest_framework.viewsets import ModelViewSet

# Create your views here.
def home(request):
    return render(request,'pocapp/home.html')

def generate(request):
    poc.customer(2)
    poc.product(2)
    poc.order(2)
    poc.excel()
    return render(request,'pocapp/sample.html')

def clone(request):
    poc2.mygen2()
    return render(request,'pocapp/sample2.html')

def dev_customer(request): 
    cust_list=Dev_Customer.objects.all()
    my_dict={'cust_list':cust_list}
    return render(request,'pocapp/dev_customers.html',context=my_dict)

def unmask(request):
    poc2.mygen3()
    return render(request,'pocapp/sample3.html')

def dev_unmask_customer(request): 
    cust_list=Dev_Unmask_Customer.objects.all()
    my_dict={'cust_list':cust_list}
    return render(request,'pocapp/dev_unmask_customers.html',context=my_dict)

class CustomerCRUDCBV(ModelViewSet):
    serializer_class=CustomerSerializer
    queryset=Customer.objects.all()

class ProductCRUDCBV(ModelViewSet):
    serializer_class=ProductSerializer
    queryset=Product.objects.all()

class OrderCRUDCBV(ModelViewSet):
    serializer_class=OrderSerializer
    queryset=Order.objects.all()
