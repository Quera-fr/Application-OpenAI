import streamlit as st
from utiles import PromptEngineering, page

page('Whisper')

api_key = st.sidebar.text_input("Api Key")
promtengine = PromptEngineering(api_key=api_key)
audio = st.experimental_audio_input('Traducteur automatique')

if audio is not None:
    transcription = promtengine.speech_to_text(audio)
    audio_speech = promtengine.text_to_speech(transcription)
    st.audio(audio_speech, autoplay=True)