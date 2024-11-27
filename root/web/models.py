from django.db import models

# Create your models here.
class WorkTable(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    salary = models.FloatField()
#   user -?
#   forum -?
#   contacts = models


#  class Forum

# elasticsearch