from django.contrib import admin
from hrm.models import Users,bulbstatus,sensor_reading

# Register your models here.
admin.site.register(Users)
admin.site.register(bulbstatus)
admin.site.register(sensor_reading)
