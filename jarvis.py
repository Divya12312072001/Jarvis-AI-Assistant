import tkinter as tk
import speech_recognition as sr
import pyttsx3
import wikipedia
import datetime
import webbrowser
import os
import threading
import random

engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

def add_history(text):
    history_box.insert(tk.END, text + "\n")
    history_box.see(tk.END)

def listen():

    r = sr.Recognizer()

    with sr.Microphone() as source:
        status_label.config(text="Listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)

    try:
        command = r.recognize_google(audio)
        command = command.lower()

        status_label.config(text="You said: " + command)
        add_history("You: " + command)

        if "time" in command:
            time = datetime.datetime.now().strftime("%H:%M")
            speak("The current time is " + time)
            add_history("Jarvis: Time is " + time)

        elif "open youtube" in command:
            speak("Opening YouTube")
            webbrowser.open("https://youtube.com")

        elif "open google" in command:
            speak("Opening Google")
            webbrowser.open("https://google.com")

        elif "open wikipedia" in command:
            speak("Opening Wikipedia")
            webbrowser.open("https://www.wikipedia.org")

        elif "play song" in command:
            speak("Playing song on YouTube")
            webbrowser.open("https://www.youtube.com/results?search_query=latest+song")

        elif "calculator" in command:
            speak("Opening calculator")
            os.system("calc")

        elif "notepad" in command:
            speak("Opening notepad")
            os.system("notepad")

        elif "tell about" in command:
            topic = command.replace("tell about", "")
            speak("Searching Wikipedia for " + topic)

            try:
                result = wikipedia.summary(topic, sentences=2)
                speak(result)
                add_history("Jarvis: " + result)
            except:
                speak("Sorry I could not find information")

        elif "stop" in command:
            speak("Goodbye")
            window.quit()

    except:
        status_label.config(text="Didn't understand")


def start_listening():
    threading.Thread(target=listen).start()


# GUI Window
window = tk.Tk()
window.title("Jarvis AI Assistant")
window.geometry("700x550")
window.configure(bg="black")

title = tk.Label(window,
                 text="JARVIS AI ASSISTANT",
                 font=("Arial",22,"bold"),
                 fg="cyan",
                 bg="black")
title.pack(pady=10)

# Voice Wave Animation
canvas = tk.Canvas(window,width=220,height=120,bg="black",highlightthickness=0)
canvas.pack()

bars=[]
for i in range(10):
    bar=canvas.create_rectangle(20*i+10,100,20*i+20,100,fill="cyan")
    bars.append(bar)

def animate():
    for bar in bars:
        height=random.randint(20,100)
        canvas.coords(bar,canvas.coords(bar)[0],height,canvas.coords(bar)[2],100)
    window.after(200,animate)

animate()

# Mic Button
mic_button = tk.Button(window,
                       text="🎤",
                       font=("Arial",40),
                       command=start_listening,
                       bg="black",
                       fg="cyan",
                       borderwidth=0)

mic_button.pack(pady=20)

status_label = tk.Label(window,
                        text="Click mic and speak",
                        font=("Arial",14),
                        fg="white",
                        bg="black")
status_label.pack()

# Command History
history_title = tk.Label(window,
                         text="Command History",
                         font=("Arial",14,"bold"),
                         fg="cyan",
                         bg="black")
history_title.pack(pady=5)

history_box = tk.Text(window,
                      height=8,
                      width=60,
                      bg="black",
                      fg="white",
                      insertbackground="white")
history_box.pack()

speak("Hello Divya, I am your Jarvis assistant")

window.mainloop()