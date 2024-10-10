import streamlit as st
from openai import OpenAI



api_key = st.sidebar.text_input("Your APIKey")
client = OpenAI(
        api_key=api_key
    )


uploaded_file = st.file_uploader("Choose a file")
if uploaded_file is not None:
    # To read file as bytes:
    bytes_data = uploaded_file.read()
    st.write(bytes_data)

    from openai import OpenAI
    client = OpenAI(
        api_key=api_key
    )

    upload_file = client.files.create(
        file=bytes_data,
        purpose="fine-tune"
        )
    
    fine_tuned_model = client.fine_tuning.jobs.create(
            training_file=upload_file.id,
            model="gpt-4o-2024-08-06",
            suffix="Dawan-Test"
            )
    st.write(fine_tuned_model)


#############################

st.title('Utilisation du modèle finetuné')

dict_models = {client.fine_tuning.jobs.list(limit=10).to_dict()['data'][n]['fine_tuned_model']:client.fine_tuning.jobs.list(limit=10).to_dict()['data'][n]['status'] for n in range(10)}
st.write(dict_models)

list_models = [client.fine_tuning.jobs.list(limit=10).to_dict()['data'][n]['fine_tuned_model'] for n in range(10)]
model = st.selectbox('Choisissez votre modèle : ',list_models)

if st.button("Envoyer votre prompt"):
    completion = client.chat.completions.create(
    model=model,
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "What can yo do for me ?"}
    ]
    )
    st.write(completion.choices[0].message.content)

    
                
