import dash
from dash import dcc, html, dash_table
import pandas as pd
import plotly.express as px

# CSV-Datei laden
df = pd.read_csv("lesestellen_daten_updated.csv", sep=";")

# Dash-App erstellen
app = dash.Dash(__name__)

# Layout der App 
tapp.layout = html.Div([
    html.H1("Lesestellen Dashboard"),
    
    # Tabelle zur Anzeige der Daten
    dash_table.DataTable(
        id='data-table',
        columns=[{"name": i, "id": i} for i in df.columns],
        data=df.to_dict('records'),
        page_size=10,
        style_table={'overflowX': 'auto'}
    ),
    
    # Diagramm für Meldungen pro Station
    dcc.Graph(
        id='station-chart',
        figure=px.bar(df, x='SATION', title='Meldungen pro Station')
    )
])

# Server starten
if __name__ == '__main__':
    app.run_server(debug=True)
