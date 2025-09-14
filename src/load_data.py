
import pandas as pd
from sqlalchemy import create_engine
from transform_data import get_transformed_data
def load_data():
    df = get_transformed_data()
    engine = create_engine("postgresql://user:password@localhost:5432/postgres")

    df.to_sql("covid_stats", engine, if_exists="replace", index=False)

    print("Data inserted into Postgres successfully!")
    return df