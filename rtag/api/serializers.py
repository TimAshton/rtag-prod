from rest_framework import serializers
from .models import Challenge


class ChallengeSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=60)
    description = serializers.CharField(max_length=160)
    created_date = serializers.DateTimeField()
    status = serializers.BooleanField()

    def create(self, validated_data):
        return Challenge.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.created_date = validated_data.get("created_date", instance.created_date)
        instance.status = validated_data.get("status", instance.status)
        # Do all fields
        instance.save()
        return instance


class RtagSerializer(serializers.Serializer):
    owner_id = serializers.CharField(max_length=60)
    title = serializers.CharField(max_length=60)
    challenge_id = serializers.CharField(max_length=60)
    longitude = serializers.CharField(max_length=60)
    latitude = serializers.CharField(max_length=60)
    elevation = serializers.CharField(max_length=60)
