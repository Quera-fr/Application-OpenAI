import streamlit as st
from utiles import PromptEngineering, page

page('Dall-E')

api_key = st.sidebar.text_input('Your APIKey')
prompt = st.text_input('Dessinez une image ...')

promtengine = PromptEngineering(api_key=api_key)

if st.button('Envoyer'):
    image_url = promtengine.generate_with_openai(prompt)
    promtengine.doanload_image(image_url, prompt.replace(' ', '-')+'.jpeg')
    st.image(image_url)