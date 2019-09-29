from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from ModuleUserInformation.models import User, Shape, SkinColor
from rest_framework.parsers import JSONParser
from ModuleUserInformation.serializers import UserSerializer, ShapeSerializer, SkinColorSerializer
from rest_framework.renderers import JSONRenderer


#สร้าง user
@csrf_exempt
def createUser(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
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
def menShape(request):
    if request.method == 'GET':
        menShape = Shape.objects.filter(shapeGender='m')
        serializer = ShapeSerializer(menShape, many=True)
        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def womanShape(request):
    if request.method == 'GET':
        womanShape = Shape.objects.filter(shapeGender='w')
        serializer = ShapeSerializer(womanShape, many=True)
        return JsonResponse(serializer.data, safe=False)
        

@csrf_exempt
def checkUserIsExist(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        fbId = data["fbId"]
        result = {
        }

        if  User.objects.filter(fbId=fbId).exists():
            result["result"] = True
        else:
            result["result"] = False
        return JsonResponse(result, safe=False)

@csrf_exempt
def getUser(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)

        fbId = data["fbId"]
        print(fbId)

        user = User.objects.filter(fbId=fbId)
        serializer = UserSerializer(user, many = True)

        return JsonResponse(serializer.data, safe=False)

@csrf_exempt
def getShapeName(request):
    if request.method == 'POST':

        data = JSONParser().parse(request)
        result = {
        }

        shapeId = data["shapeId"]

        shape = Shape.objects.filter(id=shapeId).get()

        result["result"] = shape.shapeName

        return JsonResponse(result, safe=False)


@csrf_exempt
def updateUserBodyPictureUrl(request):
    if request.method == 'POST':
        data = JSONParser().parse(request)
        print(data)
        user = User.objects.filter(fbId=data['fbId']).update(userBodyPictureUrl=data['url'])
        serializer = UserSerializer(user, many = True)
        return JsonResponse(serializer.data, safe=False)