import pyttsx3
import datetime
import time
import subprocess
import requests
import random
import wolframalpha
import webbrowser
import speech_recognition as sr
import json
# using the driver made by microsoft
engine = pyttsx3.init("sapi5")
voices = engine.getProperty('voices')
engine.setProperty('voice', 'voices[0].id')


# function for the speaking action of the assistant
def speak(text):
    engine.say(text)
    engine.runAndWait()


def speakingFreida():
    # assistant knows how to greet according to the time
    def greet():
        print('This is your voice assistant - Freida')
        speak('This is your voice assistant - Freida')
        clock = datetime.datetime.now().hour
        if 0 <= clock < 12:
            speak("Good Morning!")
            print("Good Morning!")
        elif 12 <= clock < 18:
            speak("Good Afternoon!")
            print("Good Afternoon!")
        else:
            speak("Good Evening!")
            print("Good Evening!")

    greet()

    # coding the command thrown by the user to make it understandable to Freida using the speech recognition package
    def takeATask():
        r = sr.Recognizer()
        with sr.Microphone() as source:
            print("Listening...")
            audio = r.listen(source)

            try:
                userTask = r.recognize_google(audio, language='en-in')
                print(f"user said:{userTask}\n")

            except Exception as e:
                speak("Pardon me, please say that again")
                return "None"
            return userTask

    # start

    while True:
        speak("Can I help you with anything?")
        userTask = takeATask().lower()
        if userTask == 0:
            continue
        
        elif 'how are you' in userTask:
            speak('I am really good, thank you, how are you?')
            howisuser=takeATask()
            if('good' in howisuser):
                speak('Happiness is a state of mind')
            elif('sad' in howisuser):
                speak('Seek the good things, like talking to me')
            time.sleep(5)

        elif 'who are you' in userTask or 'what can you do'  in userTask:
            speak('I am Freida. I am a personal voice assistant created with the help of stack overflow and other '
                  'websites. '
                  'I am still in a updating process, but up until now, i can tell some dad jokes'
                  'open youtube, chrome, gmail and stack overflow, i can tell the time, describe the weather'
                  'in different cities all around the globe, get news from Diji 24 and you can ask me '
                  'mathematical questions.')
            time.sleep(5)

        elif "who made you" in userTask or "who created you" in userTask or "who discovered you" in userTask:
            speak("Monica created me. Connect with her on Linkedin.")
            webbrowser.open_new_tab("https://www.linkedin.com/in/monica-leti%C8%9Bia-marinca%C8%99-a12289203")
            print("Monica created me. Connect with her on Linkedin.")
            time.sleep(7)

        elif "weather" in userTask:
            api_key = "8ef61edcf1c576d65d836254e11ea420"
            base_url = "https://api.openweathermap.org/data/2.5/weather?"
            speak("What's the city name?")
            city_name = takeATask()
            complete_url = base_url + "appid=" + api_key + "&q=" + city_name
            response = requests.get(complete_url)
            x = response.json()  # using json to access data
            if x["cod"] != "404":
                y = x["main"]
                current_temperature = y["temp"] - 272
                current_humidity = y["humidity"]
                z = x["weather"]
                weather_description = z[0]["description"]
                speak("Temperature in Celsius unit is " +
                      str(round(current_temperature, 2)) +
                      "\n humidity in percentage is " +
                      str(current_humidity) +
                      "\n description  " +
                      str(weather_description))
                print("Temperature in Celsius unit = " +
                      str(round(current_temperature, 2)) +
                      "\n humidity (in percentage) = " +
                      str(current_humidity) +
                      "\n description = " +
                      str(weather_description))
            else:
                speak("City Not Found")

            time.sleep(5)

        elif 'time' in userTask:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"the time is {strTime}")
            time.sleep(5)

        elif 'open youtube' in userTask:
            webbrowser.open_new_tab("https://www.youtube.com")
            speak("opening youtube")
            time.sleep(5)

        elif 'open google' in userTask:
            webbrowser.open_new_tab("https://www.google.com")
            speak("opening Chrome")
            time.sleep(5)

        elif 'open gmail' in userTask:
            webbrowser.open_new_tab("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox")
            speak("opening Gmail")
            time.sleep(5)

        elif "open stack overflow" in userTask:
            webbrowser.open_new_tab("https://stackoverflow.com/")
            speak("Opening stackoverflow")
            time.sleep(5)

        elif 'open facebook' in userTask:
            webbrowser.open_new_tab("https://www.facebook.com/")
            speak("Opening facebook. Don't waste your time though.")
            time.sleep(5)

        elif 'joke' in userTask:
            array = ["Hear about the new restaurant called Karma? There’s no menu: You get what you deserve.",
                     "Did you hear about the claustrophobic astronaut? He just needed a little space.",
                     "How does Moses make tea? He brews.",
                     "Why don’t Calculus majors throw house parties? Because you should never drink and derive."]
            speak(random.choice(array))
            speak("I'm trying my best to say jokes. How was it?")
            userTask1 = takeATask().lower()
            if 'good' in userTask1 or 'great' in userTask1 or 'amazing' in userTask1:
                speak("Thank you!")
            elif 'bad' in userTask1 or 'not ok' in userTask1 or 'boring' in userTask1:
                speak("Oh shoot, better luck for me next time.")
            time.sleep(5)

        elif 'siri' in userTask:
            speak('I know Siri for a long time. We are good friends, she is my mentor.')
            print('I know Siri for a long time. We are good friends, she is my mentor.')
            time.sleep(3)

        elif 'alexa' in userTask:
            speak('I know Alexa but I am better friends with Siri. Alexa is mean, maybe because she is smarter.')
            print("I know Alexa but I am better friends with Siri. Alexa is mean, maybe because she is smarter.")
            time.sleep(3)

        elif 'news' in userTask:
            webbrowser.open_new_tab("https://www.digi24.ro/")
            speak('Here are some headlines from the Diji 24.')
            time.sleep(10)

        elif 'search' in userTask:
            userTask = userTask.replace("search", "")
            webbrowser.open_new_tab(userTask)
            time.sleep(10)

        elif 'capital' in userTask:
            speak('I can tell the capitals of the countries in the whole world. What country?')
            country_name = takeATask()
            with open('capitals.json') as capitals:
                data_capitals = json.load(capitals)
                response = data_capitals[country_name]
            speak(f"The capital of {country_name} is {response}")
            time.sleep(3)

        elif 'math' in userTask:
            speak('I can solve basic math problems')
            speak('what question do you want to ask now?')
            question = takeATask()
            speak('It takes me a while, wait')
            client = wolframalpha.Client('R2K75H-7ELALHR35X')
            res = client.query(question)
            answer = next(res.results).text
            speak(answer)
            print(answer)
            time.sleep(5)

        elif "goodbye" in userTask or "ok bye" in userTask or "stop" in userTask or "bye" in userTask:
            speak('your voice assistant Freida is shutting down, Good bye')
            print('your voice assistant Freida is shutting down, Good bye')
            return 0

        elif "shutdown" in userTask:
            speak("Ok, your machine will shut down in 10 seconds. Exit from all applications.")
            subprocess.call(["shutdown", "/l"])


time.sleep(5)
