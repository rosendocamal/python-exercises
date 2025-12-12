# Instalar SpeechRecognition con pip install SpeechRecognition
import speech_recognition as sr
import webbrowser
# Instalar pyttsx3 con pip install pyttsx3
import pyttsx3
import pyaudio

recognizer = sr.Recognizer()

engine = pyttsx3.init()


def talk():
    mic = sr.Microphone()
    with mic as source:
        audio = recognizer.listen(source)

    text = recognizer.recognize_google(audio, language='ES')

    msg = f'Has dicho: {text}'
    print(msg)
    engine.say(msg)
    return text.lower()


if 'amazon' in talk():
    engine.say('Qué quieres comprar en Amazon')
    engine.runAndWait()
    text = talk()

    webbrowser.open(f'https://www.amazon.com.mx/s?k={text}')

    engine.say(f'Abriendo la página de Amazon México para comprarte {text}.')