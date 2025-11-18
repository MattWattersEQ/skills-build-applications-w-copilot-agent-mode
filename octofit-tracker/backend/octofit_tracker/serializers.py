from rest_framework import serializers

# Serializers for MongoDB collections (no Django ORM models)
class UserSerializer(serializers.Serializer):
    name = serializers.CharField()
    email = serializers.EmailField()
    team = serializers.CharField()

class TeamSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

class ActivitySerializer(serializers.Serializer):
    user = serializers.CharField()
    activity = serializers.CharField()
    duration_min = serializers.IntegerField()

class WorkoutSerializer(serializers.Serializer):
    name = serializers.CharField()
    description = serializers.CharField()

class LeaderboardSerializer(serializers.Serializer):
    user = serializers.CharField()
    points = serializers.IntegerField()
