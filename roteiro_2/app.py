import streamlit as st

st.title("Roteiro 2: Widgets Interativos")

value = st.slider("Escolha um valor", 0, 100)
if st.button("Mostrar valor do slider"):
    st.write(f"Valor escolhido: {value}")
