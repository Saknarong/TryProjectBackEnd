from django.contrib import admin
from django.urls import path,include
from django.conf.urls import include, url

urlpatterns = [
    #path('', include('userManagement.urls')),
    url(r'^', include('userManagement.urls'))
]
