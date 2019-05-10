from django.urls import path
from DressManagement import views

urlpatterns = [
    path('showAllClothes/', views.showAllClothes),
    path('showAllCategory/', views.showAllCategory)
]