import time
import functions


# time.sleep(1)
print("Say Natasha to interact")
# functions.a_speak("Hello how are you?")

active = functions.audio_data()
if active == "Natasha":
    functions.a_speak("Are you feeling well")
    time.sleep(1)
    while 1:
        voice = functions.audio_data()
        functions.respond(voice)
elif active == "exit":
    exit()
else:
    print("Try Again or say exit")
