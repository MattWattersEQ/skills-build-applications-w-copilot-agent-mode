from rest_framework.decorators import api_view
from rest_framework.response import Response
from pymongo import MongoClient
from .serializers import UserSerializer, TeamSerializer, ActivitySerializer, WorkoutSerializer, LeaderboardSerializer

client = MongoClient('localhost', 27017)
db = client['octofit_db']

@api_view(['GET'])
def api_root(request, format=None):
    return Response({
        'users': '/users/',
        'teams': '/teams/',
        'activities': '/activities/',
        'workouts': '/workouts/',
        'leaderboard': '/leaderboard/',
    })

@api_view(['GET'])
def users_list(request):
    users = list(db.users.find({}, {'_id': 0}))
    return Response(UserSerializer(users, many=True).data)

@api_view(['GET'])
def teams_list(request):
    teams = list(db.teams.find({}, {'_id': 0}))
    return Response(TeamSerializer(teams, many=True).data)

@api_view(['GET'])
def activities_list(request):
    activities = list(db.activities.find({}, {'_id': 0}))
    return Response(ActivitySerializer(activities, many=True).data)

@api_view(['GET'])
def workouts_list(request):
    workouts = list(db.workouts.find({}, {'_id': 0}))
    return Response(WorkoutSerializer(workouts, many=True).data)

@api_view(['GET'])
def leaderboard_list(request):
    leaderboard = list(db.leaderboard.find({}, {'_id': 0}))
    return Response(LeaderboardSerializer(leaderboard, many=True).data)
