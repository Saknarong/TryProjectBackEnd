from django.urls import path
from DressManagement import views

urlpatterns = [
    path('clothesManagement/', views.clothesManagement),
    path('categoryManagement/', views.categoryManagement),
    path('clothesColorManagement/', views.clothesColorManagement),
    path('patternManagement/', views.patternManagement),
    path('updateClotheName/', views.updateClotheName),
    path('getClothesByCategory/', views.getClothesByCategory),
    path('getAllPlace/', views.getAllPlace),
    path('getAllEvent/', views.getAllEvent),
]