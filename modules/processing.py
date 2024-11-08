from .extraction import carregar_dataframe

def processar_dados():
    # Carrega o DataFrame usando a função do módulo extraction
    df = carregar_dataframe()
    
    # Inicia o processamento do DataFrame aqui
    df = df.dropna()
    
    # Retorna o DataFrame processado
    return df
