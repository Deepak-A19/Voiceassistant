import speech_recognition as sr
import pyttsx3
import datetime
import webbrowser
import pyaudio

def greet():
    return "Hello! How can I assist you today?"

def get_time():
    current_time = datetime.datetime.now().strftime("%H:%M")
    return f"The current time is {current_time}"

def get_date():
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    return f"Today's date is {current_date}"

def search_web(query):
    url = f"https://www.google.com/search?q={query}"
    webbrowser.open(url)
    return f"Searching the web for {query}"

def respond(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

def voice_assistant():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Say something...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print("You said:", command)

            if "hello" in command:
                response = greet()
            elif "time" in command:
                response = get_time()
            elif "date" in command:
                response = get_date()
            
            elif "search" in command:
                search_phrase = "search for"
                if search_phrase in command:
                    query = command.split(search_phrase)[1].strip()
                    response = search_web(query)
                else:
                    response = "Please provide a search query after 'search for'."

            else:
                response = "I'm sorry, I didn't understand that."

            print(response)
            respond(response)

        except sr.UnknownValueError:
            print("Sorry, I couldn't understand your voice.")
        except sr.RequestError as e:
            print(f"Could not request results from Google Speech Recognition service; {e}")

if __name__ == "__main__":
    voice_assistant()
