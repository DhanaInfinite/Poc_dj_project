from faker import Faker
import secrets
import string
import pandas as pd
import re
import mysql.connector
from sqlalchemy import create_engine
from random import *
import farmhash
from sqlalchemy import Integer, String,BigInteger,DateTime
#from sqlalchemy.dialects.mysql import VARCHAR
from properties import *
import base64

#Masking Data
def mygen2():
    con=mysql.connector.connect(user=username,password=password,host=hostname,database=proddbname)
    cursor=con.cursor()

    #cursor.execute('''create table if not exists pocapp_dev_customer(customer_id int NOT NULL primary key,customer_name varchar(150),
                #customer_address varchar(256),customer_dob varchar(50),credit_card_number BIGINT ,customer_ssn BIGINT)''')

    cursor.execute('''create table if not exists pocapp_dev_customer(customer_id int NOT NULL primary key,customer_name varchar(150),
                customer_address varchar(256),customer_dob varchar(50),credit_card_number varchar(256) ,customer_ssn varchar(256))''')


    #engine=create_engine('mysql+mysqldb://root:Dhana1525@localhost/djpoc')
    engine=create_engine('mysql+mysqldb://'+username+':'+password+'@'+hostname+'/'+proddbname)

    con.commit()
    
    df1=pd.read_sql('pocapp_customer',engine,columns=['customer_id','customer_name','customer_address','customer_dob','credit_card_number','customer_ssn'])

    
    #df1.customer_ssn = df1.customer_ssn.apply(lambda x: re.sub(r'\d', '*', x, count=5))
    #df1.credit_card_number = df1.credit_card_number.apply(lambda x: re.sub(r'\d', '*', x, count=10))
    
    #df1.credit_card_number = df1.credit_card_number.apply(lambda x: farmhash.hash64(str(x)))
    #df1.customer_ssn = df1.customer_ssn.apply(lambda x: farmhash.hash64(str(x)))
    #df1.credit_card_number = df1.credit_card_number.apply(lambda x: base64.b64encode(str(x).encode("ascii")).decode("ascii"))
    #df1.customer_ssn = df1.customer_ssn.apply(lambda x: base64.b64encode(str(x).encode("ascii")).decode("ascii"))
    
    for i in L:
        #df1[i]= df1[i].apply(lambda x: farmhash.hash64(str(x)))
        df1[i]= df1[i].apply(lambda x: base64.b64encode(str(x).encode("ascii")).decode("ascii"))

    #print(df1)

    df1.to_excel('dev_customer.xlsx')
    df1.to_sql('pocapp_dev_customer',engine,if_exists='replace',index=False,dtype={'credit_card_number':String(200),'customer_ssn':String(200)})
    
    # Clone to djpoc_dev database

    con2=mysql.connector.connect(user=username,password=password,host=hostname,database=devdbname)
    cursor2=con2.cursor()

    #cursor2.execute('''create table if not exists pocapp_dev_customer(customer_id int NOT NULL primary key,customer_name varchar(150),
                #customer_address varchar(256),customer_dob varchar(50),credit_card_number BIGINT ,customer_ssn BIGINT)''')
    cursor2.execute('''create table if not exists pocapp_dev_customer(customer_id int NOT NULL primary key,customer_name varchar(150),
                customer_address varchar(256),customer_dob varchar(50),credit_card_number varchar(256) ,customer_ssn varchar(256))''')


    #engine2=create_engine('mysql+mysqldb://root:Dhana1525@localhost/djpoc_dev')
    engine2=create_engine('mysql+mysqldb://'+username+':'+password+'@'+hostname+'/'+devdbname)
    
    con.commit()
    df1.to_sql('pocapp_dev_customer',engine2,if_exists='replace',index=False,dtype={'credit_card_number':String(200),'customer_ssn':String(200)})

#mygen2()

#UnMasking Data

def mygen3():
    con=mysql.connector.connect(user=username,password=password,host=hostname,database=proddbname)
    cursor=con.cursor()

    cursor.execute('''create table if not exists pocapp_dev_unmask_customer(customer_id int NOT NULL primary key,customer_name varchar(150),
                customer_address varchar(256),customer_dob varchar(50),credit_card_number BIGINT ,customer_ssn BIGINT)''')

    #engine=create_engine('mysql+mysqldb://root:Dhana1525@localhost/djpoc')
   
    engine=create_engine('mysql+mysqldb://'+username+':'+password+'@'+hostname+'/'+devdbname)
    engine2=create_engine('mysql+mysqldb://'+username+':'+password+'@'+hostname+'/'+proddbname)

    con.commit()
    
    df1=pd.read_sql('pocapp_dev_customer',engine,columns=['customer_id','customer_name','customer_address','customer_dob','credit_card_number','customer_ssn'])

    
    for i in L:
        df1[i]= df1[i].apply(lambda x: base64.b64decode(str(x).encode("ascii")).decode("ascii"))

    #print(df1)

    df1.to_sql('pocapp_dev_unmask_customer',engine2,if_exists='replace',index=False)
    
#mygen3()
