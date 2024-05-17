# pip install streamlit
# Programm starten via:
# $ streamlit run [name]
import streamlit as st


# Titel der Anwendung
st.title("Einfaches Streamlit Programm")

# Text-Eingabebox hinzu
user_input = st.text_input("Gib deinen Namen ein")

# Button erstellen und prüfen ob geklickt in einem!
if st.button("Senden"):
    st.write(f"Hallo, {user_input}! Willkommen bei Streamlit.")
