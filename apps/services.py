
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
unique_values_hotwater = loc_data['hotwaterheating'].unique()
unique_values_airconditioning = loc_data['airconditioning'].unique()
unique_values_guestroom = loc_data['guestroom'].unique()

# Check if any unexpected values are present
if set(unique_values_hotwater) != {'yes', 'no'}:
    raise ValueError("Unexpected values found in 'hotwaterheating' column")

if set(unique_values_airconditioning) != {'yes', 'no'}:
    raise ValueError("Unexpected values found in 'airconditioning' column")

if set(unique_values_guestroom) != {'yes', 'no'}:
    raise ValueError("Unexpected values found in 'guestroom' column")

# Replace 'yes' and 'no' with 1 and 0, respectively
loc_data[['hotwaterheating', 'airconditioning', 'guestroom']] = loc_data[['hotwaterheating', 'airconditioning', 'guestroom']].replace({'yes':1,'no':0})
#grouped_data = loc_data.groupby(['hotwaterheating', 'airconditioning', 'guestroom']).mean().reset_index()

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
            dbc.Col(html.H1("Price Distribution Across Services available ", style={'textAlign': 'center', 'color': colors['text']}), 
                    className="mb-5 mt-5")
        ]),
        html.Div([
            # Graph component
            dcc.Graph(
                id='groupedbox',
                figure=px.bar(loc_data,
                    x=['hotwaterheating','airconditioning','guestroom'],
                    y='price',
                    labels={'x': 'Avaliability', 'price': 'Price ($)'},
                    color_discrete_sequence=['blue', 'green', 'orange']
                ).update_layout(clickmode='event+select')
                .update_traces(marker_opacity=0.5)
                .update_layout(xaxis_title='Available') 
            )      
        ], style={'width': '80%', 'margin-left': '10%', 'display': 'inline-block'}),
    ])
])

# Define callback function to update the graph (if needed)
@app.callback(
    Output('groupedbox', 'figure'),
    [Input('groupedbox', 'clickData')]
)
def update_graph(clickData):
    if clickData is None:
        # No group selected, return the default plot
        return px.bar(
            loc_data, 
            x=['hotwaterheating','airconditioning','guestroom'],
            y='price',
            labels={'x': 'Services', 'price': 'Price ($)'},
            color_discrete_sequence=['blue', 'green', 'orange']
        ).update_traces(marker_opacity=0.6)

    # Extract the selected group from clickData
    selected_group = clickData['points'][0]['x']

    # Create a mask to filter loc_data based on the selected group
    mask = loc_data[selected_group] == 1
    
    # Create the updated plot with only the selected group highlighted
    return px.bar(
        loc_data[mask], 
        x=['hotwaterheating','airconditioning','guestroom'],
        y='price',
        labels={'x': 'Services', 'price': 'Price ($)'},
        color_discrete_sequence=['blue', 'green', 'orange']
    ).update_traces(marker_opacity=0.7)  # Increase opacity for selected group

if __name__ == '__main__':
    app.run_server(debug=True)  # Change the port number as needed