import time
import functions


time.sleep(1)
functions.a_speak("Hello how are you?")
while 1:
    voice = functions.audio_data()
    functions.respond(voice)
