import streamlit as st
import hashlib
import pandas as pd
from datetime import datetime

# -----------------------------
# CONFIGURACIÓN GENERAL
# -----------------------------
st.set_page_config(page_title="Linux Challenge", page_icon="🐧")

# Inicializar estado
if "nivel" not in st.session_state:
    st.session_state.nivel = 1

if "nombre" not in st.session_state:
    st.session_state.nombre = ""

# -----------------------------
# FUNCIONES
# -----------------------------
def hash_text(text):
    return hashlib.sha256(text.encode()).hexdigest()

def guardar_progreso(nombre, nivel):
    data = {
        "Nombre": nombre,
        "Nivel": nivel,
        "Fecha": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    df = pd.DataFrame([data])
    try:
        historial = pd.read_csv("progreso.csv")
        historial = pd.concat([historial, df], ignore_index=True)
    except:
        historial = df
    historial.to_csv("progreso.csv", index=False)

# -----------------------------
# HEADER
# -----------------------------
st.title("🐧 Linux Challenge - Escape Room")
st.markdown("Completa los retos en tu terminal Linux y desbloquea niveles 🔓")

# -----------------------------
# LOGIN SIMPLE
# -----------------------------
if st.session_state.nombre == "":
    nombre = st.text_input("Ingresa tu nombre para comenzar:")
    if st.button("Iniciar"):
        if nombre.strip() != "":
            st.session_state.nombre = nombre
            st.rerun()
    st.stop()

st.success(f"Bienvenido {st.session_state.nombre} 👨‍💻")

# Barra de progreso
st.progress(st.session_state.nivel / 5)

# -----------------------------
# NIVELES
# -----------------------------

# NIVEL 1
if st.session_state.nivel == 1:
    st.header("🔍 Nivel 1: Navegación")

    st.markdown("""
    Encuentra un archivo oculto en tu sistema llamado `.secreto`  
    y muestra su contenido.

    📌 La clave es el contenido del archivo.
    """)

    respuesta = st.text_input("Ingresa la clave:")

    if st.button("Validar Nivel 1"):
        if respuesta == "linux123":
            st.success("✅ Correcto! Nivel 2 desbloqueado")
            st.session_state.nivel = 2
            guardar_progreso(st.session_state.nombre, 2)
            st.rerun()
        else:
            st.error("❌ Incorrecto, intenta nuevamente")

# NIVEL 2
elif st.session_state.nivel == 2:
    st.header("🔐 Nivel 2: Permisos")

    st.markdown("""
    Existe un archivo llamado `bloqueado.txt` sin permisos de lectura.  
    Debes cambiar sus permisos para poder leerlo.

    📌 La clave es el contenido del archivo.
    """)

    respuesta = st.text_input("Clave:")

    if st.button("Validar Nivel 2"):
        if respuesta == "permisos_ok":
            st.success("✅ Nivel 3 desbloqueado")
            st.session_state.nivel = 3
            guardar_progreso(st.session_state.nombre, 3)
            st.rerun()
        else:
            st.error("❌ Respuesta incorrecta")

# NIVEL 3
elif st.session_state.nivel == 3:
    st.header("📂 Nivel 3: Búsqueda")

    st.markdown("""
    Busca en el sistema un archivo que contenga la palabra **"cisco"**.

    📌 La clave es el nombre del archivo.
    """)

    respuesta = st.text_input("Clave:")

    if st.button("Validar Nivel 3"):
        if respuesta.lower() == "cisco.txt":
            st.success("✅ Nivel 4 desbloqueado")
            st.session_state.nivel = 4
            guardar_progreso(st.session_state.nombre, 4)
            st.rerun()
        else:
            st.error("❌ Intenta nuevamente")

# NIVEL 4
elif st.session_state.nivel == 4:
    st.header("📦 Nivel 4: Compresión")

    st.markdown("""
    Descomprime un archivo llamado `backup.tar.gz`.

    📌 Dentro encontrarás un archivo con la clave.
    """)

    respuesta = st.text_input("Clave:")

    if st.button("Validar Nivel 4"):
        if respuesta == "backup_done":
            st.success("✅ Nivel 5 desbloqueado")
            st.session_state.nivel = 5
            guardar_progreso(st.session_state.nombre, 5)
            st.rerun()
        else:
            st.error("❌ Incorrecto")

# NIVEL 5
elif st.session_state.nivel == 5:
    st.header("🤖 Nivel 5: Script Bash")

    st.markdown("""
    Crea un script en bash que imprima:

    ```bash
    echo "Linux Master"
    ```

    📌 Ejecuta el script y escribe el resultado.
    """)

    respuesta = st.text_input("Clave final:")

    if st.button("Finalizar"):
        if respuesta == "Linux Master":
            st.balloons()
            st.success("🎉 FELICIDADES! Has completado el Linux Challenge")
            guardar_progreso(st.session_state.nombre, "FINAL")
        else:
            st.error("❌ Aún no es correcto")

# -------------------------
