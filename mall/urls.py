from django.urls import path
from mall.views import *

urlpatterns = [
    #paths for api
    path("rated", get_top_rated , name='get_top_rated'),
    
]