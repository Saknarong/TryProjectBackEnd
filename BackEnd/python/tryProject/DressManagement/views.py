from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from DressManagement.models import Clothes, Category, ClothesColor, Pattern
from rest_framework.parsers import JSONParser
from DressManagement.serializers import ClothesSerializer, CategorySerializer, PatternSerializer, ClothesColorSerializer

@csrf_exempt
def clothesManagement(request):
    if request.method == 'GET':
        allClothes = Clothes.objects.all()
        serializer = ClothesSerializer(allClothes,many = True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ClothesSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)

@csrf_exempt
def categoryManagement(request):
    if request.method == 'GET':
        allCategories = Category.objects.all()
        serializer = CategorySerializer(allCategories,many = True)
        return JsonResponse(serializer.data, safe=False)
    
    elif request.method == 'POST':
        print('Test')
        data = JSONParser().parse(request)
        print(data)
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
        print('Test')
        data = JSONParser().parse(request)
        print(data)
        serializer = ClothesColorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)

