from django.contrib import admin
from .models import Airport, Flight, Passenger
# Register your models here.
# 这个文件中注册的表可以在……/admin的图形化界面中直接编辑

admin.site.register(Airport)
admin.site.register(Flight)
admin.site.register(Passenger)