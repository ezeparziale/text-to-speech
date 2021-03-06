import streamlit as st
import pyttsx3
from datetime import datetime

engine = pyttsx3.init()

st.title("Text to speech")
text = st.text_input("Texto", "Hola! como estas?", help="Texto a reproducir")
rate = st.slider("Velocidad", 0, 500, 145, help="Velocidad de reproducción")
volume = st.slider("Volumen", 0, 100, 80, help="Volumen del audio")
guardar = st.checkbox("Guardar")


if st.button("Hablar"):
    engine.setProperty("voice", "spanish")
    engine.setProperty("rate", rate)
    engine.setProperty("volume", volume / 100)
    engine.say(text)
    engine.runAndWait()
    engine.stop()

    if guardar:
        curr_dt = datetime.now()
        file_name = int(round(curr_dt.timestamp()))
        engine.save_to_file(text, f"export\{file_name}.mp3")
        engine.runAndWait()

        with open(f"export\{file_name}.mp3", "rb") as file:
            btn = st.download_button(
                label="Download audio", data=file, file_name=f"{file_name}.mp3"
            )
