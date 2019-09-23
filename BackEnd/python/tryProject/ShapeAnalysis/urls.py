from django.urls import path
from ShapeAnalysis import views

urlpatterns = [
    path('analyzeShape/', views.analyzeShape),
]