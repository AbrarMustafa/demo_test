from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.response import Response
from rest_framework.views import APIView

class SAFE_METHOD_Permission(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        return request.user and request.user.is_authenticated 


class POST_METHOD_Permission(BasePermission):        

    def has_permission(self, request, view):
        if request.method in ["POST"]:
            return True
        return request.user and request.user.is_authenticated 