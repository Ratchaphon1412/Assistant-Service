import speech_recognition as sr

class SpeechTT:
    def __init__(self):
       pass

    def startListen(self):
        # obtain audio from the microphone
        r = sr.Recognizer()
        r.energy_threshold = 4000
        with sr.Microphone() as microphone:
            print("Say something!")
            audio = r.listen(microphone)
        return audio,r

    def changevoiceTT(self,audio,recognizer):
        # recognize speech using Google Speech Recognition
        text = None
        try:
            
            text = recognizer.recognize_google(audio,language = "th-TH")
        except sr.UnknownValueError:
            print("Google Speech Recognition could not understand audio")
        except sr.RequestError as e:
            print("Could not request results from Google Speech Recognition service; {0}".format(e))

        return text
            
        
        

        


        
       
