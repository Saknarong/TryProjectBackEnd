from django.urls import path
from ModuleUserInformation import views

urlpatterns = [
    path('skinColorManagement/', views.skinColorManagement),
    path('shapeManagement/', views.shapeManagement),
    path('menShape/', views.menShape),
    path('womanShape/', views.womanShape),
    path('createUser/', views.createUser),
    path('checkUserIsExist/', views.checkUserIsExist),
]