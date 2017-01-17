from django.shortcuts import render
from .models import *
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
import requests
from django.utils import timezone
import json

@csrf_exempt
def orders(request):
	if request.method=='GET':
		response_data={}
		total_sell=0
		total_purchase=0

		orders_list=order_data.objects.filter(order_type='PURCHASE')
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

		orders_list=order_data.objects.filter(order_type='SELL')
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
		return render(request,"orders/orders.html",response_data)
	else:
		return JsonResponse({"success":False,"message":"I am a big hacker out here . Please get out of here"})


def register(request):
	with open('student_list.json') as data_file:
		data = json.load(data_file)
		# print data
	for o in data:
		print 'First Name',o['firstname']
		response = requests.post('http://mpenavmo.com:8080/register810/', data=o)
		content = response.content
		print content

	return JsonResponse({})