# django 
from django.urls import *
from django.contrib import * 

# app level 
from .views import *   


class ProviderUrl():
    def getUrls():
        urlpatterns = [ 
            path('providers/', ProviderView.as_view()),  
            path('service_area/', ServiceView.as_view()),  
            path('specific_to_polygon/', SpecificToPolygon.as_view()),  
        ]
        return urlpatterns