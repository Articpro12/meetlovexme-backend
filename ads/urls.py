from django.urls import path
from .views import AdListAPIView

urlpatterns = [
    path('api/ads/', AdListAPIView.as_view(), name='ad-list'),
]
