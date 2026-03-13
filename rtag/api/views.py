# from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from .models import Challenge
import io
from rest_framework.parsers import JSONParser
from .serializers import ChallengeSerializer
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
from rest_framework import status


# Create your views here.
@csrf_exempt
def challenge(req, id):
    data = Challenge.objects.get(id=id)
    if req.method == "PUT":
        stream = io.BytesIO(req.body)
        parsed_data = JSONParser().parse(stream)
        serializer = ChallengeSerializer(data, data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"update": "success"})
        
        return JsonResponse(serializer.errors, status.HTTP_400_BAD_REQUEST)

    serializer = ChallengeSerializer(data)
    return JsonResponse(serializer.data)

@csrf_exempt
def challenges(req):
    if req.method == "POST":
        json = req.body
        stream = io.BytesIO(json)
        parsed_data = JSONParser().parse(stream)
        
        serializer = ChallengeSerializer(data=parsed_data)
        if serializer.is_valid():
            serializer.save()
            return JsonResponse({"created": "success"}, status=status.HTTP_201_CREATED)
        return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
    data = Challenge.objects.all()
    serializer = ChallengeSerializer(data, many=True)
    return JsonResponse(serializer.data, safe=False)
