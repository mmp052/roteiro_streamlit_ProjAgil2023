import streamlit as st

st.title("Roteiro 1: Primeiros Passos com Streamlit")

input = st.text_input('Digite seu nome')
if st.button("Clique-me"):
    st.write('nome:',input)
