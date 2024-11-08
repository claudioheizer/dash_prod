import streamlit as st
from modules import processar_dados

st.title("Dashboard de Dados Processados")

# Carrega e processa os dados
df_processado = processar_dados()

# Verifica se o DataFrame foi processado com sucesso
if df_processado is not None:
    st.write("Dados processados com sucesso!")
    st.dataframe(df_processado.head())
else:
    st.write("Erro ao processar os dados.")

