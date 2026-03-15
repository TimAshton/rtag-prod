# from django.shortcuts import render
from .models import Challenge
from .serializers import ChallengeModelSerializer
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import APIView


# Create your views here.
@api_view(['GET', 'PUT', 'PATCH'])
def challenge(req, id):
    data = Challenge.objects.get(id=id)
    if req.method == "PUT":
        parsed_data = req.data
        serializer = ChallengeModelSerializer(data, data=parsed_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"update": "success"})

    if req.method == "GET":
        serializer = ChallengeModelSerializer(data)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def challenges(req):
    if req.method == "POST":
        parsed_data = req.data

        serializer = ChallengeModelSerializer(data=parsed_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"created": "success"},
            status=status.HTTP_201_CREATED)

    if req.method == "GET":
        data = Challenge.objects.all()
        serializer = ChallengeModelSerializer(data, many=True)
        return Response(serializer.data)


class ChallengesAPIView(APIView):
    def get(self, req):
        data = Challenge.objects.all()
        serializer = ChallengeModelSerializer(data, many=True)
        return Response(serializer.data)

    def post(self, req):
        parsed_data = req.data

        serializer = ChallengeModelSerializer(data=parsed_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(
            {"created": "success"},
            status=status.HTTP_201_CREATED)


class ChallengeAPIView(APIView):
    def get(self, req, id):
        data = Challenge.objects.get(id=id)
        serializer = ChallengeModelSerializer(data)
        return Response(serializer.data)

    def put(self, req, id):
        data = Challenge.objects.get(id=id)
        parsed_data = req.data
        serializer = ChallengeModelSerializer(data, data=parsed_data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({"update": "success"})

    def patch(self, req):
        # data = Challenge.objects.get(id=id)
        pass
