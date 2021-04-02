import pyttsx3
import speech_recognition as sr
import datetime
from playsound import playsound
import wikipedia
import webbrowser
import os
import smtplib




engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

engine.setProperty('voice', voices[0].id)


 
 
 
 
 
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour= int(datetime.datetime.now().hour)
    if hour>=0 and hour<=12:
        speak("good morning!")

    elif hour>=12 and hour<=18:
        speak("good afternoon!")

    else:
        speak("good evening!")


    speak("i am online , satalite no 12304 is ready ,  all functions can be controlled now , hello  yuvraj sir i am your jarvis please tell me how may i help you")

        
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("listening....")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing>...")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said: {query}\n")

    except Exception as e:
        speak("say that again please...")
        return "None"
    return query


 





def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('singhyuvraj42259@gmail.com', '8123327133')
    server.sendmail('singhyuvraj42259@gmail.com', to, content)
    server.close()



            
            



if __name__== "__main__":
    wishMe()
    
    
    while True:
        query = takeCommand().lower()
        if "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia","")
            results = wikipedia.summary(query, sentences=2)
            speak("according to wikipedia")
            print(results)
            speak (results)
        elif'open youtube' in query:
            webbrowser.open('youtube.com')
            
        elif'open google' in query:
            webbrowser.open('google.com')
         
        elif'open stackoverflow' in query:
            webbrowser.open('stackoverflow.com')
             
        



        #elif'play music' in query:
            #for music directory in computer
            #music_dir = "path of music files
            #songs = os.listdir(music_dir)
            #print(songs)
            #os.startfile(os.path,join(music_dir,songs[0]))

        elif 'time' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"sir the time is{strTime}")

        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codePath) 
            speak("opening")


        if "jarvis are you online" in query:
            speak("i am online and ready")



        if "hey jarvis" in query:
            speak("hello yuvraj sir")


        if "how does the dog speak" in query:
             speak("bhow bhow")


        if "who made you" in query:
            speak ("i was made by yuvraj singh")


        if "do you have any crush" in query:
            speak("i have a crush on internet")


        if "close" in query:
            speak("i am offline")
        
        if "start" in query:
            speak("i am online")
        
    
        
          





        if "you are genius" in query:
            speak("thank you making me sir this is because of you")            

 


        
        elif 'send email' in query:
            try:
                speak("What should i say")
                content = takeCommand()
                to = "bullzie.inc@gmail.com"
                sendEmail(to, content)
            except Exception as e:
                  print(e)
                  speak("sorry sir .i am not able to send this email")


        
        elif 'alarm' in query:
           speak("enter the time!")
           time = input(": enter the time:")

           while True:
               Time_Ac = datetime.datetime.now()
               now = Time_Ac.strftime("%H:%M:%S")


               if now == time:
                   speak("time to wake up yuvraj sir please go to freedom park and get fit")
                   playsound("yu.mp3")
                   speak("alarm closed")


              


                 


           

                    
               









               




           

