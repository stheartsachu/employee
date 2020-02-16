from rest_framework import serializers
from hrm.models import Users,bulbstatus,sensor_reading

class Userserializer(serializers.ModelSerializer):
    class Meta():
        model = Users
        fields = '__all__' #('employee_id','employee_name')
class bulbserializer(serializers.ModelSerializer):
    class Meta():
        model = bulbstatus
        fields = '__all__'
class readingserializer(serializers.ModelSerializer):
    class Meta():
        model = sensor_reading
        fields = '__all__'
