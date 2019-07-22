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
    fbId = models.CharField(max_length=300)
    userName = models.CharField(max_length=300)
    userProfile = models.TextField()
    userBodyPictureUrl = models.TextField(blank=True)
    userGender = models.CharField(max_length=10)
    shapeId = models.ForeignKey('Shape',on_delete=models.CASCADE)
    skinColorId = models.ForeignKey('SkinColor',on_delete=models.CASCADE)

    # def __init__(self, fbId, userName, userProfile, userBodyPictureUrl,userGender, shapeId, skinColorId):
    #     self.fbId = fbId
    #     self.userName = userName
    #     self.userProfile = userProfile
    #     self.userBodyPictureUrl = userBodyPictureUrl
    #     self.userGender = userGender
    #     self.shapeId = shapeId
    #     self.skinColorId = skinColorId



