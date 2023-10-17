import streamlit as st

st.title("Roteiro 2: Widgets Interativos")

value = st.slider("Escolha um valor", 0, 100)
check = st.checkbox('Voce xekou?')
togle = st.toggle('Voce togou?')
radio = st.radio('Qual teu time',('vasco','mengo'))
select = st.selectbox('Qual é melhor',('vasco','mengo'))
if st.button("Mostrar valor do slider"):
    st.write(f"Valor escolhido: {value,check,togle,radio,select}")
