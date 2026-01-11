import streamlit as st

def vigenere_encrypt(plaintext, key):
    plaintext = ''.join(filter(str.isalpha, plaintext)).upper()
    key = key.upper()
    if not key:
        raise ValueError("Kunci tidak boleh kosong!")
    ciphertext = ''
    key_index = 0
    for char in plaintext:
        shift = ord(key[key_index % len(key)]) - ord('A')
        encrypted_char = chr((ord(char) - ord('A') + shift) % 26 + ord('A'))
        ciphertext += encrypted_char
        key_index += 1
    return ciphertext

def vigenere_decrypt(ciphertext, key):
    ciphertext = ''.join(filter(str.isalpha, ciphertext)).upper()
    key = key.upper()
    if not key:
        raise ValueError("Kunci tidak boleh kosong!")
    plaintext = ''
    key_index = 0
    for char in ciphertext:
        shift = ord(key[key_index % len(key)]) - ord('A')
        decrypted_char = chr((ord(char) - ord('A') - shift) % 26 + ord('A'))
        plaintext += decrypted_char
        key_index += 1
    return plaintext

st.set_page_config(page_title="Vigenère Cipher", page_icon="🔒", layout="wide")
st.title("🔒 Vigenère Cipher (Web)")

col1, col2 = st.columns(2)

with col1:
    st.subheader("Input")
    mode = st.radio("Mode", ["Encrypt", "Decrypt"], horizontal=True)
    message = st.text_area("Message", height=200)
    key = st.text_input("Key (A–Z only)")
    run = st.button("Run")

with col2:
    st.subheader("Output")
    output_placeholder = st.empty()

if run:
    if not key:
        st.warning("Masukkan key dulu.")
    elif not message.strip():
        st.warning("Masukkan pesan dulu.")
    else:
        try:
            if mode == "Encrypt":
                result = vigenere_encrypt(message, key)
            else:
                result = vigenere_decrypt(message, key)
            output_placeholder.code(result)
        except Exception as e:
            st.error(str(e))
