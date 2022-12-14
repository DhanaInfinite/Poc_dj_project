from django.db import models

# Create your models here.
class Customer(models.Model):
    customer_id=models.BigIntegerField(primary_key=True, editable=True)
    customer_name=models.CharField(max_length=156)
    customer_address=models.CharField(max_length=256)
    customer_dob=models.DateField()
    credit_card_number=models.BigIntegerField()
    customer_ssn=models.BigIntegerField()

class Product(models.Model):
    product_id=models.BigIntegerField(primary_key=True, editable=True)
    product_name=models.CharField(max_length=256)
    product_price=models.FloatField()

class Order(models.Model):
    order_id=models.BigIntegerField(primary_key=True, editable=True)
    customer=models.ForeignKey(Customer, on_delete=models.CASCADE)
    product=models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity=models.IntegerField()
    order_total=models.FloatField()

class Dev_Customer(models.Model):
    customer_id=models.BigIntegerField(primary_key=True, editable=True)
    customer_name=models.CharField(max_length=156)
    customer_address=models.CharField(max_length=256)
    customer_dob=models.DateField()
    #credit_card_number=models.BigIntegerField()
    #customer_ssn=models.BigIntegerField()
    credit_card_number=models.CharField(max_length=256)
    customer_ssn=models.CharField(max_length=256)

class Dev_Unmask_Customer(models.Model):
    customer_id=models.BigIntegerField(primary_key=True, editable=True)
    customer_name=models.CharField(max_length=156)
    customer_address=models.CharField(max_length=256)
    customer_dob=models.DateField()
    credit_card_number=models.BigIntegerField()
    customer_ssn=models.BigIntegerField()
   