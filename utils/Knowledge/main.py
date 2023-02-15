from .geolocation import Geolocation
from .nlg import Nlg
from .weather import Weather
from .knowledgeGoogle import KnowledgeGoogle
# from .coreLocationMacOS import CoreLocationMacOS


class Knowlegde(Geolocation, Nlg, Weather, KnowledgeGoogle):
    def __init__(self, weatherAPI, rapidAPI, googleAPI, googleMapAPI):
        Geolocation.__init__(self, rapidAPI)
        Nlg.__init__(self)
        Weather.__init__(self, weatherAPI)
        KnowledgeGoogle.__init__(self, googleAPI, googleMapAPI)
        # self.CORE_LOCATION = CoreLocationMacOS.alloc().init()

    def weather(self, entities):
        text = None
        if entities == None:
            # when entities is empty
            # lat1, long1 = self.CORE_LOCATION.getCoreLocationMac()
            # print(lat1, long1)
            # if (lat1 == None and long1 == None):
            #     lat, long = self.getGeoLocation()
            #     des, temp = self.weatherCurrent(lat, long)
            #     text = self.answerWeather(des, temp)
            # else:
            #     des, temp = self.weatherCurrent(lat1, long1)
            #     text = self.answerWeather(des, temp)
            pass
        else:
            # entitiesKey = entities.keys()
            # location = None
            # *time not use now
            # time = None
            # for key in list(entitiesKey):
            #     if key == "location:location":
            #         for listinlocation in entities["location:location"]:
            #             max = 0
            #             if listinlocation["confidence"] >= max:
            #                 max = listinlocation["confidence"]
            #                 location = listinlocation["value"]

            #     if key == "time:time":
            #         for listintime in entities["time:time"]:
            #             max = 0
            #             if listintime["confidence"] >= max:
            #                 max = listintime["confidence"]
            #                 time = listintime["value"]
            # if location != None
            if entities != None:
                lat, long = self.getPlaceGeolocation(entities)
                des, temp = self.weatherCurrent(lat, long)
                text = self.answerPlaceWeather(des, temp, entities)
            else:
                # lat1, long1 = self.CORE_LOCATION.getCoreLocationMac()
                # print(lat1, long1)
                # if (lat1 == None and long1 == None):
                #     lat, long = self.getGeoLocation()
                #     des, temp = self.weatherCurrent(lat, long)
                #     text = self.answerWeather(des, temp)
                # else:
                #     des, temp = self.weatherCurrent(lat1, long1)
                #     text = self.answerWeather(des, temp)
                pass
        return text

    def findsomething(self, entities):
        data = None
        # for key in list(entities):
        #     if key == "data:data":
        #         max = 0
        #         for listData in entities["data:data"]:
        #             if listData["confidence"] >= max:
        #                 max = listData["confidence"]
        #                 data = listData["value"]
        # listText = self.findknowledgeGoogle(data)
        listText = self.findknowledgeGoogle(entities)

        text = self.ansQuestion(listText)

        return text

    # def findRestaurantNearMe(self):
    #     lat, long = self.CORE_LOCATION.getCoreLocationMac()
    #     if (lat == None and long == None):
    #         return None
    #     else:
    #         list_restaurant = self.nearPlaceRestaurant(lat, long)
    #         print(list_restaurant)
    #         text = self.ansRestaurant(list_restaurant)

    #         return text
