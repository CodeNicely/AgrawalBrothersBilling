from django.contrib import admin
from .models import *

# Register your models here.
class payment_dataAdmin(admin.ModelAdmin):
	list_display=["id","firm_name","amount","payment_type","modified","created"]
admin.site.register(payment_data,payment_dataAdmin)