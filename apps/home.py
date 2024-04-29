# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 22:05:11 2024

@author: tarek
"""

import dash
from dash import html
import dash_bootstrap_components as dbc

# needed only if running this as a single page app
#external_stylesheets = [dbc.themes.LUX]
#app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

from app import app

# change to app.layout if running as single page app instead
layout = html.Div(style={'background-image': 'url(/assets/houses3.jpg)',
                             'background-size': 'cover',
                             'background-position': 'center',
                             'height': '100vh'},children=[
    dbc.Container([
        dbc.Row([
            #Header span the whole row
            #className: Often used with CSS to style elements with common properties.
            dbc.Col(html.H1("Welcome to the Housing Analysis Dashboard", className="text-center")
                    , className="mb-5 mt-5")
        ]),
        dbc.Row([
            dbc.Col(html.H5(children='This app shows the house prices aginst every other aspect of the house '
                                   )
                    , className="mb-4")
            ]),

        dbc.Row([
            dbc.Col(html.H5(children='It consists of multiple pages: each page has a visualization that displays the house price against other aspects, which gives an overview of how aspects are affecting the house price.', style={'color': 'white'} )
                    , className="mb-5")
        ]),

        dbc.Row([
            # 2 columns of width 6 with a border
            dbc.Col(dbc.Card(children=[html.H3(children='Go to the original dataset for more data',
                                               className="text-center"),
                                       dbc.Button("Housing Data",
                                                  href="https://www.kaggle.com/datasets/yasserh/housing-prices-dataset?resource=download",
                                                  color="primary",
                                                  className="mt-3"),
                                       ],
                             body=True, color="dark", outline=True)
                    , width=3, className="mb-4")

          

        ], className="mb-5")
 
    ])

])

# needed only if running this as a single page app
#if __name__ == '__main__':
#    app.run_server(port=8098,debug=True)