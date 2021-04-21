import pyttsx3
engine=pyttsx3.init()
msg=input("Enter what you want to get spoken:  ")
engine.say(msg)
engine.runAndWait()