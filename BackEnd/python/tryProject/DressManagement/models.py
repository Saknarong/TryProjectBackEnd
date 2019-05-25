from django.db import models

class Clothes(models.Model):
    GENDER = (
        ('m', 'Man'),
        ('w', 'Woman'),
        ('u', 'Unisex')
    )
    clotheName = models.CharField(max_length=200, blank=False)
    clothePictureUrl = models.TextField()
    categoryId = models.ForeignKey('Category',on_delete=models.CASCADE)
    clotheGender = models.CharField(max_length=6,
                            choices=GENDER,
                            default='Unisex')

class Category(models.Model):
    categoryName = models.CharField(max_length=100, blank=False)

class Pattern(models.Model):
    patternName = models.CharField(max_length=200)

class ClothesColor(models.Model):
    clothesColorCode = models.CharField(max_length=8)
