from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions
from utils.AI.Wit import Wit
from utils.Knowledge.main import Knowlegde

import json

from .serializers import *

# Create your views here.


class AssistantAPI(APIView):
    def post(self, request, format=None):

        if request.data['query']:
            print(request.data['query'])
            # not good to do this
            wit = Wit('Bearer HD7463MS2IMBGP4AW4AFFGTZGVIUF2GI')
            intent, confidence, entities = wit.getIntent(request.data['query'])
            print(intent, confidence, entities)

            return Response({'intent': intent, 'confidence': confidence, 'entities': entities})

        return Response({'intent': None, 'confidence': None, 'entities': None})

    def get(self, request, format=None):
        return Response({'status': 'failer', 'category': 'Music'})


class KnowledgeAPI(APIView):
    def post(self, request):
        if request.data['query']:
            knowledge = Knowlegde('f2b10a33ba4535b73fc9845ab9ffef10', '091aed48d7mshac28a14304d11cap1182e7jsn2d5daa5546cc',
                                  'AIzaSyDyS4AG25zm3dape-5shH65PqdDQjkV2Sw', 'AIzaSyBmhSoUadgZp9FKCYFhuxUaRjKTYTZ71T8')
            if request.data['query']:
                print(type(request.data['query']))
                text = knowledge.findsomething(request.data['query'])
                return Response({'answer': text})
            return Response({'answer': None})


class UserAPI(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):

        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
