from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserAccount
from .serializers import *
from  rest_framework.decorators import  api_view
from rest_framework import status
from mall.models import *

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

# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# class ProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
#       def get(self, request):   
#         queryset = UserAccount.objects.get(pk=request.user.id)
#         serializer_class = UserProfileSerializer
#         return Response(serializer_class.data)



class ProfileRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = UserAccount.objects.all()
    serializer_class = UserProfileSerializer

    def get_object(self):
        return self.queryset.get(pk=self.request.user.id)


@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_user(request):
    instance = UserAccount.objects.get(pk=request.user.id)
    print(instance)
    serializer = UserProfileSerializer(instance)
    return Response(serializer.data)


def get_shop(request):
    instance = Shop.objects.get(pk=request.user.id)
    serializer = UserProfileSerializer(instance)
    return Response(serializer.data)



# @api_view(['PUT'])
# @authentication_classes([JWTAuthentication])
# @permission_classes([IsAuthenticated])
# def update_user(request):
#     user = UserAccount.objects.get(pk=request.user.id)
#     serializer = UserUpdateSerializer(user, data=request.data,partial=True)
#     if serializer.is_valid():
#         print("true ")
#         serializer.save()
#         return Response(serializer.data)
#     else:
#         print(user) 
#         return Response(serializer.errors, status=status.HTTP_404_NOT_FOUND)