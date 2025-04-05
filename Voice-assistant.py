# import pyttsx3
# import speech_recognition as sr
# import datetime
# import wikipedia
# import webbrowser
# import os
# # import smtplib


# engine = pyttsx3.init('sapi5')
# voices = engine.getProperty('voices')

# engine.setProperty('voice', voices[0].id)


# def speak(audio):
#     engine.say(audio)
#     engine.runAndWait()


# def wishMe():
#     hour = int(datetime.datetime.now().hour)
#     if hour>=0 and hour<12:
#         speak("Hello, Good Morning Sir!")

#     elif hour>=12 and hour<18:
#         speak("Hello, Good Afternoon Sir!")

#     else:
#         speak("Hello, Good Night Sir!")

#     speak("I am your assistant, Jarvess . Please tell me how may I help you")

# def takeCommand():
#     #It takes microphone input from user and returns string output

#     r = sr.Recognizer()
#     with sr.Microphone() as source:
#         print("Listening:")
#         r.pause_threshold = 1
#         audio = r.listen(source)

#     try:
#         # print("You said " + r.recognize_google(audio, language='en-in'))
#         print("Recognizing...")
#         query = r.recognize_google(audio, language='en-in')
#         print(f"You said: {query}\n")
#     except sr.UnknownValueError:
#         print("Could not understand audio")
#         return "None"
#     except sr.RequestError as e:
#         # print("Could not request results; {0}".format(e))
#         print(f"Could not request results; {e}")
#         return "None"
#     return query

# # def sendEmail(to, content):
# #     server = smtplib.SMTP('smtp.gmail.com', 587)
# #     server.ehlo()
# #     server.starttls()
# #     server.login('youremail@gmail.com', 'your-password')
# #     server.sendmail('youremail@gmail.com', to, content)
# #     server.close()

        
# if __name__ == "__main__":
#     wishMe()
#     while True:
#         query = takeCommand().lower()

#         if query == "none":
#             continue

#         # Logic for executing tasks based on query
#         if 'wikipedia' in query:
#             speak('Searching Wikipedia...')
#             query = query.replace("wikipedia", "")
#             results = wikipedia.summary(query, sentences=2)
#             speak("According to Wikipedia")
#             speak(results)
        
        
#         elif 'open youtube' in query:
#             speak("Opening YouTube...")
#             chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
#             webbrowser.get(chrome_path).open('https://www.youtube.com')

#         # elif 'play music' in query:
#         #     music_dir = 'C:\\Users\\hp\\Music'
#         #     songs = os.listdir(music_dir)
#         #     print(songs)
#         #     os.startfile(os.path.join(music_dir, songs[0]))

#         elif 'time kya hai' in query:
#             strTime = datetime.datetime.now().strftime("%H:%M:%S")
#             speak(f"Sir, time is {strTime}")
        
#         elif 'open code' in query:
#             codePath = "C:\\Users\\hp\\Microsoft VS Code\\Code.exe"
#             os.startfile(codePath)

#         # elif 'email to aadi' in query:
#         #     try:
#         #         speak("What should I say?")
#         #         content = takeCommand()
#         #         to = "aadiyourEmail@gmail.com"
#         #         sendEmail(to, content)
#         #         speak("Email has been send!")
#         #     except Exception as e:
#         #         print(e)
#         #         speak("Sorry my friend aadi bhai. I am not able to send this email")


#         elif 'open whatsapp' in query:
#             speak("Opening whatsapp")
#             chrome_path = 'C:/Program Files/Google/Chrome/Application/chrome.exe %s'
#             webbrowser.get(chrome_path).open('https://web.whatsapp.com/')

#         elif 'open chrome' in query:
#             codePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
#             os.startfile(codePath)

#         elif 'exit' in query or 'quit' in query:
#             speak("Goodbye Sir!")
#             break





import pyttsx3
import speech_recognition as sr
import datetime
import wikipedia
import webbrowser
import os

# Initialize the text-to-speech engine
engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')

# Set the voice (0 for male, 1 for female, etc.)
engine.setProperty('voice', voices[0].id)

# Speak function
def speak(audio):
    engine.say(audio)
    engine.runAndWait()

# Function to greet the user based on the time
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour >= 0 and hour < 12:
        speak("Hello, Good Morning Sir!")
    elif hour >= 12 and hour < 18:
        speak("Hello, Good Afternoon Sir!")
    else:
        speak("Hello, Good Night Sir!")
    speak("I am your assistant, Jarvess. Please tell me how may I help you.")

# Function to listen to the user's voice and convert it into text
def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Recognizing...")
        query = r.recognize_google(audio, language='en-in')
        print(f"You said: {query}\n")
    except sr.UnknownValueError:
        print("Could not understand audio")
        return "None"
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return "None"
    return query.lower()

# Main function
if __name__ == "__main__":
    wishMe()
    while True:
        query = takeCommand()

        if query == "none":
            continue

        # Wikipedia search
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia", "")
            try:
                results = wikipedia.summary(query, sentences=2)
                speak("According to Wikipedia")
                speak(results)
            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"There are multiple results for {query}. Please be more specific.")
            except wikipedia.exceptions.PageError:
                speak(f"Sorry, I could not find any result for {query}.")

        # Open YouTube
        elif 'open youtube' in query:
            speak("Opening YouTube...")
            webbrowser.open('https://www.youtube.com')

        # Check time
        elif 'time kya hai' in query or 'what time is it' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir, the time is {strTime}")

        # Open Visual Studio Code
        elif 'open code' in query:
            codePath = "C:\\Users\\hp\\Microsoft VS Code\\Code.exe"
            if os.path.exists(codePath):
                speak("Opening Visual Studio Code...")
                os.startfile(codePath)
            else:
                speak("Sorry, I could not find Visual Studio Code on your system.")

        # Open WhatsApp
        elif 'open whatsapp' in query:
            speak("Opening WhatsApp...")
            webbrowser.open('https://web.whatsapp.com/')

        # Open Chrome
        elif 'open chrome' in query:
            chromePath = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            if os.path.exists(chromePath):
                speak("Opening Google Chrome...")
                os.startfile(chromePath)
            else:
                speak("Sorry, I could not find Google Chrome on your system.")

        # Exit the assistant
        elif 'exit' in query or 'quit' in query:
            speak("Goodbye Sir!")
            break
