from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserAccount
from .serializers import *
from  rest_framework.decorators import  api_view

####activation email #####

############################

#####authentication imports#######
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
##################################

from rest_framework import generics



# Create your views here.
#View Set
#Api View
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# class ViewProfileApiView(APIView):
#     def get(self, request):
#         instance = UserAccount.objects.filter(pk=request.user.id)
#         serializer = UserProfileSerializer(instance=instance)
#         return Response(serializer.data)
    
# class ProfileListCreateView(generics.ListCreateAPIView):
#     queryset = UserAccount.objects.all()
#     serializer_class = UserProfileSerializer   


class ProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    queryset = UserAccount.objects.all()
    serializer_class = UserProfileSerializer

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request):
    instance = UserAccount.objects.get(pk=request.user.id)

    serializer = UserProfileSerializer(instance)
    return Response(serializer.data)


