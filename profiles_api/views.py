from django.shortcuts import render
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response

# Create your views here.

class HelloAPIView(APIView):
    """ Return features of an API """
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
