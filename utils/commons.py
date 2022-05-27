from django.contrib.gis.geos import Point
from django.conf import settings

errorLog =lambda _errorlog: "  "+_errorlog+" " if settings.DEBUG else "" 

def distBetweenPoints( pointOne, pointTwo): 
    distance = pointOne.distance(pointTwo)
    distance_in_km = distance * 100
    return distance_in_km