from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from utils.AI.Wit import Wit

from .serializers import *

# Create your views here.


class AssistantAPI(APIView):
    def post(self, request, format=None):

        if request.data['query']:
            print(request.data['query'])
            wit = Wit('W2FXIUBZXFPX7FBJFJ5WYRJBU72LOEZ3')
            intent, confidence, entities = wit.getIntent(request.data['query'])
            print(intent, confidence, entities)

            return Response({'intent': intent, 'confidence': confidence, 'entities': entities})

        return Response({'status': 'failer', 'category': 'Music'})

    def get(self, request, format=None):
        return Response({'status': 'failer', 'category': 'Music'})


class UserAPI(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):

        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
