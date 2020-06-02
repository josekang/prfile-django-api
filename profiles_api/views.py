from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

from profiles_api import serializers

# Create your views here.

class HelloAPIView(APIView):
    """ Return features of an API """
    serializer_class = serializers.HelloSerializer
    
    def get(self, request, formart=None):
        """ Shows the methods used """
        api_views = [
            "Similar to traditional django mehods",
            "Methods are GET, POST, PUT, PATCH, DELETE"
        ]
        
        response = {
            "status": status.HTTP_200_OK,
            "message": "Shows the output as a dictionary, power of API",
            "data": api_views
        }
        
        return Response(response)
    
    def post(self, request, format=None):
        serializer = self.serializer_class(data=request.data)
        
        if serializer.is_valid():
            name = serializer.validated_data.get('name')
            message = f"hello {name}"
            
            response = {
                "status": status.HTTP_200_OK,
                "message": message
            }
            
            return Response(response)
        
        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST,
            
        )
        
    def put(self, request, pk=None):
        response = {
            "status": status.HTTP_200_OK,
            "message": "Updated successfully"
        }
        
        return Response(response)
    
    def patch(self, request, pk=None):
        response = {
            "status": status.HTTP_200_OK,
            "message": "Patched successfully"
        }
        
        return Response(response)
    
    def delete(self, request, pk=None):
        response = {
            "status": status.HTTP_200_OK,
            "message": "Deleted successfully"
        }
        
        return Response(response)