# src/fetch_data.py
import pandas as pd
import os

def load_data():
    # Caminho absoluto relativo à raiz do projeto

    base_dir = os.path.dirname(os.path.dirname('raw.csv'))  # sobe de src/ para raiz
    csv_path = r"C:\Users\Admin\Documents\CURSO\Atividades_806\10806\Atividade3\Grupo6"

    
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV não encontrado: {csv_path}")
    
    df = pd.read_csv(csv_path)
    print("Dataset carregado do CSV")
    return df

if __name__ == "__main__":
    df = load_data()
    print(df.head())
