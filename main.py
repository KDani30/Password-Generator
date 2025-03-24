import streamlit as st
import random
import string

# Función para generar una contraseña segura
def generar_contraseña(longitud, usar_especiales):
    caracteres = string.ascii_letters + string.digits
    if usar_especiales:
        caracteres += string.punctuation

    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

# Interfaz de usuario con Streamlit
st.title("Generador de Contraseñas Seguras")

# Selección de la longitud de la contraseña
longitud = st.slider("Longitud de la contraseña", min_value=8, max_value=20, value=16)

# Opción para incluir caracteres especiales
usar_especiales = st.checkbox("Incluir caracteres especiales", value=True)

# Botón para generar la contraseña
if st.button("Generar Contraseña"):
    contraseña = generar_contraseña(longitud, usar_especiales)
    st.success("Contraseña generada:")
    st.code(contraseña, None)

# Información adicional sobre seguridad
st.markdown("### Consejos para una contraseña segura:")
st.markdown("""
- Usa una longitud mínima de 16 caracteres.
- Incluye una combinación de letras mayúsculas, minúsculas, números y caracteres especiales.
- Evita usar información personal o palabras comunes.
""")
st.markdown("**Para la comprobación de la seguridad de tu contraseña [Visita Kaspersky Password Checker](https://password.kaspersky.com/es/)**")

