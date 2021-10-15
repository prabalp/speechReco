import speech_recognition as sr
import webbrowser

r = sr.Recognizer()


def audio_data():
    with sr.Microphone() as source:
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
    # if 'search' in voice:
    #     search = audio_data('What do you want to search')


print('Hello how are you?')
voice = audio_data()
respond(voice)
