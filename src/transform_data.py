import pandas as pd
import os
import glob


def get_transformed_data():

    # Selecionar colunas
    cols = ["country", "date", "continent", "code", "new_cases", "new_deaths", "population"]
    df = get_latest_data()
    
    df = df[cols]
    
    # Filtrar países
    df = df[df["country"].isin(["Brazil", "United States", "India", "Russia", "France", "United Kingdom", "Italy", "Spain", "Germany", "Argentina"])]

    df["cases_per_100k"] = df["new_cases"] / df["population"] * 100000
    df["deaths_per_100k"] = df["new_deaths"] / df["population"] * 100000

    # Ajustar formato de data
    df["date"] = pd.to_datetime(df["date"])
    df = df.sort_values(by=["country", "date"])

    return df


def get_latest_data():

# Path to the directory
    directory = "data/"

    # Get all CSV files in the directory
    files = glob.glob(os.path.join(directory, "*.csv"))

    # Find the latest file based on creation time
    latest_file = max(files, key=os.path.getctime)

    print(f"The latest file is: {latest_file}")

    latest_data = pd.read_csv(latest_file)
    return latest_data

