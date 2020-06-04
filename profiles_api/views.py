from django.shortcuts import render
from rest_framework import status, viewsets, filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.settings import api_settings

from profiles_api import serializers
from profiles_api.models import UserProfile
from profiles_api import permissions


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

class HelloViewSet(viewsets.ModelViewSet):
    
    serializer_class = serializers.HelloSerializer
    
    def list(self, request):
        a_viewset = [
            "This is a vieset",
            "Provides more functionality with less code"
        ]
        
        response = {
            "status":status.HTTP_200_OK,
            "mesage": "A list of all viewset",
            "data": a_viewset
        }
        return Response(response)
    
    def create(self, request, format=None):
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
        
    def retrieve(self, request, pk=None):
        return Response({"Method": "RETRIEVE"})
    
    def update(self, request, pk=None):
        return Response({"Method": "PUT"})
    
    def partial_updates(self, request, pk=None):
        return Response({"Method": "PATCH"})
    
    def destroy(self, request, pk=None):
        return Response({"Method": "delete"})
    
class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = serializers.UserProfileSerializer
    authentication_classes = (TokenAuthentication,)
    permission_classes = (permissions.UpdateOwnPermission)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name', 'email',)
      
class UserLoginViewSet(ObtainAuthToken):
        renderer_classes = api_settings.DEFAULT_RENDERER_CLASSES