import streamlit as st
from utiles import page

# Configuration de la page
page(title="Présentation des Fonctionnalités de Streamlit")

# Titre de la page
st.title("Présentation de Streamlit")

# Sous-titre
st.subheader("Explorez les principales fonctionnalités")

# Introduction
st.write("""
Streamlit est un framework Python qui permet de créer des applications web interactives simplement et rapidement. 
Voici un aperçu des principales fonctionnalités que vous pouvez utiliser dans vos applications Streamlit :
""")

# Exemple de code
st.write("""
### Exemple de code avec Streamlit
Vous pouvez utiliser du code Python pour créer des interfaces utilisateurs dynamiques. Par exemple :
```python
import streamlit as st
st.title("Ma première application Streamlit")
```
""")

# Champ de saisie
nom = st.text_input("Entrez votre nom", "Tapez ici...")

# Bouton interactif
if st.button("Afficher le nom"):
    st.write(f"Bonjour, {nom} !")

# Slider
age = st.slider("Quel est votre âge ?", 0, 100, 25)
st.write(f"Votre âge est de {age} ans.")

# Checkbox
if st.checkbox("Afficher plus d'informations"):
    st.write("Streamlit permet également d'ajouter des widgets interactifs comme les cases à cocher, les boutons, etc.")

# Colonnes
col1, col2 = st.columns(2)

with col1:
   # Image
    st.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmrJJS51aimdKyh_eNLrzG21MzoVOYgoHeUQ&s")
    

with col2:
    # Vidéo YouTube
    st.video("https://www.youtube.com/watch?v=GsZhStn1OgI")

# Sidebar
st.sidebar.title("Fonctionnalités supplémentaires")
st.sidebar.write("Explorez les options dans la barre latérale pour plus de contenus.")

 # Selectbox
langue = st.sidebar.selectbox("Sélectionnez votre langue : ", ["Français", "Anglais", "Espagnol"])
st.sidebar.write(f"Langue sélectionnée : {langue}")

# Section de code avec explication
st.write("""
### Correction d'erreur courante :
Si vous souhaitez afficher "Hello" en Python, utilisez la commande suivante :
```python
print("Hello")
```
""")