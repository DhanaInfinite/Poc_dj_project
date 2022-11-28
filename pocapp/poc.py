import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','Poc_dj_project.settings')

import django
django.setup()

from faker import Faker
import secrets
import string
import pandas as pd
import re
import mysql.connector
from sqlalchemy import create_engine
from cryptography.fernet import Fernet
from random import *

fake = Faker(locale='en_US')
from pocapp.models import Customer
from pocapp.models import Product
from pocapp.models import Order

def customer(n):

    for i in range(n):
        customer_id = fake.random_number(6),
        customer_name = fake.name(),
        customer_address = fake.address(),
        customer_dob = fake.date_between(start_date='-60y', end_date='-20y'),
        credit_card_number = fake.credit_card_number(),
        customer_ssn = ''.join(secrets.choice(string.digits) for i in range(9))
        customer_record=Customer.objects.get_or_create(customer_id=customer_id[0],customer_name=customer_name[0],customer_address=customer_address[0],customer_dob=customer_dob[0],credit_card_number=int(credit_card_number[0]),customer_ssn=customer_ssn)

#customer(2)

def product(n):

    list=['pen','laptop','pencil','laptop bag','monitor','generator','tablet','mobile','ipad','computer','luggage bag','earphones','pendrive','headphones']

    for i in range(n):
        product_id = fake.random_number(6),
        product_name = choice(list),
        product_price = fake.random_number(3)
        product_record=Product.objects.get_or_create(product_id=product_id[0],product_name=product_name[0],product_price=product_price)

#product(2)

con=mysql.connector.connect(user='root',password='Dhana1525',host='localhost',database='djpoc')
cursor=con.cursor()

def order(n):
    
    #print("Fetching Data from Customer table")

    list1=[]
    cursor.execute("select customer_id from pocapp_customer")
    data=cursor.fetchall()
    #print(data)
    for i in data:
        for x in i:
            list1.append(x)
    #print(list1)

    #print("Fetching Data from Customer table")

    list2=[]
    cursor.execute("select product_id from pocapp_product")
    data=cursor.fetchall()
    #print(data)
    for i in data:
        for x in i:
            list2.append(x)
    #print(list2)

    list3=[1,2,3,4,5,6,7,8,9,10]

    for i in range(n):
        order_id = fake.random_number(6),
        customer_id =choice(list1),
        product_id = choice(list2),
        quantity = choice(list3),
        order_total = (choice(list3)*fake.random_number(3))
        order_record=Order.objects.get_or_create(order_id=order_id[0],customer_id=customer_id[0],product_id=product_id[0],quantity=quantity[0],order_total=order_total)

#order(2)

print("Data generated successfully...")

engine=create_engine('mysql+mysqldb://root:Dhana1525@localhost/djpoc')

def excel():
    # To Covert from Database customer table to Excel sheet
    df1=pd.read_sql('pocapp_customer',engine,columns=['customer_id','customer_name','customer_address','customer_dob','credit_card_number','customer_ssn'])
    df1.to_excel('customer.xlsx')

    # To Covert from Database product table to Excel sheet
    df2=pd.read_sql('pocapp_product',engine,columns=['product_id','product_name','product_price'])
    df2.to_excel('product.xlsx')

    # To Covert from Database order table to Excel sheet
    df3=pd.read_sql('pocapp_order',engine,columns=['order_id','customer_id','product_id','quantity','order_total'])
    df3.to_excel('order.xlsx')

#excel()