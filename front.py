import streamlit as st
import speech_recognition as sr

def recognize_speech():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()

    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        st.write("Listening...")

        try:
            audio = recognizer.listen(source, timeout=5)
            text = recognizer.recognize_google(audio)
            return text
        except sr.WaitTimeoutError:
            return "Timeout: No speech detected"
        except sr.UnknownValueError:
            return "Error: Unable to recognize speech"
        except Exception as e:
            return f"Error: {str(e)}"

st.title("Real-time Voice Recognition")

st.write("Click the button below and speak into your microphone.")

if st.button("Start Recording"):
    text = recognize_speech()
    st.write("Recognized Text:")
    st.write(text)
