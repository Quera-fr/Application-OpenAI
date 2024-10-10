import streamlit as st
from openai import OpenAI
from utiles import speech_to_text, text_to_speech


api_key = st.sidebar.text_input("Api Key")
audio = st.experimental_audio_input('Traducteur automatique')

if audio is not None:

    transcription = speech_to_text(audio, api_key)
    audio_speech = text_to_speech(transcription, api_key)
    
    st.audio(audio_speech, autoplay=True)