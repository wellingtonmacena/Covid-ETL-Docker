import os
import pandas as pd
from datetime import datetime

def extract_data():
    # Criar nome do arquivo com data
    timestamp = datetime.now().strftime("%Y-%m-%d")
    filename = f"data/covid_data_{timestamp}.csv"

    # Verificar se já existe
    if os.path.exists(filename):
        print(f"Arquivo já existe: {filename}")
        return filename

    # Caso não exista, faz o download
    url = "https://catalog.ourworldindata.org/garden/covid/latest/compact/compact.csv"
    covid_data = pd.read_csv(url)

    # Salvar CSV
    covid_data.to_csv(filename, index=False)
    print(f"Dados COVID-19 extraídos e salvos em '{filename}'")

    return filename
