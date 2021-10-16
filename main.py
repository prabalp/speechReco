import speech_recognition as sr
import webbrowser
import time

r = sr.Recognizer()


def audio_data(ask=False):
    with sr.Microphone() as source:
        if ask:
            print(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio)
        except sr.UnknownValueError:
            print("Try Again")
        except sr.RequestError:
            print("Sorry, my service is down")
        return voice


def respond(voice):
    if 'I am fine' in voice:
        print('Good to hear that')
    if 'search' in voice:
        search = audio_data('What do you want to search')
        url = "https:://google.com/search?q=" + search
        webbrowser.get().open(url)
        print('Here is what I found for ' + search)
    if 'find location' in voice:
        location = audio_data('What is the location')
        url = "https:://google.nl/maps/place/" + location + '/&amp;'
        webbrowser.get().open(url)
        print('Here is the location of ' + location)
    if 'exit' in voice:
        exit()


time.sleep(1)
print('Hello how are you?')
while 1:
    voice = audio_data()
    respond(voice)
