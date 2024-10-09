import streamlit as st
from utiles import analyse_img_by_gpt, create_variation_with_openai, doanload_image
from openai import OpenAI

api_key = st.sidebar.text_input('Your APIKey')

uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:

    bytes_data = uploaded_file.read()
    st.image(bytes_data)

    if st.button("Démmarer l'analyse"):
        text = analyse_img_by_gpt(bytes_data, api_key)
        st.write(text)
        
    
    if st.button("Création d'une variation"):
        image_url = create_variation_with_openai(bytes_data, api_key)
        st.image(image_url)


        doanload_image(image_url, 'img.png')

        with open('img.png', "rb") as file:
            btn = st.download_button(
                label="Download image",
                data=file,
                file_name="flower.png",
                mime="image/png",
            )

        
   