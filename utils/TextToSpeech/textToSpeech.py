# from playsound import playsound
import requests
import asyncio
import json
# import os
import time


class textTTS:
    def __init__(self, playhtHeader):
        self.playhtHeader = playhtHeader

    def changetextTV(self, text):
        endpoint = "https://play.ht/api/v1/"

        headers = {
            'Authorization': self.playhtHeader['Authorization'],
            'X-User-ID': self.playhtHeader['X-User-ID'],
            'Content-Type': 'application/json'
        }
        payloads = {
            "voice": 'th-TH-NiwatNeural',
            "content": [text],
            "title": 'test'
        }
        response = requests.post(
            endpoint+'convert', headers=headers, json=payloads)
        time.sleep(5)
        # await asyncio.sleep(10)
        print(response.text)
        dic_response = json.loads(response.text)
        print(dic_response['status'])
        if (dic_response['status'] == 'CREATED'):
            responseVoice = requests.get(
                endpoint + 'articleStatus?transcriptionId=' + dic_response['transcriptionId'], headers=headers)
            print(responseVoice.text)
            dic_responseVoice = json.loads(responseVoice.text)
            print(dic_responseVoice['audioUrl'])
            return dic_responseVoice['audioUrl']
            # downloadMP3 = requests.get(dic_responseVoice['audioUrl'])
            # open('./Sound/Voice.mp3', 'wb').write(downloadMP3.content)
            # playsound('./Sound/Voice.mp3')
            # os.remove('./Sound/Voice.mp3')
        return None

    # async def main(self, text):

    #     # return await asyncio.gather(self.findingData(), self.changetextTV(text))
    #     return await asyncio.run(self.changetextTV(text))

    # def nofeature(self):
    #     return playsound('./Sound/nofeature.mp3')

    # def dontunderstand(self):
    #     return playsound('./Sound/don\'tunderstand.mp3')

    # async def findingData(self):
    #     return playsound('./Sound/finddata.mp3')

    # def problemPlayht(self):
    #     return playsound('./Sound/problem.mp3')
