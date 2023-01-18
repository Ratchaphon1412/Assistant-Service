from geopy.geocoders import Nominatim
import geocoder
import requests
import json


class Geolocation:
    def __init__(self, rapidAPI):
        self.rapidAPI = rapidAPI

    def getGeoLocation(self):
        Nomi_locator = Nominatim(user_agent="My App")
        my_location = geocoder.ip("me")

        # my latitude and longitude coordinates
        latitude = my_location.geojson["features"][0]["properties"]["lat"]
        longitude = my_location.geojson["features"][0]["properties"]["lng"]
        return latitude, longitude

    def getPlaceGeolocation(self, text):
        enpoint = "https://google-maps-geocoding.p.rapidapi.com/geocode/json"
        headers = {
            "X-RapidAPI-Key": self.rapidAPI,
            "X-RapidAPI-Host": "google-maps-geocoding.p.rapidapi.com",
        }
        param = {"address": text, "language": "th"}
        response = requests.get(enpoint, headers=headers, params=param)
        dicresponse = json.loads(response.text)

        if dicresponse["status"] == "OK":
            lat = dicresponse["results"][0]["geometry"]["location"]["lat"]
            long = dicresponse["results"][0]["geometry"]["location"]["lat"]
            # name = dicresponse["results"][0]["formatted_address"]
            return lat, long
        else:
            return
