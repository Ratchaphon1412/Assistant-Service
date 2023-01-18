import requests
import json
class Weather:
    def __init__(self,weatherAPI):
        self.__weatherAPI = weatherAPI
    def weatherCurrent(self,lat,long):
        r =requests.get(f'https://api.openweathermap.org/data/2.5/weather?lat={lat}&lon={long}&lang=th&appid={self.__weatherAPI}')
        print(r.text)
        dic = json.loads(r.text)
        
        description = dic["weather"][0]["description"]
        temp = str("{:.2f}".format(dic["main"]["temp"]- 273.15))
        
        return description,temp

