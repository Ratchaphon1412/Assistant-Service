import json
import requests


class KnowledgeGoogle:
    def __init__(self, googleAPI, googleMapAPI):
        self.googleKey = googleAPI
        self.googleMapKey = googleMapAPI

    def findknowledgeGoogle(self, text):
        endpoint = 'https://kgsearch.googleapis.com/v1/entities:search'
        params = {
            'query': text,
            'limit': 5,
            'indent': True,
            'key': self.googleKey,
            'languages': 'th'
        }
        response = requests.get(endpoint, params=params)
        print(response.text)
        articleList = []
        listData = json.loads(response.text)
        if (len(listData['itemListElement']) != 0):
            for diclist in listData['itemListElement']:
                if('result' in diclist):
                    if('detailedDescription' in diclist['result']):
                        if('articleBody' in diclist['result']['detailedDescription']):
                            articleList.append(
                                diclist['result']['detailedDescription']['articleBody'])

        return articleList

    def nearPlaceRestaurant(self, lat, long):
        endpoint = f"https://maps.googleapis.com/maps/api/place/nearbysearch/json?location={lat},{long}&radius=1500&type=restaurant&key={self.googleMapKey}&language=th"
        response = requests.get(endpoint)
        dict_response = json.loads(response.text)
        list_restaurant = []

        for i in range(len(dict_response['results'])):
            print(dict_response['results'][i]['name'])
            dict_compressrestaurant = {}
            dict_compressrestaurant['name'] = dict_response['results'][i]['name']
            dict_compressrestaurant['geometry'] = dict_response['results'][i]['geometry']
            dict_compressrestaurant['vicinity'] = dict_response['results'][i]['vicinity']
            list_restaurant.append(dict_compressrestaurant)
            dict_compressrestaurant = {}

        return list_restaurant
