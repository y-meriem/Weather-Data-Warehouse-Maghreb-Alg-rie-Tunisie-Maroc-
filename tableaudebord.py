### Les bibliothéques necessaires
import numpy as np 
import pandas as pd 
import sys
import os
sys.path.append(r'c:\users\dell\appdata\roaming\python\python312\site-packages')
import pymysql 
import csv
import plotly.express as px
import plotly.graph_objects as go
from dash import Dash, dcc, html, Input, Output

### Une carte géographique et Un diagramme en barre
app = Dash(__name__)

# -- Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             database='weathers_datawarehouse',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

cursor = connection.cursor()
# Ajoutez les colonnes day, month, et year à la table Dim_Date
cursor.execute('''
ALTER TABLE Dim_Date
ADD COLUMN Day INT,
ADD COLUMN Month INT,
ADD COLUMN Year INT;
''')

connection.commit()
# Mettez à jour les colonnes day, month et year en extrayant les valeurs depuis la colonne Date
cursor.execute('''
UPDATE Dim_Date
SET Day = DAY(STR_TO_DATE(Date, '%Y-%m-%d')),
    Month = MONTH(STR_TO_DATE(Date, '%Y-%m-%d')),
    Year = YEAR(STR_TO_DATE(Date, '%Y-%m-%d'));
''')
connection.commit()
# -- Import data for TMAX
query_tmax = """
SELECT TMAX, station_dim.Country_Name, dim_date.Year 
FROM fact_weather
JOIN station_dim ON fact_weather.Station_ID = station_dim.Station_ID 
JOIN dim_date ON fact_weather.Date_ID = dim_date.Date_ID
"""
with connection.cursor() as cursor:
    cursor.execute(query_tmax)
    data = cursor.fetchall()  # Fetches all the rows of a query result, returns a list of dictionaries

df_tmax = pd.DataFrame(data)
cur= connection.cursor()
# -- Import data for TAVG
query_tavg = """
SELECT TAVG, station_dim.Country_Name, dim_date.Year 
FROM fact_weather
JOIN station_dim ON fact_weather.Station_ID = station_dim.Station_ID 
JOIN dim_date ON fact_weather.Date_ID = dim_date.Date_ID
"""
with connection.cursor() as cur:
    cur.execute(query_tavg)
    data = cur.fetchall()  # Fetches all the rows of a query result, returns a list of dictionaries

df_tavg = pd.DataFrame(data)
# Group and summarize the data
df_tmax = df_tmax.groupby(['Country_Name', 'Year']).agg({'TMAX': 'sum'}).reset_index()
df_tavg = df_tavg.groupby(['Country_Name', 'Year']).agg({'TAVG': 'sum'}).reset_index()

# App layout
app.layout = html.Div([
    html.H1("Visualisation des Données Climatiques", style={'text-align': 'center'}),

    dcc.Dropdown(id="slct_year",
                 options=[{"label": str(year), "value": year} for year in df_tmax['Year'].unique()] + [{"label": "Tout", "value": "Tout"}],
                 multi=True,
                 placeholder="Select a year",
                 value=['Tout'],
                 style={'width': "40%"}),

    html.Div(id='output_container', children=[]),
    html.Br(),

    dcc.Graph(id='my_bar_chart', figure={}),
    dcc.Graph(id='sales_map', figure={})
])

@app.callback(
    [Output(component_id='output_container', component_property='children'),
     Output(component_id='my_bar_chart', component_property='figure'),
     Output(component_id='sales_map', component_property='figure')],
    [Input(component_id='slct_year', component_property='value')]
)
def update_graph(option_slctd):
    container = f"Année(s) choisie par l'utilisateur : {option_slctd}"

    if 'Tout' in option_slctd or not option_slctd:
        dff_tmax = df_tmax.copy()
        dff_tavg = df_tavg.copy()
    else:
        dff_tmax = df_tmax[df_tmax['Year'].isin(option_slctd)]
        dff_tavg = df_tavg[df_tavg['Year'].isin(option_slctd)]

    # Bar chart for TMAX
    fig_bar = px.bar(dff_tmax, x='Country_Name', y='TMAX', color='Country_Name', barmode='group',
                 title='Température maximale (TMAX) par pays et par année')

    # Choropleth map for TAVG
    fig_map = px.choropleth(
        data_frame=dff_tavg,
        locationmode='country names',
        locations='Country_Name',
        scope="world",
        color='TAVG',
        hover_data=['Country_Name', 'TAVG'],
        color_continuous_scale=px.colors.sequential.Viridis_r,
        labels={'Température moyenne'},
        template='plotly_white'
    )
    fig_map.update_layout(
        title_text='Température moyenne (TAVG) par pays et par année',
        geo_scope='world'
    )

    return container, fig_bar, fig_map

if __name__ == '__main__':
    app.run_server(debug=True)