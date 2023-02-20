from django.shortcuts import render
from django.contrib.auth.models import User
# from rest_framework.permissions import IsAuthenticated

from rest_framework.views import APIView
from rest_framework.response import Response
from decouple import config
from rest_framework import authentication, permissions
from utils.AI.Wit import Wit
from utils.Knowledge.main import Knowlegde
from utils.TextToSpeech.textToSpeech import textTTS
import json

from .serializers import *

# Create your views here.

knowledge = Knowlegde(config('weatherAPI'), config('rapidAPI'),
                      config('googleAPI'), config('googleMapAPI'))
wit = Wit(config('witAPI'))
textToSpeechURL = textTTS({
    "Authorization": config('playhtAPIAuthorization'),
    "X-User-ID": config('playhtAPIX-User-ID')
})


class AssistantAPI(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request, format=None):
        if request.body.decode('utf-8'):
            requestJson = json.loads(request.body.decode('utf-8'))
            intent, confidence, entities = wit.getIntent(
                requestJson.get('query'))
            return Response({'intent': intent, 'confidence': confidence, 'entities': entities})
        return Response({'intent': None, 'confidence': None, 'entities': None})

    def get(self, request, format=None):
        return Response({'status': 'failer', 'category': 'Music'})


class KnowledgeAPI(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.body.decode('utf-8'):
            requestJson = json.loads(request.body.decode('utf-8'))
            text = knowledge.findsomething(requestJson.get('question'))
            return Response({'answer': text})

        return Response({'answer': None})


class TextToSpeech(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.body.decode('utf-8'):
            requestJson = json.loads(request.body.decode('utf-8'))
            print("test1")
            voiceURL = textToSpeechURL.changetextTV(requestJson['text'])
            print(voiceURL)
            return Response({'url': voiceURL})
        return Response({'url': None})


class WeatherAPI(APIView):
    # permission_classes = [IsAuthenticated]

    def post(self, request):
        if request.body.decode('utf-8'):
            requestJson = json.loads(request.body.decode('utf-8'))
            text = knowledge.weather(requestJson.get('city'))

            return Response({'weather': text})
