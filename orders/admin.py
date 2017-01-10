from django.contrib import admin
from .models import *

# Register your models here.
class order_dataAdmin(admin.ModelAdmin):
	list_display=["id","product_name","firm_name","broker","product_quantity","product_price","product_total","truck_number","order_type","remark","modified","created"]
admin.site.register(order_data,order_dataAdmin)