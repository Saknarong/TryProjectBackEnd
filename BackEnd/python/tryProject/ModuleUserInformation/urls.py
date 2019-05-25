from django.urls import path
from ModuleUserInformation import views

urlpatterns = [
    path('skinColorManagement/', views.skinColorManagement),
    path('shapeManagement/', views.shapeManagement),
    path('userManagement/', views.userManagement),
    path('guest/', views.createGuest),
]