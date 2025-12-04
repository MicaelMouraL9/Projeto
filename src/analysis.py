# src/analysis.py
import plotly.express as px
import pandas as pd

def create_sample_plot(df: pd.DataFrame):
    print("Creating visualization...")

    numeric_cols = df.select_dtypes(include="number").columns

    if len(numeric_cols) == 0:
        raise ValueError("No numeric columns found for plotting.")

    fig = px.bar(df, x=numeric_cols[0], title=f"Distribution of {numeric_cols[0]}")
    return fig

if __name__ == "__main__":
    from cleaning import clean_data
    from fetch_data import load_data

    df = clean_data(load_data())
    fig = create_sample_plot(df)
    fig.show()
