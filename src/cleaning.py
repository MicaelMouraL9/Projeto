# src/cleaning.py
import pandas as pd

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    print("Cleaning data...")

    # Remove duplicados
    df = df.drop_duplicates()

    # Preencher valores nulos simples
    df = df.fillna(method="ffill")

    print("Cleaning done!")
    return df

if __name__ == "__main__":
    from fetch_data import load_data
    df = load_data()
    print(clean_data(df).head())
