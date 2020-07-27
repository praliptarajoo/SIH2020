from django.db import models
from django.db import connections
from django.utils import timezone

# Create your models here.
class Dashboard(models.Model):
    user = models.CharField(max_length=20)
    date = models.DateField(max_length=20)
    lat = models.CharField(max_length=20)
    lon = models.CharField(max_length=20)
    near = models.CharField(max_length=50)
    sug = models.CharField(max_length=50)
    url = models.CharField(max_length=225)
    lod = models.IntegerField(max_length=5)
    status = models.CharField(max_length=20)
    class Meta:
        db_table="collect"

#CATEGORIES = (  
 #   ('SORT BY', '0'),
  #  ('LOD', '1'),
   # ('DATE', '2'),
#)


