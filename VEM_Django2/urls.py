
from django.contrib import admin
from django.urls import path, include, re_path
from django.views.generic import TemplateView
from django.contrib.auth import authenticate, login
from accounts.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include('djoser.urls')),
    path('account/', include('djoser.urls.jwt')),
    path('account/', include('djoser.social.urls')),
    # path('profile/', ViewProfileApiView.as_view(),name="profile"),
]

urlpatterns += [re_path(r'^.*', TemplateView.as_view(template_name='index.html'))]
