# -*- coding: utf-8 -*-
"""
Created on Mon Apr 29 00:10:03 2024

@author: tarek
"""

# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 21:44:41 2024
@author: tarek
"""
from dash.dependencies import Input, Output
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
import plotly.express as px
import pandas as pd

# Load data
loc_data = pd.read_csv("C:\\Users\\tarek\\Downloads\\Housing (1).csv")

# Define color palette
colors = {
    'background': '#343A40',  # Background color
    'text': '#FFFFFF'          # Text color
}

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    dbc.Container([
        dbc.Row([
            # Header spanning the whole row
            dbc.Col(html.H1("Stories against price colored by basement", style={'textAlign': 'center', 'color': colors['text']}), 
                    className="mb-5 mt-5")
        ]),
        html.Div([
            # Graph component
            dcc.Graph(
                id='scatterplot',
                figure=px.scatter(loc_data, x='stories', y='price', color='basement')
            )
        ], style={'width': '80%', 'margin-left': '10%', 'display': 'inline-block'}),
    ])
])

# Define callback function to update the graph (if needed)
@app.callback(
    Output(component_id='scatterplot', component_property='figure'),
    [Input('url', 'pathname')] # Example input, modify as needed
)
def update_graph(pathname):
#     # Your callback logic here
#     # Example: Filter data based on the pathname and update the graph accordingly
#     if pathname == '/bedrooms':
#         # Filter data or perform any other operation based on the pathname
#         filtered_data = loc_data.loc[loc_data['bedrooms'] == some_value]
#         # Update the graph figure
#         updated_figure = px.bar(filtered_data, x='bedrooms', y='price', color='bedrooms')
#         return updated_figure
#     else:
#         # Return the original figure if the pathname is not '/bedrooms'
#         return px.bar(loc_data, x='bedrooms', y='price', color='bedrooms')

 if __name__ == '__main__':
    app.run_server(debug=True)  # Change the port number as needed
