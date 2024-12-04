from django.db import models
from django.urls import reverse


# Create your models here.
# class WorkTable(models.Model):
#     name = models.CharField(max_length=255)
#     description = models.TextField()
#     salary = models.FloatField()
#   user -?
#   forum -?
#   contacts = models


#  class Forum
class Feedback(models.Model):
    email = models.EmailField(blank=True)


    




# elasticsearch