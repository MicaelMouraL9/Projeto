# src/fetch_data.py
import pandas as pd
import os

def load_data():
    # Caminho absoluto relativo à raiz do projeto
    base_dir = os.path.dirname(os.path.dirname('raw.csv'))  # sobe de src/ para a raiz
    csv_path = os.path.join(base_dir, "data", "raw", "ds.csv")
    
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV não encontrado: {csv_path}")
    
    df = pd.read_csv(csv_path)
    print("Dataset carregado do CSV")
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())
