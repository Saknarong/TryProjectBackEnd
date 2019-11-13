from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from DressManagement.models import Clothes, Category, ClothesColor, Pattern, ClothesForShape, ClothesForEvent, ClothesForPlace, Place, Event
from rest_framework.parsers import JSONParser
from DressManagement.serializers import ClothesSerializer, CategorySerializer, PatternSerializer, ClothesColorSerializer, PlaceSerializer, EventSerializer


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

        clothe["clotheName"] = data["clotheName"]
        clothe["clothePictureUrl"] = data["clothePictureUrl"]
        clothe["clotheGender"] = data["clotheGender"]
        clothe["categoryId"] = data["categoryId_id"]
        clothe["clotheDrescription"] = data["clotheDrescription"]
        clothe["clotheLinkToBuy"] = data["clotheLinkToBuy"]
        clothe["clotheBrand"] = data["clotheBrand_id"]

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
        serializer = ClothesColorSerializemr(data=data)
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

        clothe = Clothes.objects.filter(id=data['id'])
        clothe.delete()
        allClothes = Clothes.objects.all()
        serializer = ClothesSerializer(allClothes,many = True)
        return JsonResponse(serializer.data, safe=False)



# @csrf_exempt
# def getBrand(request):
#     if request.method == 'POST':
#         brand = Brand.objects.filter(id=data['id'])
#         serializer = BrandSerializer(brand,many = True)
#         return JsonResponse(serializer.data, safe=False)
