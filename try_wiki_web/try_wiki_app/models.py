from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Type(models.Model):
    type_name = models.CharField(max_length=255, blank=True)


class Industry(models.Model):
    industry_name = models.TextField( null=True)


class Information(models.Model):
    name = models.CharField(max_length=255, blank=True)
    type_key = models.ForeignKey(Type , on_delete=models.CASCADE , null=True)
    industry_key = models.ForeignKey(Industry ,  on_delete=models.CASCADE ,null=True)
    image = models.TextField()
    

class Info_Meta(models.Model):
    keyh2 = models.TextField( )
    valueh2 = models.TextField(null=True)
    key_h3 = models.TextField()
    key_h4 = models.TextField()
    info_key = models.ForeignKey(Information, on_delete=models.CASCADE ,null=True)


class Main_Info(models.Model):
    keyh3 = models.TextField( null=True)
    valueh3 = models.TimeField()
    keyh4 = models.TextField( null=True)
    valueh4 = models.TimeField()
    Main_key = models.ForeignKey(Info_Meta, on_delete=models.CASCADE ,null=True)
