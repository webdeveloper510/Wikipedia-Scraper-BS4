from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class Type(models.Model):
    type_name = models.CharField(max_length=255, blank=True)


class Industry(models.Model):
    industry_name = models.TextField(max_length=255, null=True)


class Information(models.Model):
    name = models.CharField(max_length=255, blank=True)
    type_key = models.ForeignKey(Type , on_delete=models.CASCADE , null=True)
    industry_key = models.ForeignKey(Industry ,  on_delete=models.CASCADE ,null=True)
    image = models.TextField()
    

class Info_Meta(models.Model):
    meta_key = models.TextField(max_length=255 )
    meta_value = models.TextField(null=True)
    info_key = models.ForeignKey(Information, on_delete=models.CASCADE ,null=True)