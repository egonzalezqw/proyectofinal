import streamlit as st

st.title("Linux Challenge 🚀")

nivel = st.session_state.get("nivel", 1)

if nivel == 1:
    st.header("Nivel 1: Navegación")
    respuesta = st.text_input("Ingresa la clave:")

    if respuesta == "linux123":
        st.success("Correcto! Nivel 2 desbloqueado 🔓")
        st.session_state["nivel"] = 2

elif nivel == 2:
    st.header("Nivel 2: Permisos")
