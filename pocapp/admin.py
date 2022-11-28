from django.contrib import admin
from pocapp.models import Customer
from pocapp.models import Product
from pocapp.models import Order
from pocapp.models import Dev_Customer
# Register your models here.
class CustomerAdmin(admin.ModelAdmin):
    list_display= ['customer_id','customer_name','customer_address','customer_dob','credit_card_number','customer_ssn']

class ProductAdmin(admin.ModelAdmin):
    list_display= ['product_id','product_name','product_price']

class OrderAdmin(admin.ModelAdmin):
    list_display= ['order_id','customer_id','product_id','quantity','order_total']

#class Dev_CustomerAdmin(admin.ModelAdmin):
    #list_display= ['customer_id','customer_name','customer_address','customer_dob','credit_card_number','customer_ssn']


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
#admin.site.register(Dev_Customer,Dev_CustomerAdmin)
