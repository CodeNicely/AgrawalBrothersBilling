#!/usr/local/bin/python
# -*- coding: utf-8 -*- 
from __future__ import unicode_literals
from django.db import models
# Create your models here.

FIRM_CHOICES = (
    ('Guru Teg Bahadur Rice Mill , Mahasamund','Guru Teg Bahadur Rice Mill , Mahasamund'),
    ('Pankaj Agrawal , Sinapali','Pankaj Agrawal , Sinapali'),
    ('Sunil Kumar Agrawal , Sohela',"Sunil Kumar Agrawal , Sohela"),
    ('Rajendra Pali , Durg',"Rajendra Pali , Durg"),
    ('Radhe Rahe Traders , Varud',"Radhe Rahe Traders , Varud"),
    ('Kissan Rice Mill , Arang',"Kissan Rice Mill , Arang"),
    ('Jay Shankar Rice Mill , Raipur',"Jay Shankar Rice Mill , Raipur"),
    ('Jindal Rice Mill , Bagbara',"Jindal Rice Mill , Bagbara"),
    ('Vishva Bharti Rice Mill , Raipur',"Vishva Bharti Rice Mill , Raipur"),
    ('Konark Industries , Raipur',"Konark Industries , Raipur"),
    ('Ratiram Tarachand , Raipur',"Ratiram Tarachand , Raipur"),
    ('Balaji Rice Mill , Kharora',"Balaji Rice Mill , Kharora"),
    ('Anil Rice Mill , Bilaspur',"Anil Rice Mill , Bilaspur"),
    ('Vijay and Company , Rajim',"Vijay and Company , Rajim"),
    ('Durga Trading , Raipur',"Durga Trading , Raipur"),
    ('Sonia Cattlefeed , Raipur',"Sonia Cattlefeed , Raipur"),
    ('Shri Nath Agro , Durg',"Shri Nath Agro , Durg"),
    ('Mahendra Dalal , Raipur',"Mahendra Dalal , Raipur"),
    ('Santosh Kumar Dewangan , Rajnandgaon',"Santosh Kumar Dewangan , Rajnandgaon"),










    )

PRODUCT_CHOICES = (
    ('Bhusa', "Bhusa"),
    ('Bhusi', "Bhusi"),
    ('Filter Kodha', "Filter Kodha"),
    ('Non Filter Kodha',"Non Filter Kodha"),
    ('Combo Filter Kodha',"Combo Filter Kodha"),
    ('Rafi', "Rafi"),
    ('Kanki', "Kanki"),
    ('Hallar Konda', "Hallar Konda"),
    ('Badra', "Badra"),
    )
ORDER_TYPE=(
    ('PURCHASE', "PURCHASE"),
    ('SELL', "SELL"),
    )

class order_data(models.Model):
	product_name=models.CharField(choices=PRODUCT_CHOICES,max_length=20,blank=True,null=True)
	firm_name=models.CharField(choices=FIRM_CHOICES,max_length=255,blank=True,null=True)
	broker=models.CharField(max_length=255,blank=True,null=True,default='No Broker')
	bags=models.IntegerField(default=0)
	product_quantity=models.DecimalField(max_digits=20,decimal_places=2,default=0)
	product_price=models.DecimalField(max_digits=20,decimal_places=2,default=0)
	truck_number=models.CharField(max_length=32,blank=True,null=True)
	order_type=models.CharField(choices=ORDER_TYPE,max_length=10,blank=True,null=True)
	remark=models.CharField(max_length=255,blank=True,null=True,default='No Remark')
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	product_total=models.DecimalField(max_digits=20,decimal_places=2,default=0)

	def save(self, *args, **kwargs):
		self.product_total=(self.product_quantity)*(self.product_price)
		super(order_data,self).save(*args, **kwargs)

