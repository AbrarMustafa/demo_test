from distutils.fancy_getopt import FancyGetopt
from django.contrib.auth.models import BaseUserManager
from django.contrib.gis.db import models

# applevel. 
from utils.consts import *

class DateTimeMixin(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
    class Meta:
        abstract = True

class ProviderModel(DateTimeMixin):
    name                = models.CharField(max_length=100)
    email               = models.EmailField(max_length=100)
    phone_number        = models.CharField(max_length=15 )
    language            = models.CharField(max_length=15, choices=LANGUAGE_OPTIONS, default=ENGLISH)
    currency            = models.CharField(max_length=6, choices=CURRENCY_OPTIONS, default=USD)

class ServiceModel(DateTimeMixin):
    provider            = models.ForeignKey(ProviderModel,      null=False, blank=False,      on_delete=models.CASCADE, related_name='service_provider' )
    name                = models.CharField(max_length=100)
    price               = models.IntegerField()
    geojson             = models.PolygonField(geography=True)   
    information         = models.CharField(max_length=500)