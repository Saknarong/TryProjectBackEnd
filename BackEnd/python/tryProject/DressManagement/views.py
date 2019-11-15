from django.http import HttpResponse, JsonResponse
import json
from django.views.decorators.csrf import csrf_exempt
from DressManagement.models import Clothes, Category, ClothesColor, Pattern, ClothesForShape, ClothesForEvent, ClothesForPlace, Place, Event, FavoriteClothes
from rest_framework.parsers import JSONParser
from ModuleUserInformation.models import Shape, BrandOwner
from DressManagement.serializers import ClothesSerializer, CategorySerializer, PatternSerializer, ClothesColorSerializer, PlaceSerializer, EventSerializer, FavoriteClothesSerializer, ClothesForShapeSerializer, ClothesForPlaceSerializer, ClothesForEventSerializer


@csrf_exempt
def updateClotheName(request):
    if request.method == 'GET':
        data = JSONParser().parse(request)
        clothe = Clothes.objects.filter(id=data['id']).update(clotheName=data['clotheName'])
        allClothes = Clothes.objects.all()
        serializer = ClothesSerializer(allClothes,many = True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def addClothe(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        clothe = {

        }

        brandOwner = BrandOwner.objects.filter(brandGoogleId=data['clotheBrand_id'])

        clothe["clotheName"] = data["clotheName"]
        clothe["clothePictureUrl"] = data["clothePictureUrl"]
        clothe["clotheGender"] = data["clotheGender"]
        clothe["categoryId"] = data["categoryId_id"]
        clothe["clotheDrescription"] = data["clotheDrescription"]
        clothe["clotheLinkToBuy"] = data["clotheLinkToBuy"]
        clothe["clotheBrand"] = brandOwner[0].id

        serializer = ClothesSerializer(data=clothe)
        if serializer.is_valid():
            serializer.save()
            
            for event in data['event']:
                clotheForEvent = ClothesForEvent()
                clotheForEvent.clothes_id = serializer.data['id']
                clotheForEvent.event_id = event
                clotheForEvent.save()

            for place in data['place']:
                clotheForPlace = ClothesForPlace()
                clotheForPlace.clothes_id = serializer.data['id']
                clotheForPlace.place_id = place
                clotheForPlace.save()

            for shape in data['shape']:
                clotheForShape = ClothesForShape()
                clotheForShape.clothes_id = serializer.data['id']
                clotheForShape.shape_id = shape
                clotheForShape.save()

            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def editClothe(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        clothe = {

        }

        clothe["clotheName"] = data["clotheName"]
        clothe["clothePictureUrl"] = data["clothePictureUrl"]
        clothe["clotheGender"] = data["clotheGender"]
        clothe["categoryId"] = data["categoryId_id"]
        clothe["clotheDrescription"] = data["clotheDrescription"]
        clothe["clotheLinkToBuy"] = data["clotheLinkToBuy"]

        clotheForUpDate = Clothes.objects.filter(id=data['id'])
        clotheForUpDate.update(clotheName=clothe["clotheName"])
        clotheForUpDate.update(clothePictureUrl=clothe["clothePictureUrl"])
        clotheForUpDate.update(clotheGender=clothe["clotheGender"])
        clotheForUpDate.update(categoryId=clothe["categoryId"])
        clotheForUpDate.update(clotheDrescription=clothe["clotheDrescription"])
        clotheForUpDate.update(clotheLinkToBuy=clothe["clotheLinkToBuy"])

        clotheForEvent = ClothesForEvent.objects.filter(clothes=data['id']).delete()
        clotheForPlace = ClothesForPlace.objects.filter(clothes=data['id']).delete()
        clotheForShape = ClothesForShape.objects.filter(clothes=data['id']).delete()
        
        for event in data['event']:
            clotheForEvent = ClothesForEvent()
            clotheForEvent.clothes_id = data['id']
            clotheForEvent.event_id = event
            clotheForEvent.save()

        for place in data['place']:
            clotheForPlace = ClothesForPlace()
            clotheForPlace.clothes_id = data['id']
            clotheForPlace.place_id = place
            clotheForPlace.save()

        for shape in data['shape']:
            clotheForShape = ClothesForShape()
            clotheForShape.clothes_id = data['id']
            clotheForShape.shape_id = shape
            clotheForShape.save()

        serializer = ClothesSerializer(clotheForUpDate, many=True)
        
        return JsonResponse(serializer.data, status=201, safe=False)


@csrf_exempt
def clothesManagement(request):
    if request.method == 'GET':
        data = 'JSONParser().parse(request)'
        # print(data)
        # allClothes = Clothes.objects.all()
        # serializer = ClothesSerializer(allClothes,many = True)
        return JsonResponse(data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClothesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

    elif request.method == 'DELETE':
        data = JSONParser().parse(request)
        clothe = Clothes.objects.filter(id=data['id'])
        clothe.delete()
        allClothes = Clothes.objects.all()
        serializer = ClothesSerializer(allClothes,many = True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def categoryManagement(request):
    if request.method == 'GET':
        allCategories = Category.objects.all()
        serializer = CategorySerializer(allCategories,many = True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = CategorySerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)


@csrf_exempt
def patternManagement(request):
    if request.method == 'GET':
        allPattern = Pattern.objects.all()
        serializer = PatternSerializer(allPattern,many = True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = PatternSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def clothesColorManagement(request):
    if request.method == 'GET':
        allClothesColor = ClothesColor.objects.all()
        serializer = ClothesColorSerializer(allClothesColor,many = True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClothesColorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

@csrf_exempt
def getClothesByCategory(request):

    if request.method == 'POST':

        data = JSONParser().parse(request)

        print(data["categoryId"])
        print(data["shapeId"])
        print(data["eventId"])
        print(data["placeId"])
        print(data["gender"])
            
        clothes = Clothes.objects.raw("SELECT c.id, c.clotheName, c.clothePictureUrl, c.clotheGender, c.categoryId_id, cs.shape_id, ce.event_id, cp.place_id "+
                                      "FROM DressManagement_clothes as c "+
                                      "JOIN DressManagement_clothesforshape as cs ON c.id = cs.clothes_id "+
                                      "JOIN DressManagement_clothesforevent as ce ON c.id = ce.clothes_id "+
                                      "JOIN DressManagement_clothesforplace as cp ON c.id = cp.clothes_id "+
                                      "WHERE c.categoryId_id like %s "+
                                      "AND cs.shape_id like %s "+
                                      "AND ce.event_id like %s "+
                                      "AND cp.place_id like %s "+
                                      "AND (c.clotheGender like %s OR c.clotheGender like 'u') "+
                                      "GROUP BY 1", [data["categoryId"], data["shapeId"], data["eventId"], data["placeId"], data["gender"]])

        serializer = ClothesSerializer(clothes,many = True)
            
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def getAllPlace(request):
    if request.method == 'GET':
        allPlace = Place.objects.all()
        serializer = PlaceSerializer(allPlace,many = True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def getAllEvent(request):
    if request.method == 'GET':
        allEvent = Event.objects.all()
        serializer = EventSerializer(allEvent,many = True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def getClothesByBrandAndCategory(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        allClothes = Clothes.objects.filter(clotheBrand=data['clotheBrand']).filter(categoryId=data['categoryId'])
        serializer = ClothesSerializer(allClothes,many = True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def deleteClothe(request):
    if request.method == 'POST':
        data = JSONParser().parse(request) 

        clotheForEvent = ClothesForEvent.objects.filter(clothes=data['id']).delete()
        clotheForPlace = ClothesForPlace.objects.filter(clothes=data['id']).delete()
        clotheForShape = ClothesForShape.objects.filter(clothes=data['id']).delete()
        FavoriteClothes.objects.filter(clothe=data['id']).filter(user=data['userId']).delete()

        clothe = Clothes.objects.filter(id=data['id'])
        clothe.delete()
        allClothes = Clothes.objects.all()
        serializer = ClothesSerializer(allClothes,many = True)
        return JsonResponse(serializer.data, safe=False)


@csrf_exempt
def getFavoriteByUserId(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        result = [

        ]

        allFavorite = FavoriteClothes.objects.filter(user=data['id'])

        for favorite in allFavorite:
            json = {

            }
            clothe = Clothes.objects.filter(id=favorite.clothe.id)    
            json['categoryId'] = clothe[0].categoryId.id
            json['clotheBrand'] = clothe[0].clotheBrand.id
            json['clotheDrescription'] = clothe[0].clotheDrescription
            json['clotheGender'] = clothe[0].clotheGender
            json['clotheLinkToBuy'] = clothe[0].clotheLinkToBuy
            json['clotheName'] = clothe[0].clotheName
            json['clothePictureUrl'] = clothe[0].clothePictureUrl
            json['id'] = clothe[0].id
            json['brandName'] = BrandOwner.objects.filter(id=clothe[0].clotheBrand.id)[0].brandName   
            result.append(json)

        return JsonResponse(result, safe=False)

@csrf_exempt
def addFavorite(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        if FavoriteClothes.objects.filter(user=data['user']).filter(clothe=data['clothe']).exists():
            favorite = FavoriteClothes.objects.filter(user=data['user']).filter(clothe=data['clothe'])
            serializer = FavoriteClothesSerializer(favorite, many = True)
            return JsonResponse(serializer.data, safe=False)
        else:
            serializer = FavoriteClothesSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse(serializer.data, status=201)

@csrf_exempt
def deleteFavorite(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        FavoriteClothes.objects.filter(user=data['userId']).filter(clothe=data['clotheId']).delete()
        allFavorite = FavoriteClothes.objects.all()
        serializer = FavoriteClothesSerializer(allFavorite,many = True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def getClotheById(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        clothe = Clothes.objects.filter(id=data['id'])
        serializer = ClothesSerializer(clothe, many = True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def getEventById(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = []
        allEvent = ClothesForEvent.objects.filter(clothes=data['id'])
        for event in allEvent:
            json = {}
            eventObj = Event.objects.filter(id=event.event.id)
            json['id'] = eventObj[0].id
            json['event'] = eventObj[0].event
            json['clothes'] = event.clothes.id
            result.append(json)
        return JsonResponse(result, safe=False)

@csrf_exempt
def getPlaceById(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = []
        allPlaces = ClothesForPlace.objects.filter(clothes=data['id'])
        for place in allPlaces:
            json = {}
            placeObj = Place.objects.filter(id=place.place.id)
            json['id'] = placeObj[0].id
            json['place'] = placeObj[0].place
            json['clothes'] = place.clothes.id
            result.append(json)
        return JsonResponse(result, safe=False)

@csrf_exempt
def getShapeById(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        result = []
        allShapes = ClothesForShape.objects.filter(clothes=data['id'])
        for shape in allShapes:
            json = {}
            shapeObj = Shape.objects.filter(id=shape.shape.id)
            json['id'] = shapeObj[0].id
            json['shape'] = shapeObj[0].shapeName
            json['clothes'] = shape.clothes.id
            result.append(json)
        return JsonResponse(result, safe=False)



# @csrf_exempt
# def getBrand(request):
#     if request.method == 'POST':
#         brand = Brand.objects.filter(id=data['id'])
#         serializer = BrandSerializer(brand,many = True)
#         return JsonResponse(serializer.data, safe=False)
