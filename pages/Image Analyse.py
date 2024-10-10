import streamlit as st
from utiles import PromptEngineering, page

page('Image Analyse')

api_key = st.sidebar.text_input('Your APIKey')
promtengine = PromptEngineering(api_key=api_key)

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    bytes_data = uploaded_file.read()
    st.image(bytes_data)

    if st.button("Démmarer l'analyse"):
        text = promtengine.analyse_img_by_gpt(bytes_data)
        st.write(text)
    
    if st.button("Création d'une variation"):
        image_url = promtengine.create_variation_with_openai(bytes_data,)
        st.image(image_url)

        promtengine.doanload_image(image_url, 'img.png')

        with open('img.png', "rb") as file:
            btn = st.download_button(
                label="Download image",
                data=file,
                file_name="flower.png",
                mime="image/png",
            )

        
   