import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
listener= sr.Recognizer()
engine=pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.say('I am your dora ')
engine.say('What can I do for you')
engine.runAndWait()
def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print('listening....')
            voice=listener.listen(source)
            command=listener.recognize_google(voice)
            command=command.lower()
            if 'dora' in command:
                command=command.replace('dora','')
                print(command)
    except:
        pass
    return command
def run_dora():
    command=take_command()
    print(command)
    if 'play' in command:
        song=command.replace('play','')
        talk('playing'+song)
        print('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time' in command:
        time=datetime.datetime.now().strftime('%I:%M %p')
        print(time)
        talk('current time is'+time)
    elif 'tell me about ' in command:
        person=command.replace('tell me about ','')
        info= wikipedia.summary(person,2)
        print(info)
        talk(info)
    elif 'joke ' in command:
        talk(pyjokes.get_joke())
    elif 'date' in command:
        talk('sorry,i hava headache')
    elif 'single' in command:
        talk('i am happy to say i feel whole all on my own , plus, i never have to share dessert')
    elif 'stop' in command:
        talk("Okay, stopping the song.")
    elif 'thank you' in command:
        talk("You're welcome. How can I assist you further?")
    elif 'goodbye' in command:
        talk("Goodbye. Have a great day!")
    else:
        talk("I'm sorry, I didn't understand that. Could you please repeat?")

while True:
    run_dora()