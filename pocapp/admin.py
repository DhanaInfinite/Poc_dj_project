from django.contrib import admin
from pocapp.models import Customer
from pocapp.models import Product
from pocapp.models import Order
from pocapp.models import Dev_Customer
from import_export.admin import ImportExportModelAdmin
from import_export import resources

# Register your models here.

class CapabilityResource(resources.ModelResource):
    class Meta:
        model = Customer
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('customer_id','customer_name','customer_address','customer_dob','credit_card_number','customer_ssn',)


class CapabilityResource2(resources.ModelResource):
    class Meta:
        model = Product
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('product_id','product_name','product_price',)


class CapabilityResource3(resources.ModelResource):
    class Meta:
        model = Order
        skip_unchanged = True
        report_skipped = True
        exclude = ('id',)
        import_id_fields = ('order_id','customer_id','product_id','quantity','order_total',)


class CustomerAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CapabilityResource
    list_display= ['customer_id','customer_name','customer_address','customer_dob','credit_card_number','customer_ssn']



class ProductAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CapabilityResource2
    list_display= ['product_id','product_name','product_price']


class OrderAdmin(ImportExportModelAdmin,admin.ModelAdmin):
    resource_class = CapabilityResource3
    list_display= ['order_id','customer_id','product_id','quantity','order_total']

#class Dev_CustomerAdmin(admin.ModelAdmin):
    #list_display= ['customer_id','customer_name','customer_address','customer_dob','credit_card_number','customer_ssn']


admin.site.register(Customer,CustomerAdmin)
admin.site.register(Product,ProductAdmin)
admin.site.register(Order,OrderAdmin)
#admin.site.register(Dev_Customer,Dev_CustomerAdmin)
