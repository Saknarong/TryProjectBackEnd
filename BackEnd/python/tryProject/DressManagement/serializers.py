from rest_framework import serializers
from DressManagement.models import Clothes, Category, Pattern, ClothesColor



class ClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Clothes
        fields = ('__all__')

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('__all__')

class PatternSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pattern
        fields = ('__all__')

class ClothesColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesColor
        fields = ('__all__')

