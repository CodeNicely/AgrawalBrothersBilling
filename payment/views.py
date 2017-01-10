from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
from django.utils import timezone
import json

# Create your views here.
@csrf_exempt
def payment(request):
	if request.method=='GET':
		response_data={}
		total_credit=0
		total_debit=0

		payments_list=payment_data.objects.filter(payment_type='DEBIT')
		payment_list_debit=''
		i=1
		for o in payments_list:
			payment_list_debit+='<tr><td>'+str(i)+'</td>'
			i+=1
			payment_list_debit+='<td>'+o.firm_name+'</td>'
			payment_list_debit+='<td>'+str(o.amount)+'</td>'
			payment_list_debit+='<td>'+str(o.created)[:10]+'</td>'
			payment_list_debit+='<td>'+str(o.payment_medium)+'</td>'
			payment_list_debit+='<td>'+str(o.remarks)+'</td></tr>'
			total_debit+=o.amount

		payments_list=payment_data.objects.filter(payment_type='CREDIT')
		payment_list_credit=''
		i=1
		for o in payments_list:
			payment_list_credit+='<tr><td>'+str(i)+'</td>'
			i+=1
			payment_list_credit+='<td>'+o.firm_name+'</td>'
			payment_list_credit+='<td>'+str(o.amount)+'</td>'
			payment_list_credit+='<td>'+str(o.created)[:10]+'</td>'
			payment_list_credit+='<td>'+str(o.payment_medium)+'</td>'
			payment_list_credit+='<td>'+str(o.remarks)+'</td></tr>'
			total_credit+=o.amount
		# payment_list_debit+='</tbody>'
		# payment_list_debit+='</table>'


		response_data['payment_list_credit']=payment_list_credit
		response_data['payment_list_debit']=payment_list_debit
		response_data['total_credit']=total_credit
		response_data['total_debit']=total_debit
		return render(request,"payment/payment.html",response_data)
	else:
		return JsonResponse({"success":False,"message":"I am a big hacker out here . Please get out of here"})