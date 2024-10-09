import streamlit as st
from utiles import generate_with_openai, doanload_image


api_key = st.sidebar.text_input('Your APIKey')
prompt = st.text_input('Dessinez une image ...')

if st.button('Envoyer'):

    image_url = generate_with_openai(prompt, api_key)
    doanload_image(image_url, prompt.replace(' ', '-')+'.jpeg')
    st.image(image_url)


