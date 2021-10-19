import speech_recognition as sr
import webbrowser
import playsound
import os
import random
from gtts import gTTS
from time import ctime

r = sr.Recognizer()


def audio_data(ask=False):
    with sr.Microphone() as source:
        if ask:
            a_speak(ask)
        audio = r.listen(source)
        voice = ""
        try:
            voice = r.recognize_google(audio)
        except sr.UnknownValueError:
            a_speak("Try Again")
        except sr.RequestError:
            a_speak("Sorry, my service is down")
        return voice


def a_speak(a_string):
    tts = gTTS(text=a_string, lang="en")
    r = random.randint(1, 10000000)
    audio_file = 'audio-'+str(r)+'.mp3'
    tts.save(audio_file)
    playsound.playsound(audio_file)
    print(a_string)
    os.remove(audio_file)


def respond(voice):
    if 'I am fine' in voice:
        a_speak('Good to hear that')
    if 'search' in voice:
        search = audio_data('What do you want to search')
        url = "https:://google.com/search?q=" + search
        webbrowser.get().open(url)
        a_speak('Here is what I found for ' + search)
    if 'find location' in voice:
        location = audio_data('What is the location')
        url = "https:://google.nl/maps/place/" + location + '/&amp;'
        webbrowser.get().open(url)
        a_speak('Here is the location of ' + location)
    if 'exit' in voice:
        exit()
