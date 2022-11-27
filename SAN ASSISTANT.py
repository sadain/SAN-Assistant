import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os
import smtplib
import random

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wish_me():
    hour = int(datetime.datetime.now().hour)

    if hour >= 0 and hour < 12:
        speak("Good Morning!")

    elif hour >= 12 and hour < 18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")
    speak("I am San-pi sir. Please tell me how may i help you")


def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print(f'user said:{query}\n')

    except Exception as e:
        print(e)
        print('say that again please...')
        return 'None'
    return query


def send_email():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login("nsasadain@gmail.com", "sadainnsa@2002")
    server.sendmail("nsasadain@gmail.com", to, content)
    server.close()


if __name__ == "__main__":
    wish_me()
    while True:
        query = take_command().lower()

        if 'wikipedia' in query:
            speak("Searching Wikipedia...")
            query = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open stackoverflow' in query:
            webbrowser.open("stackoverflow.com")

        elif 'play nazam' in query:
            music_dir = "E:\\ISLAMIC ACTIVETY SECTION\\NAZAM"
            music = os.listdir(music_dir)
            print(music)
            os.startfile(os.path.join(music_dir, music[random]))

        elif 'the time' in query:
            strtime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir, the time is{strtime}")

        elif 'open pycharm' in query:
            codepath = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\JetBrains"
            os.startfile(codepath)

        elif 'send email' in query:
            try:
                speak("what shoud i say")
                content = take_command()
                to = "nsasadain@gmail.com"
                send_email(to, content)
                speak("Email has been send!")

            except Exception as e:
                print(e)
                speak("Sorry sir. i am not able to send this email!")

