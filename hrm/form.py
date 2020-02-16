from django import forms

from .models import bulbstatus,sensor_reading
class bulbstatus_form(forms.ModelForm):
    class Meta():
        model = bulbstatus
        exclude = ['on', 'off']

class sensor_reading_form(forms.ModelForm):
    class Meta():
        model = sensor_reading
        exclude = ['temp_reading', 'humidity_reading']
