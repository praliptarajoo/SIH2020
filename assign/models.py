from django.db import models
from django.db import connections

# Create your models here.
class assignwork(models.Model):
    cemail = models.CharField(max_length=200)
    adate = models.DateField(max_length=20)
    alat = models.CharField(max_length=20)
    alon = models.CharField(max_length=20)
    anear = models.CharField(max_length=50)
    aurl = models.CharField(max_length=255)
    alod = models.IntegerField(max_length=5)
    aoption = models.IntegerField(max_length=5)
    astatus = models.IntegerField(max_length=5)
    class Meta:
        db_table="assignment"
