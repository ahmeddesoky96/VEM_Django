from django.urls import path
from accounts.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", get_user, name='get_user_info'),
    # path('', ProfileListCreateView.as_view(), name='profile-list-create'),
    # path('<int:pk>', ProfileRetrieveUpdateDestroyView.as_view(), name='profile-retrieve-update-destroy'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
