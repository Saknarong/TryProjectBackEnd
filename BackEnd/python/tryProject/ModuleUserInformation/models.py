from django.db import models


class Shape(models.Model):
    GENDER = (
        ('m', 'Man'),
        ('w', 'Woman')
    )
    shapeName = models.CharField(max_length=200, blank=False)
    shapeGender = models.CharField(max_length=6,
                                   choices=GENDER,
                                   blank=False)
    shapePictureUrl = models.TextField()

class SkinColor(models.Model):
    skinColorCode = models.CharField(max_length=8, blank=False)

class User(models.Model):
    userFirstName = models.CharField(max_length=300)
    userLastName = models.CharField(max_length=300)
    userEmail = models.TextField()
    userPictureUrl = models.TextField()
    shapeId = models.ForeignKey('Shape',on_delete=models.CASCADE)
    skinColorId = models.ForeignKey('SkinColor',on_delete=models.CASCADE)
