import streamlit as st
from utiles import Proccessing


dict_func = {
    "Traduction": Proccessing().trad_with_openai,
    "Code Correction": Proccessing().code_corector,
}

key_funct = st.selectbox("Choisissez une fonction", list(dict_func.keys()))



openai_key = st.sidebar.text_input("Entez votre clé OpenAI")
prompt = st.text_input("Entez votre texte")


if st.button("Envoyer"):
    process = Proccessing()
    st.write(dict_func[key_funct](prompt, openai_key))