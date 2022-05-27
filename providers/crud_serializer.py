
from rest_framework import serializers
 

#---------------------Provider
# POST
class N_PostProviderSerializer(serializers.Serializer):  
    name            = serializers.CharField(required=True)
    email           = serializers.CharField(required=True) 
    phone_number    = serializers.CharField(required=True) 
    language        = serializers.CharField(required=True) 
    currency        = serializers.CharField(required=True) 

# PUT
class N_PutProviderSerializer(serializers.Serializer):  
    provider_id     = serializers.IntegerField(required=True)
    email           = serializers.CharField(required=True) 
    phone_number    = serializers.CharField(required=True) 
    language        = serializers.CharField(required=True) 
    currency        = serializers.CharField(required=True) 
   
# DELETE
class N_DeleteProviderSerializer(serializers.Serializer):  
    provider_id     = serializers.IntegerField(required=True)
    


#---------------------Service
# POST
class N_PostServiceSerializer(serializers.Serializer):  
    provider_id     = serializers.IntegerField(required=True)
    name            = serializers.CharField(required=True) 
    price           = serializers.IntegerField(required=True) 
    geojson         = serializers.JSONField(required=True) 
    information     = serializers.CharField(required=True) 

# PUT
class N_PutServiceSerializer(serializers.Serializer):  
    service_id     = serializers.IntegerField(required=True)
    name            = serializers.CharField(required=True) 
    price           = serializers.IntegerField(required=True) 
    geojson         = serializers.JSONField(required=True) 
    information     = serializers.CharField(required=True) 

# DELETE
class N_DeleteServiceSerializer(serializers.Serializer):  
    service_id     = serializers.IntegerField(required=True)


     