import speech_recognition as sr
import gtts


r = sr.Recognizer()

def get_audio():
    with sr.Microphone() as source:
        print("Say something...")
        audio = r.listen(source)
    return audio

def audio_to_text(audio):
    text = ""
    try:
        text = r.recognize_google(audio)
    except sr.UnknownValueError:
        print("Speak Again!")
    except sr.RequestError:
        print("Could not request results from API")
    except Exception as e:
        print(e)
    return text

if __name__ == "__main__":

    a = get_audio()
    command = audio_to_text(a)
    print(command)