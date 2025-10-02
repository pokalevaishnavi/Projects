import os
import speech_recognition as sr
from openai import OpenAI
import pyaudio
import win32com.client
import webbrowser
import datetime
from config import OPENAI_API_KEY
import tkinter as tk
from tkinter import scrolledtext, Entry, Button, END

# Initialize OpenAI client
client = OpenAI(api_key=OPENAI_API_KEY)

# Initialize TTS
speaker = win32com.client.Dispatch("SAPI.SpVoice")
is_speaking = False  # Flag to control speaking process

# Global chat history
messages = [{"role": "system", "content": "You are a helpful voice assistant."}]


def say(text):
    global is_speaking
    is_speaking = True
    speaker.Speak(text)
    is_speaking = False


def chat(query):
    """Chat with memory (text only)"""
    global messages
    messages.append({"role": "user", "content": query})

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        temperature=1,
        max_tokens=256,
    )

    reply = response.choices[0].message.content.strip()
    messages.append({"role": "assistant", "content": reply})
    return reply


def chat2(query):
    """Chat with memory (with speech output)"""
    reply = chat(query)
    say(reply)
    return reply


def ai(prompt):
    """Handle AI response and save to file"""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            max_tokens=256,
        )

        reply = response.choices[0].message.content.strip()
        text = f"OpenAI response for Prompt: {prompt}\n*********************\n\n{reply}"

        save_response(prompt, text)

        if len(reply) < 150:
            say(reply)
        else:
            say("Done! Look into responses please")

    except Exception as e:
        print(f"An error occurred: {e}")
        say("Sorry, I encountered an error. Please try again.")


def save_response(prompt, text):
    index = prompt.lower().find("using ai")
    if index != -1:
        filename = prompt[index + len("using ai"):].strip()
    else:
        filename = "response"

    filename = ''.join(char for char in filename if char.isalnum())[:20]

    if not os.path.exists("Responses"):
        os.makedirs("Responses")

    with open(os.path.join("Responses", f"{filename}.txt"), "w", encoding="utf-8") as f:
        f.write(text)


def takeCommand():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
        try:
            print("Recognizing..")
            query = r.recognize_google(audio, language="en-in")
            print(f"User said: {query}")
            return query.lower()
        except Exception:
            return "Some error occurred. Sorry from Assistant"


def open_website(query):
    sites = {
        "youtube": "https://youtube.com",
        "google": "https://google.com",
        "wikipedia": "https://wikipedia.com"
    }

    for site in sites:
        if site in query:
            say(f"Opening {site}")
            webbrowser.open(sites[site])
            return True
    return False


def open_app(query):
    apps = {
        "vs code": "C:\\Users\\Dell\\Desktop\\Visual Studio Code.lnk",
        "notepad": "C:\\Windows\\notepad.exe",
        "microsoft word": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Word.lnk",
        "microsoft powerpoint": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\PowerPoint.lnk",
        "microsoft excel": "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Excel.lnk",
        "oracle virtual box": "C:\\Users\\Public\\Desktop\\Oracle VM VirtualBox.lnk",
        "zoom": "C:\\Users\\Dell\\Desktop\\Zoom.lnk",
        "dosbox": "C:\\Users\\Public\\Desktop\\DOSBox 0.74-3.lnk",
        "turbo c": "C:\\Users\\Dell\\Desktop\\TurboC++ for Windows 7.lnk"
    }

    for app in apps:
        if app in query:
            say(f"Opening {app}")
            os.startfile(apps[app])
            return True
    return False


def chat_box():
    window = tk.Tk()
    window.title("Voice Assistant")
    window.geometry("600x514")

    lbl = tk.Label(window, text="Ask Assistant:")
    lbl.grid(column=0, row=0)

    txt = Entry(window, width=68)
    txt.grid(column=1, row=0)

    txt_output = scrolledtext.ScrolledText(window, width=72, height=30)
    txt_output.grid(column=0, row=1, columnspan=4)

    def clicked():
        user_input = txt.get()
        txt.delete(0, END)
        reply = chat(user_input)
        txt_output.insert(END, f"User: {user_input}\nAssistant: {reply}\n")

    def clear_text():
        txt_output.delete(1.0, END)

    def voice_command():
        query = takeCommand()
        reply = chat(query)
        txt_output.insert(END, f"User: {query}\nAssistant: {reply}\n")

    btn = Button(window, text="Ask", command=clicked)
    btn.grid(column=2, row=0)

    btn_clear = Button(window, text="Clear", command=clear_text)
    btn_clear.grid(column=3, row=0)

    btn_voice = Button(window, text="Voice Command", command=voice_command)
    btn_voice.grid(column=0, row=0)

    window.mainloop()


def main():
    say("Hello")
    while True:
        query = takeCommand()

        if "open music" in query:
            music_path = "C:\\Users\\Dell\\Music\\Mera-man.mp3"
            say("Opening music")
            os.startfile(music_path)

        elif "the time" in query:
            current_time = datetime.datetime.now().strftime("%H:%M")
            say(f"The time is {current_time}")

        elif "open" in query and open_website(query):
            continue

        elif "open" in query and open_app(query):
            continue

        elif "using ai" in query:
            ai(query)

        elif "open chat box" in query:
            chat_box()

        elif "quit chat" in query:
            exit()

        elif "reset chat" in query:
            global messages
            messages = [{"role": "system", "content": "You are a helpful voice assistant."}]
            say("Chat has been reset")

        else:
            chat2(query)


if __name__ == '__main__':
    main()
