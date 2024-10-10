import streamlit as st
from utiles import PromptEngineering


###### Entrainement d'un modèle OpenAI  #########

api_key = st.sidebar.text_input("Your APIKey")
promtengine = PromptEngineering(api_key=api_key)

if st.checkbox('Entrainement du modèle'):
    uploaded_file = st.file_uploader("Choose a file")
    if uploaded_file is not None:
        promtengine.fine_tuning(uploaded_file)


######   Utilisation d'un modèle entrainé #########

if st.checkbox('Utilisation du modèle finetuné'):

    dict_models = promtengine.show_models()
    list_models = dict_models.keys()
    
    st.sidebar.write(dict_models)
    
    model = st.selectbox('Choisissez votre modèle : ', list_models)
    prompt = st.text_input('Tape your text', "Comment peut-tu m'aider ?")

    if st.button("Envoyer votre prompt"):
        response = promtengine.use_finetuned_model(model, prompt=prompt)
        st.write(response)