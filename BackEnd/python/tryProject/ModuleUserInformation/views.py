from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ModuleUserInformation.models import User, Shape, SkinColor
from rest_framework.parsers import JSONParser
from ModuleUserInformation.serializers import UserSerializer, ShapeSerializer, SkinColorSerializer


@csrf_exempt
def userManagement(request):
    if request.method == 'GET':
        allUser = User.objects.all()
        serializer = UserSerializer(allUser, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)
        return JsonResponse(serializer.errors, status=400)


@csrf_exempt
def shapeManagement(request):
    if request.method == 'GET':
        allShape = Shape.objects.all()
        serializer = ShapeSerializer(allShape, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ShapeSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)


@csrf_exempt
def skinColorManagement(request):
    if request.method == 'GET':
        allSkinColor = SkinColor.objects.all()
        serializer = SkinColorSerializer(allSkinColor, many=True)
        return JsonResponse(serializer.data, safe=False)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = SkinColorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse(serializer.data, status=201)


@csrf_exempt
def createGuest(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        guestShape = Shape.objects.get(id=data['userShapeId'])
        guestSkinColor = SkinColor.objects.get(id=data['userSkinColorId'])
        guest = User(data['userFirstName'], data['userLastName'], data['userEmail'],
                     data['userPictureUrl'], guestShape.id, guestSkinColor.id)
        user = json.dump(guest)
        serializer = UserSerializer(data=user)
        if serializer.is_valid():
            return JsonResponse(serializer.data, status=201)
        
