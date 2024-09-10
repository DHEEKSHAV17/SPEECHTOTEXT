import speech_recognition as sr

def live_speech_to_text():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Adjusting microphone for ambient noise... Please wait.")
        recognizer.adjust_for_ambient_noise(source, duration=2)
        print("Microphone adjusted, you can speak now...")

        while True:
            try:
                print("Listening...")
                audio = recognizer.listen(source)

                print("Recognizing...")
                text = recognizer.recognize_sphinx(audio)  # For offline
                print(f"Recognized text: {text}")

            except sr.UnknownValueError:
                print("Sorry, I could not understand the audio.")
            except sr.RequestError as e:
                print(f"Recognition error: {e}")
            except KeyboardInterrupt:
                print("Stopping the live speech-to-text process.")
                break

if __name__ == "__main__":
    live_speech_to_text()
