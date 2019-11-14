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
    path('getClothesByBrandAndCategory/', views.getClothesByBrandAndCategory),
    path('addClothe/', views.addClothe),
    path('editClothe/', views.editClothe),
    path('deleteClothe/', views.deleteClothe),
    path('getFavoriteByUserId/', views.getFavoriteByUserId),
    path('addFavorite/', views.addFavorite),
    path('deleteFavorite/', views.deleteFavorite),
    path('getClotheById/', views.getClotheById),
    path('getShapeById/', views.getShapeById),
    path('getEventById/', views.getEventById),
    path('getPlaceById/', views.getPlaceById),

    
]