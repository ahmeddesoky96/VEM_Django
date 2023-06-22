from django.shortcuts import render

# Create your views here.
#####authentication imports#######
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
## @authentication_classes([JWTAuthentication]) ||| @permission_classes([IsAuthenticated])
##################################


