from django.contrib import admin
from django.urls import path, include
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Welcome to MeetLoveXme</h1>')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home),
    path('', include('ads.urls')),
]
