import pyttsx3
import speech_recognition as sr
import pyaudio
import winsound


engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice', voices[1].id)
engine.setProperty('volume', 0.90)
engine.setProperty('rate' , 180)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def takecommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("i listening.........")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("i recognizing...........")
        query = r.recognize_google(audio , language='en-in')
        print(f"User Said:{query}\n")

    except Exception as e:
        print(e)
        speak("Network connection Error")
        speak("Unable to recognize your voice")
        return 'None'
    return query

def Pass(pass_inp):
    password = "Sumit"
    passs = str(password)
    if passs == str(pass_inp):
        from Ai import startup
        from Ai import task
        speak("Access granted , now you can use this system ")
        startup()
        task()
    else:
        speak("Access not granted")

if __name__ == '__main__':
    while True:
        speak("this system is password protected")
        speak("kindly provide the password to access ")
        speak("tell your password")
        passsss = takecommand()
        Pass(passsss)











