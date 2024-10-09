import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Dawan - AppWeb",
    page_icon="🧊",
    layout="centered",
    initial_sidebar_state="auto",
)

# Configure the title of the page
st.title("Dawan - AppWeb")

# Subtitle
st.subheader("Subtitle")


# Text
st.write("""

this is a code block
         ```python
        import streamlit as st
        st.title("Dawan - AppWeb")
            ```
         """)

# Input field
prompt = st.text_input("Enter your name", "Type Here ...")

# Add Boutton
if st.button("Simple Button"):
    st.write(prompt)


# Slider
age = st.slider("Quel est votre age ?", 0, 100, 25)


# Checkbox
if st.checkbox("Show/Hide"):
    st.write("Showing or Hiding widget")


col1, col2 = st.columns(2)

with col1:
    # Selectbox
    st.selectbox("Sélectionnez votre langue : ", ["Français", "Anglais", "Espagnol"])
    
with col2:
    # Video
    st.video("https://www.youtube.com/watch?v=GsZhStn1OgI")

st.sidebar.title("Sidebar")
st.sidebar.image("https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcRmrJJS51aimdKyh_eNLrzG21MzoVOYgoHeUQ&s")


st.write("""It seems like there is an error in the code provided. If you intended to print the word "Hello", the correct syntax in Python would be `print("Hello")`. Here is the corrected version:

```python
print("Hello")
```
         """)