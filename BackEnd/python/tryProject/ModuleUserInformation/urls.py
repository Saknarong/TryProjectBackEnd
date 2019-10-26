from django.urls import path
from ModuleUserInformation import views

urlpatterns = [
    path('skinColorManagement/', views.skinColorManagement),
    path('shapeManagement/', views.shapeManagement),
    path('menShape/', views.menShape),
    path('womanShape/', views.womanShape),
    path('createUser/', views.createUser),
    path('checkUserIsExist/', views.checkUserIsExist),
    path('getUser/', views.getUser),
    path('getShapeName/', views.getShapeName),
    path('updateUserBodyPictureUrl/', views.updateUserBodyPictureUrl),
    path('createBrand/', views.createBrand),
    path('checkAdminIsExist/', views.checkAdminIsExist),
]