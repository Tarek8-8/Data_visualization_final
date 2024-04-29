
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
    'background': '##343A40',  # Background color
    'text': '#FFFFFF'          # Text color
}

# Initialize the Dash app
app = dash.Dash(__name__)

# Define the layout of the app
layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    dbc.Container([
        dbc.Row([
            # Header spanning the whole row
            dbc.Col(html.H1("Price Distribution Across facilities number", style={'textAlign': 'center', 'color': colors['text']}), 
                    className="mb-5 mt-5")
        ]),
        html.Div([
            # Graph component
            dcc.Graph(
                id='bubbleplot',
                figure=px.scatter(loc_data, x='bathrooms', y='price', size='parking', 
                                  labels={'bathrooms': 'Number of Bathrooms', 'price': 'Price'},
                                  size_max=30).update_layout(clickmode='event+select')
                
            )
        ], style={'width': '80%', 'margin-left': '10%', 'display': 'inline-block'}),
      
    ])
])
# Define callback function to update the graph (if needed)
# Define callback function to update the graph (if needed)
@app.callback(
    Output('bubbleplot', 'figure'),
    [Input('bubbleplot', 'clickData')]
    )
def update_figure(clickData):
    print("Callback function triggered")
    
    # If no data is clicked, return the original figure
    if clickData is None:
        print("No data clicked, returning original figure")
        return px.scatter(loc_data, x='bathrooms', y='price', size='parking', 
                          labels={'bathrooms': 'Number of Bathrooms', 'price': 'Price'},
                          size_max=30)
    
    # Extract the clicked data
    clicked_point = clickData['points'][0]
    x_value = clicked_point['x']
    y_value = clicked_point['y']
    print(f"Clicked point: ({x_value}, {y_value})")
    
    # Filter the dataframe to highlight only the clicked point
    filtered_df = loc_data[(loc_data['bathrooms'] == x_value) & (loc_data['price'] == y_value)]
    print("Filtered dataframe:")
    print(filtered_df)
    
    # Generate a new figure highlighting the clicked point
    fig = px.scatter(filtered_df, x='bathrooms', y='price', size='parking', 
                     labels={'bathrooms': 'Number of Bathrooms', 'price': 'Price'},
                     size_max=30)
    
    # Highlight the clicked point by changing its marker color
    fig.update_traces(marker=dict(color='red', line=dict(color='black', width=2)))
    
    return fig
if __name__ == '__main__':
    app.run_server(debug=True)