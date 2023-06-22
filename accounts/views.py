from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserAccount
from .serializers import *

####activation email #####

############################

#####authentication imports#######
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
##################################


# Create your views here.
#View Set
#Api View
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
class ViewProfileApiView(APIView):
    def get(self, request):
        instance = UserAccount.objects.filter(pk=request.user.id)
        serializer = UserProfileSerializer(instance=instance)
        return Response(serializer.data)
    



