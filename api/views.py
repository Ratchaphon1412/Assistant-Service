from django.shortcuts import render
from django.contrib.auth.models import User


from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
from rest_framework import authentication, permissions
from utils.AI.Wit import Wit
from utils.Knowledge.main import Knowlegde
from utils.TextToSpeech.textToSpeech import textTTS


import asyncio
import json

from .serializers import *

# Create your views here.


class AssistantAPI(APIView):
    def post(self, request, format=None):

        # if request.data.get('data').get('_streams')[1]:
        #     # print(request.data['query'])
        #     # not good to do this
        #     wit = Wit('Bearer HD7463MS2IMBGP4AW4AFFGTZGVIUF2GI')
        #     print(request.data['query'])
        #     intent, confidence, entities = wit.getIntent(
        #         request.data.get('data').get('_streams')[1])
        #     print(intent, confidence, entities)

        #     return Response({'intent': intent, 'confidence': confidence, 'entities': entities})

        if request.body.decode('utf-8'):
            requestJson = json.loads(request.body.decode('utf-8'))

            wit = Wit(config('witAPI'))
            intent, confidence, entities = wit.getIntent(
                requestJson.get('query'))
            return Response({'intent': intent, 'confidence': confidence, 'entities': entities})
        return Response({'intent': None, 'confidence': None, 'entities': None})

    def get(self, request, format=None):
        return Response({'status': 'failer', 'category': 'Music'})


class KnowledgeAPI(APIView):
    def post(self, request):

        if request.body.decode('utf-8'):
            knowledge = Knowlegde(config('weatherAPI'), config('rapidAPI'),
                                  config('googleAPI'), config('googleMapAPI'))
            requestJson = json.loads(request.body.decode('utf-8'))
            # print(type(request.data['query']))
            text = knowledge.findsomething(requestJson.get('question'))
            return Response({'answer': text})

        return Response({'answer': None})


class TextToSpeech(APIView):
    def post(self, request):

        if request.body.decode('utf-8'):
            requestJson = json.loads(request.body.decode('utf-8'))
            # print(requestJson.get('text'))
            textToSpeechURL = textTTS({
                "Authorization": config('playhtAPIAuthorization'),
                "X-User-ID": config('playhtAPIX-User-ID')
            })
            print("test1")
            voiceURL = textToSpeechURL.changetextTV(requestJson['text'])
            # voiceURL = textToSpeechURL.main(requestJson['text'])
            print(voiceURL)
            return Response({'url': voiceURL})
        return Response({'url': None})


class WeatherAPI(APIView):
    def post(self, request):
        if request.body.decode('utf-8'):
            requestJson = json.loads(request.body.decode('utf-8'))
            knowledge = Knowlegde(config('weatherAPI'), config('rapidAPI'),
                                  config('googleAPI'), config('googleMapAPI'))
            text = knowledge.weather(requestJson.get('city'))

            return Response({'weather': text})


class UserAPI(APIView):
    authentication_classes = [authentication.TokenAuthentication]
    permission_classes = [permissions.IsAdminUser]

    def get(self, request, format=None):

        usernames = [user.username for user in User.objects.all()]
        return Response(usernames)
