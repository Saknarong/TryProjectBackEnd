from django.db import models
#from ModuleUserInforemation.models import Shape
# from ModuleUserInformation.models import Shape

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

class Event(models.Model):
    event = models.TextField()

class Place(models.Model):
    place = models.TextField()    

class ClothesForShape(models.Model):
    shape = models.ForeignKey('ModuleUserInformation.Shape',on_delete=models.CASCADE)
    clothes = models.ForeignKey('Clothes',on_delete=models.CASCADE)

class ClothesForEvent(models.Model):
    event = models.ForeignKey('Event',on_delete=models.CASCADE)
    clothes = models.ForeignKey('Clothes',on_delete=models.CASCADE)

class ClothesForPlace(models.Model):
    place = models.ForeignKey('Place',on_delete=models.CASCADE)
    clothes = models.ForeignKey('Clothes',on_delete=models.CASCADE)