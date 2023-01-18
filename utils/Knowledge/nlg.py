from fileinput import close
from heapq import merge
import random


class Nlg:
    def __init__(self):
        pass

    def answerWeather(self, des, temp):
        mergeString = ["มี", " สภาพอากาศที่คุณอยู่ มี", "ณ ที่คุณอยู่ มี"]
        speechtemp = ["", " อุณหภูมิประมาณ " + temp + "องศา"]
        speech = None
        if "ฝน" in des:
            speech = mergeString[random.randrange(
                0, 2)] + des + speechtemp[random.randrange(0, 1)] + "อย่าลืมพกร่มไปด้วยนะครับ"
        else:
            speech = mergeString[random.randrange(
                0, 2)] + des + speechtemp[random.randrange(0, 1)] + "ครับ"
        print(speech)
        return speech

    def answerPlaceWeather(self, des, temp, text):
        mergeString = ["จากที่ทราบข้อมูล แถวๆ บริเวณ ",
                       "บริเวณ ", "จากข้อมูลพบว่า แถวนั้น "]
        desMerge = ["มี", "สภาพอากาศ มี"]
        speechtemp = ["", " อุณหภูมิประมาณ " + temp + "องศา"]

        if "ฝน" in des:
            speech = mergeString[random.randrange(0, 2)] + text + desMerge[random.randrange(
                0, 1)] + des + speechtemp[random.randrange(0, 2)] + "อย่าลืมพกร่มไปด้วยนะครับ"
        else:
            speech = mergeString[random.randrange(0, 2)] + text + desMerge[random.randrange(
                0, 1)] + des + speechtemp[random.randrange(0, 2)] + "ครับ"

        print(speech)
        return speech

    def ansQuestion(self, listText):

        start = ['ข้อมูลที่ผมพบทั้งหมด จำนวน ',
                 'จากข้อมูลที่พบทั้ง ', 'ข้อมูลที่หาได้ ']
        text = start[random.randrange(0, 2)] + \
            str(len(listText)) + ' การค้นหา '
        print(text)
        merge = ""
        for i in range(len(listText)):

            merge += "ข้อมูลชุดที่ " + str(i+1) + " " + str(listText[i])
        print(text + merge)
        return text + merge

    def ansRestaurant(self, list_restaurant):
        start = [
            'ร้านอาหารที่ผม พบบริเวณใกล้ๆคุณ ระยะทางไม่เกิน 1.5 กิโลเมตร มีทั้งหมด ', 'ร้านอาหารที่พบใกล้ๆคุณ มีทั้งหมด ', 'จากการค้นหา ร้านอาหารที่ใกล้ๆคุณ พบทั้งหมด ']
        text = start[random.randrange(0, 3)] + \
            str(len(list_restaurant)) + " ร้าน "

        for i in range(len(list_restaurant)):
            text += "ร้านที่ " + str(i+1) + " " +\
                list_restaurant[i]['name'] + "  "
        text += "ต้องการไปร้านไหนไหมครับ"

        return text
