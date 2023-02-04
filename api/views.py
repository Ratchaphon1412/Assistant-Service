from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions


from .serializers import *

# Create your views here.


class AssistantAPI(APIView):
    def post(self, request, format=None):

        if request.data['query']:
            return Response({'response': 'Hello, how are you?'})

        return Response({'status': 'failer', 'category': 'Music'})


class UserAPI(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):

        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
