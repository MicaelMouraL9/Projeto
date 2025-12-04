# src/dashboard.py
from dash import Dash, html, dcc
from .cleaning import clean_data
from .fetch_data import load_data
from .analysis import create_sample_plot

def create_dashboard():
    df=clean_data(load_data())
    fig=create_sample_plot(df)

    app = Dash(__name__)

    app.layout = html.Div([
        html.H1("CSV Dataset Test Dashboard"),
        html.P("Ligação testada com CSV + Plotly + Dash"),
        dcc.Graph(figure=fig)
    ])

    return app