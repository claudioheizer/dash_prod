import pandas as pd 
import numpy as np
import streamlit as st

df.rename(columns={
    'puerp_hosp': 'Código',
    'puerp_macro': 'Macrorregião',
    'puerp_lu_1': 'Data1',
    'pront_bl18_280_2': 'Data2'
}, inplace=True)


st.write("""# Dashboard de Controle de Produção""")

# # Carrega e processa os dados
# df_processado = processar_dados()

# # Verifica se o DataFrame foi processado com sucesso
# if df_processado is not None:
#     st.write("Dados processados com sucesso!")
#     st.dataframe(df_processado.head())
# else:
#     st.write("Erro ao processar os dados.")

