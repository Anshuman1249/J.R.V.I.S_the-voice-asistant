import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import subprocess # you will only need this library for linux distributions
import os 

engine = pyttsx3.init('espeak') # for windows use engine = pyttsx3.init()  
engine.setProperty('rate', 125)
voices = engine.getProperty('voices')
engine.setProperty('voice', 'en-us1')


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!")

    else:
        speak("Good Evening!")

    speak("I am Jarvis, Please tell me How may i help you today?")

def takecommand():
    # It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source
        r.pause_threshold = 1 
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language="en-in")
        print("User said: ", query)

    except Exception as e:
        print("Say that again please...")
        return "None"    
    return query


if __name__ =="__main__":
    wishme()
    while True:
        query = takecommand().lower()
        
        if 'hey jarvis' in query:
            wishMe()
            print("Listening...")

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("Wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("Accoriding to Wikipedia")
            print(results)  
            speak(results)

        elif 'open youtube' in query:
            webbrowser.open("https://www.youtube.com")

        elif 'open google' in query:
            webbrowser.open("https://www.google.com")    

        elif 'open stackoverflow' in query:
            webbrowser.open("https://www.stackoverflow.com")


        elif 'play music' in query:
            music_dir = '/put/your/music_directory/path/here/'
            songs = os.listdir(music_dir)
            print(songs)
            subprocess.call(["xdg-open", os.path.join(music_dir, songs[0])]) # subprocess library can only be used in linux
            #Alternative program line for windows can be  os.startfile(os.path.join(music_dir, songs[0]))
        
        elif 'the time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            print("Time:" + strTime)
            speak(f"Sir, the time is {strTime}")
        
        elif 'open vs code' in query:
            subprocess.Popen(["code"])
        #for windows os users use the following program insted of the the above 2 lines
        #elif 'open vs code in query:
        #codePath = "put\\your\\executable\\file's\\path\\here\\" 
        # os.startfile(codePath)

        elif 'stop' in query:
            speak("Okay, goodbye!")
            break

        
