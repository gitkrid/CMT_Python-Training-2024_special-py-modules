# !pip install streamlit
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np


st.title("Einfaches Streamlit Programm")

user_input = st.text_input("Gib deinen Namen ein")

# Button erstellen und prüfen ob geklickt in einem!
if st.button("Senden"):
    st.write(f"Hallo, {user_input}! Willkommen bei Streamlit.")

    x = np.linspace(0, 4, 50)
    y = np.sin(x*np.pi)

    # Diagramm mit Matplotlib
    fig, ax = plt.subplots()
    ax.plot(x, y)
    ax.set(title="Sinuskurve", xlabel="x-Werte", ylabel="sin(x * pi)")

    # Zeige das Diagramm in Streamlit an
    st.pyplot(fig)
