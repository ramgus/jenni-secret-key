import streamlit as st
import base64
import hashlib

# Website A: Key Generation Utility
st.title("generador de llave secreta")

# Ask user for passphrase input
passphrase = st.text_input("como te tengo guardada de contacto?:", type="password")

if st.button("generar"):
    if passphrase:
        # Derive a 256-bit key from the passphrase
        salt = b'this is my salt!'  # Use a fixed salt to ensure consistency
        kdf = hashlib.pbkdf2_hmac('sha256', passphrase.encode(), salt, 100000, dklen=32)
        key = base64.urlsafe_b64encode(kdf).decode()
        st.write("Derived Key:")
        st.code(key, language='plaintext')
    else:
        st.error("nope.")
