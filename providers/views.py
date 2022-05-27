 
import json
import random
import datetime 

from django.apps import apps
from django.db.models import Q
from django.contrib.gis.geos import GEOSGeometry
from django.core import * 
from django.shortcuts import *
from rest_framework.views import * 
from django.contrib.gis.geos import *
from rest_framework.response import * 
from rest_framework.permissions import *   
from django.contrib.auth.hashers import *  
from rest_framework.authentication import * 
from rest_framework.authtoken.models import *  

# Create your views here. 
from utils.consts import * 
from utils.commons import * 
from utils.permission import *  
from .models import *   
from .serializers import * 
from .crud_serializer import * 



class ProviderView(APIView):

    def get(self, request):
        data, isSuccess , msg =None, False, "error while performing operation" 
        try: 
            _provider = ProviderModel.objects.all() 

            _providerresponce = ProviderSerializer(_provider, many=True) 
            data=_providerresponce.data
            msg=SUCCESS
            isSuccess=True 

        except Exception as expt:
            msg=str(msg) + errorLog(str(expt)) 
            data=None
            isSuccess=False

        return Response({DATA: data, MSG: msg, ISSUCCESS: isSuccess})
  

    def post(self, request):
        data, isSuccess , msg =None, False, "error while performing operation" 
        try:   
            ser = N_PostProviderSerializer(data=request.data)
            if not ser.is_valid(): 
                msg=ser.errors
                raise Exception('My error!')

            _provider = ProviderModel()
            _provider.name=ser.validated_data["name"] 
            _provider.email = ser.validated_data["email"]   
            _provider.phone_number = ser.validated_data["phone_number"]   
            _provider.language = ser.validated_data["language"]   
            _provider.currency = ser.validated_data["currency"]   
            _provider.save()


            msg=SUCCESS
            isSuccess=True  

        except Exception as expt:
            msg=str(msg) + errorLog(str(expt)) 
            isSuccess=False
        return Response({DATA: data, MSG: msg, ISSUCCESS: isSuccess})
      
    def put(self, request):
        data, isSuccess , msg =None, False, "error while performing operation" 
        try:   
            ser = N_PutProviderSerializer(data=request.data)
            if not ser.is_valid(): 
                msg=ser.errors
                raise Exception('My error!')
        
            _provider = ProviderModel.objects.get(id=ser.validated_data["provider_id"]) 
            _provider.email = ser.validated_data["email"]   
            _provider.phone_number = ser.validated_data["phone_number"]   
            _provider.language = ser.validated_data["language"]   
            _provider.currency = ser.validated_data["currency"]   
            _provider.save()

            msg=SUCCESS
            isSuccess=True  

        except Exception as expt:
            msg=str(msg) + errorLog(str(expt)) 
            isSuccess=False
        return Response({DATA: data, MSG: msg, ISSUCCESS: isSuccess})
       
      
    def delete(self, request):
        data, isSuccess , msg =None, False, "error while performing operation" 
        try:    
            ser = N_DeleteProviderSerializer(data=request.data)
            if not ser.is_valid(): 
                msg=ser.errors
                raise Exception('My error!')
                 
            _provider = ProviderModel.objects.get(id=ser.validated_data["provider_id"])
            _provider.delete()  
            msg=SUCCESS
            isSuccess=True    
         
        except Exception as expt:
            msg=str(msg) + errorLog(str(expt)) 
            isSuccess=False
        return Response({DATA: data, MSG: msg, ISSUCCESS: isSuccess})
 

class SpecificToPolygon(APIView):

    def get(self, request):
        data, isSuccess , msg =None, False, "error while performing operation" 
        try: 
            #  
            if "lat" not in request.GET or "lng" not in request.GET:
                msg="lat and lng required in get params" 
                raise Exception('My error!')  
            
            lat_lng="Point("+str(request.GET.get('lat'))+" "+str(request.GET.get('lng'))+")"
            p = GEOSGeometry( lat_lng, srid=4326) # 4326 for standard lng/lat coordinates

            # Transform to same coordinate system as maps
            p.transform(27700)

            _service= ServiceModel.objects.filter(geojson__intersects=p)
            _serviceresponce = ServiceSerializer(_service, many=True) 
            data=_serviceresponce.data
            
            msg=SUCCESS
            isSuccess=True 

        except Exception as expt:
            msg=str(msg) + errorLog(str(expt)) 
            data=None
            isSuccess=False

        return Response({DATA: data, MSG: msg, ISSUCCESS: isSuccess})
   


class ServiceView(APIView):

    def get(self, request):
        data, isSuccess , msg =None, False, "error while performing operation" 
        try: 
            _service = ServiceModel.objects.all() 

            _serviceresponce = ServiceSerializer(_service, many=True) 
            data=_serviceresponce.data
            msg=SUCCESS
            isSuccess=True 

        except Exception as expt:
            msg=str(msg) + errorLog(str(expt)) 
            data=None
            isSuccess=False

        return Response({DATA: data, MSG: msg, ISSUCCESS: isSuccess})
  

    def post(self, request):
        data, isSuccess , msg =None, False, "error while performing operation" 
        try:   
            ser = N_PostServiceSerializer(data=request.data)
            if not ser.is_valid(): 
                msg=ser.errors
                raise Exception('My error!')

            _provider = ProviderModel.objects.get(id=ser.validated_data["provider_id"]) 

            _service = ServiceModel(name=ser.validated_data["name"]) 
            _service.provider = _provider  
            _service.price = ser.validated_data["price"]   
            _service.geojson = GEOSGeometry(str(ser.validated_data["geojson"])) 
            _service.information = ser.validated_data["information"]   
            _service.save()


            msg=SUCCESS
            isSuccess=True  

        except Exception as expt:
            msg=str(msg) + errorLog(str(expt)) 
            isSuccess=False
        return Response({DATA: data, MSG: msg, ISSUCCESS: isSuccess})
      
    def put(self, request):
        data, isSuccess , msg =None, False, "error while performing operation" 
        try:   
            ser = N_PutServiceSerializer(data=request.data)
            if not ser.is_valid(): 
                msg=ser.errors
                raise Exception('My error!')
        
            _service = ServiceModel.objects.get(id=ser.validated_data["service_id"]) 
            _service.price = ser.validated_data["price"]      
            _service.geojson = GEOSGeometry(str(ser.validated_data["geojson"])) 
            _service.information = ser.validated_data["information"]   
            _service.save()

            msg=SUCCESS
            isSuccess=True  

        except Exception as expt:
            msg=str(msg) + errorLog(str(expt)) 
            isSuccess=False
        return Response({DATA: data, MSG: msg, ISSUCCESS: isSuccess})
       
      
    def delete(self, request):
        data, isSuccess , msg =None, False, "error while performing operation" 
        try:    
            ser = N_DeleteServiceSerializer(data=request.data)
            if not ser.is_valid(): 
                msg=ser.errors
                raise Exception('My error!') 
            _service = ServiceModel.objects.get(id=ser.validated_data["service_id"])
            _service.delete()  
            msg=SUCCESS
            isSuccess=True    
         
        except Exception as expt:
            msg=str(msg) + errorLog(str(expt)) 
            isSuccess=False
        return Response({DATA: data, MSG: msg, ISSUCCESS: isSuccess})
 
        