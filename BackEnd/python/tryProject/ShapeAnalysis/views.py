from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from rest_framework.parsers import JSONParser
from ModuleUserInformation.models import Shape

# @csrf_exempt
# def analyzeSkinColor(request):
#     if request.method == 'POST':
#         data = JSONParser().parse(request)

@csrf_exempt
def analyzeShape(request):
    if request.method == 'POST':
        
        resultOfDif = None
        shapeId = None
        data = JSONParser().parse(request)
        personShoulder = data["shoulder"]
        personChest = data["chest"]
        personWaist = data["waist"]
        personHip = data["hip"]
        personLeg = data["leg"]

        shapesData = Shape.objects.all()
        for shapeData in shapesData:
                modelShoulder = shapeData.shapeShoulder
                modelChest = shapeData.shapeChest
                modelWaist = shapeData.shapeWaist
                modelHip = shapeData.shapeHip
                modelLeg = shapeData.shapeLeg
                
                rateOfDif = modelShoulder/personShoulder
                
                resizePersonShoulder = personShoulder*rateOfDif
                resizePersonChest = personChest*rateOfDif
                resizePersonWaist = personWaist*rateOfDif
                resizePersonHip = personHip*rateOfDif
                resizePersonLeg = personLeg*rateOfDif

                difOfShoulder = abs(resizePersonShoulder-modelShoulder)
                difOfChest = abs(resizePersonChest-modelChest)
                difOfWaist = abs(resizePersonWaist-modelWaist)
                difOfHip = abs(resizePersonHip-modelHip)
                difOfLeg = abs(resizePersonLeg-modelLeg)

                sumOfDif = difOfShoulder+difOfChest+difOfWaist+difOfHip+difOfLeg

                if resultOfDif is None:
                        resultOfDif = sumOfDif
                        shapeId = shapeData.id
                else:
                        if resultOfDif > sumOfDif:
                                resultOfDif = sumOfDif
                                shapeId = shapeData.id

        return JsonResponse(shapeId, safe=False)
        


