from rest_framework import serializers
from DressManagement.models import Clothes, Category, Pattern, ClothesColor, Event, Place, FavoriteClothes, ClothesForShape, ClothesForEvent, ClothesForPlace



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


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = ('__all__')

class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = ('__all__')

class  FavoriteClothesSerializer(serializers.ModelSerializer):
    class Meta:
        model = FavoriteClothes
        fields = ('__all__')

class  ClothesForShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesForShape
        fields = ('__all__')

class  ClothesForPlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesForPlace
        fields = ('__all__')

class  ClothesForEventSerializer(serializers.ModelSerializer):
    class Meta:
        model = ClothesForEvent
        fields = ('__all__')




       

