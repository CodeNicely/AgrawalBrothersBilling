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
    ('Radhe Rahe Traders , Varud',"Radhe Rahe Traders , Varud")

    )
PAYMENT_CHOICES=(
	('DEBIT',"DEBIT"),
	('CREDIT',"CREDIT"),
	)
PAYMENT_MEDIUM=(
	('CASH',"CASH"),
	('CHEQUE',"CHEQUE"),
	)


class payment_data(models.Model):
	firm_name=models.CharField(choices=FIRM_CHOICES,max_length=255,blank=True,null=True)
	amount=models.IntegerField(default=0)
	payment_type=models.CharField(choices=PAYMENT_CHOICES,max_length=100,blank=True,null=True)
	payment_medium=models.CharField(choices=PAYMENT_MEDIUM,max_length=100,blank=True,null=True)
	remarks=models.CharField(max_length=512,blank=True,null=True)
	modified= models.DateTimeField(auto_now=True,auto_now_add=False)
	created= models.DateTimeField(auto_now=False,auto_now_add=True)
	