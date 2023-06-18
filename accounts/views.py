from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import UserAccount
from .serializers import *
# Create your views here.
#View Set
#Api View

class ViewProfileApiView(APIView):
    def get(self, request):
        instance = UserAccount.objects.filter(pk=request.user.id)
        serializer = UserProfileSerializer(instance=instance)
        return Response(serializer.data)