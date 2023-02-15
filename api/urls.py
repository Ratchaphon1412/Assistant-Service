from django.urls import path, include
from .views import *

urlpatterns = [
    path('ai/', AssistantAPI.as_view()),
    path('knowledge/', KnowledgeAPI.as_view()),
    path('texttospeech/', TextToSpeech.as_view()),
    path('weather/', WeatherAPI.as_view()),
]
