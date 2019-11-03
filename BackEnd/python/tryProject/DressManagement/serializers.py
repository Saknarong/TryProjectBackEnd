from rest_framework import serializers
from DressManagement.models import Clothes, Category, Pattern, ClothesColor, Event, Place



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

