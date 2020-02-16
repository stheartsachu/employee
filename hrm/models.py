from django.db import models


class Users(models.Model):
    employee_id = models.AutoField(primary_key=True)
    employee_name = models.CharField(max_length=255,default="",blank=True)
    employee_age = models.IntegerField()
    employee_ranking = models.FloatField()
    # def image(self,filename):
    #     path = "./images/%s"% filename
    #     return path
    # employee_photo = models.ImageField(upload_to=image, blank=True
    #                                    )
    def __str__(self):
        return (str(self.employee_name)+str('-')+str(self.employee_id))

class bulbstatus(models.Model):
    trigger_id = models.AutoField(primary_key=True)
    on = models.CharField(max_length=255, default="", blank=True)
    off = models.CharField(max_length=255, default="", blank=True)
    def __str__(self):
        return (str(self.trigger_id)+str("on")+str("-")+str(self.on)+str("off")+str("-")+str(self.off))

class sensor_reading(models.Model):
    reading_id = models.AutoField(primary_key=True)
    # sensor_name = models.CharField(max_length=255, default="", blank=True)
    temp_reading = models.CharField(max_length=255, default="", blank=True)
    humidity_reading = models.CharField(max_length=255, default="", blank=True)
    def __str__(self):
        return (str("reading-id")+str(self.reading_id))