from django.shortcuts import render
from django.shortcuts import render
from django.http import HttpResponse ,HttpResponseRedirect
from .models import *
from rest_framework.response import Response
from  rest_framework.decorators import  api_view
from .serializers import *
from rest_framework.status import *
from django.shortcuts import  get_object_or_404,get_list_or_404
# Create your views here.
#####authentication imports#######
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.permissions import IsAuthenticated
## @authentication_classes([JWTAuthentication]) ||| @permission_classes([IsAuthenticated])
##################################



@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def get_top_rated(req):
    # top_rated_shops = Shop.objects.order_by('-total_rate')[:5]
    top_rated_shops = get_list_or_404(Shop.objects.order_by('-total_rate')[:5])


    if(top_rated_shops):
            shop_json = Shopserializer(top_rated_shops,many=True)
            return Response(status = HTTP_202_ACCEPTED, data={'Shop': shop_json.data})
    #else return status code 404 not found
    else:
        return  Response(status=HTTP_404_NOT_FOUND)
