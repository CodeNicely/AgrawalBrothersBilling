from django.shortcuts import render
from orders.models import *
from payment.models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
from django.utils import timezone
import json
import datetime

def billing(request):
	if request.method=='GET':
		firm_name=request.GET.get('firm_name')
		from_time=request.GET.get('from_time')
		to_time=request.GET.get('to_time')

		if firm_name=='':
			firm_name=None

		if from_time==None:
			from_time=datetime.date.today()
			print from_time
	

		if to_time==None:
			to_time=datetime.date.today() + datetime.timedelta(days=1)
	

			# firm_name=''
		response_data={}
		total_sell=0
		total_purchase=0

		firm_list=order_data.objects.order_by().values_list('firm_name').distinct()
		firmlist=''
		for o in firm_list:
			firmlist+='<option value="'+o[0]+'">'

		print 'FirmNameHere',firm_name
		print from_time
		print to_time

		if firm_name==None:
			orders_list=order_data.objects.filter(order_type='PURCHASE',created__range=[str(from_time),str(to_time)])
		else:
			orders_list=order_data.objects.filter(order_type='PURCHASE',firm_name=firm_name,created__range=[str(from_time),str(to_time)])

		orders_list_purchase=''
		i=1
		for o in orders_list:
			orders_list_purchase+='<tr><td>'+str(i)+'</td>'
			i+=1
			orders_list_purchase+='<td>'+o.firm_name+'</td>'
			orders_list_purchase+='<td>'+o.product_name+'</td>'
			orders_list_purchase+='<td>'+o.truck_number+'</td>'
			orders_list_purchase+='<td>'+str(o.product_quantity)+'</td>'
			orders_list_purchase+='<td>'+str(o.product_price)+'</td>'
			orders_list_purchase+='<td>'+str(o.product_total)+'</td>'
			orders_list_purchase+='<td>'+str(o.created)[:10]+'</td></tr>'
			total_purchase+=o.product_total

		if firm_name==None:
			orders_list=order_data.objects.filter(order_type='SELL',created__range=[str(from_time),str(to_time)])
		else:
			orders_list=order_data.objects.filter(order_type='SELL',firm_name=firm_name,created__range=[str(from_time),str(to_time)])

		orders_list_sell=''
		i=1
		for o in orders_list:
			orders_list_sell+='<tr><td>'+str(i)+'</td>'
			i+=1
			orders_list_sell+='<td>'+o.firm_name+'</td>'
			orders_list_sell+='<td>'+o.product_name+'</td>'
			orders_list_sell+='<td>'+o.truck_number+'</td>'
			orders_list_sell+='<td>'+str(o.product_quantity)+'</td>'
			orders_list_sell+='<td>'+str(o.product_price)+'</td>'
			orders_list_sell+='<td>'+str(o.product_total)+'</td>'
			orders_list_sell+='<td>'+str(o.created)[:10]+'</td></tr>'
			total_sell+=o.product_total
		# orders_list_sell+='</tbody>'
		# orders_list_sell+='</table>'


		response_data['orders_list_purchase']=orders_list_purchase
		response_data['orders_list_sell']=orders_list_sell
		response_data['total_purchase']=total_purchase
		response_data['total_sell']=total_sell

		total_credit=0
		total_debit=0

		if firm_name==None:
			payments_list=payment_data.objects.filter(payment_type='DEBIT',created__range=[str(from_time),str(to_time)])
		else:
			payments_list=payment_data.objects.filter(payment_type='DEBIT',firm_name=firm_name,created__range=[str(from_time),str(to_time)])

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

		if firm_name==None:
			payments_list=payment_data.objects.filter(payment_type='CREDIT',created__range=[str(from_time),str(to_time)])
		else:
			payments_list=payment_data.objects.filter(payment_type='CREDIT',firm_name=firm_name,created__range=[str(from_time),str(to_time)])

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
		
		total_sell_debit=total_sell+total_debit
		total_purchase_credit=total_purchase+total_credit

		balance=total_sell_debit - total_purchase_credit

		# payment_list_debit+='</tbody>'
		# payment_list_debit+='</table>'
		response_data['payment_list_credit']=payment_list_credit
		response_data['payment_list_debit']=payment_list_debit
		response_data['total_credit']=total_credit
		response_data['total_debit']=total_debit
		response_data['firmlist']=firmlist
		response_data['from_time']=from_time
		response_data['to_time']=to_time
		

		if firm_name==None:
			response_data['firm_name']=''
		else:
			response_data['firm_name']=firm_name

		if balance<0:
			response_data['balance_credit']=balance
		else:
			response_data['balance_debit']=balance
		# response_data['balance']=balance
		response_data['total_sell_debit']=total_sell_debit
		response_data['total_purchase_credit']=total_purchase_credit

		print response_data['firmlist']
		return render(request,"billing/billing.html",response_data)
	else:
		return JsonResponse({"success":False,"message":"I am a big hacker out here . Please get out of here"})