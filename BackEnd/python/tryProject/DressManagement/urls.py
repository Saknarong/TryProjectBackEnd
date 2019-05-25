from django.urls import path
from DressManagement import views

urlpatterns = [
    path('clothesManagement/', views.clothesManagement),
    path('categoryManagement/', views.categoryManagement),
    path('clothesColorManagement/', views.clothesColorManagement),
    path('patternManagement/', views.patternManagement),
]