from rest_framework import serializers
from ModuleUserInformation.models import User, Shape, SkinColor, BrandOwner



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('__all__')

class ShapeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Shape
        fields = ('__all__')

class SkinColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = SkinColor
        fields = ('__all__')

class BrandOwnerSerializer(serializers.ModelSerializer):
    class Meta:
        model = BrandOwner
        fields = ('__all__')
