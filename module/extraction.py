from dotenv import load_dotenv
import pandas as pd
import os
import requests

# Carregar variáveis do arquivo .env
load_dotenv()

# URL da API
url = 'https://redcap.fiocruz.br/redcap/api/'

# Cria o dicionário de tokens e reports
tokens_report_ids = {
    os.getenv('TOKEN_1'): [{'report_id': 14319}],
}

# Cria um dicionário de dataframes
dataframes = {}

# Faz um loop for para iterar sobre os reports e fazer as requests
for token, reports in tokens_report_ids.items():
    for report in reports:

        data = {
            'token': token,
            'content': 'report',
            'format': 'json',
            'report_id': report['report_id'],
            'rawOrLabel': 'raw',
            'rawOrLabelHeaders': 'raw',
            'exportCheckboxLabel': 'false',
            'exportSurveyFields': 'false',
            'exportDataAccessGroups': 'false',
            'returnFormat': 'json'
        }

        response = requests.post(url, data=data)
        if response.status_code == 200:
            df = pd.DataFrame(response.json())
            dataframes[report['report_id']] = df 
        else:
            print(f"Failed to get data for report_id: {report['report_id']}")

# Confere se os reports estão no dicionário
for report_id, df in dataframes.items():
    print(f"Report ID: {report_id}")

# Atribui os reports a dataframes específicos para manipulação
def carregar_dataframe():
    df = dataframes[14319]
    return df
