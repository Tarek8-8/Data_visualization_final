# -*- coding: utf-8 -*-
"""
Created on Sun Apr 28 21:41:30 2024

@author: tarek
"""

import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

from app import app
# import all pages in the app
from apps import bedrooms, home, Stories,Furnish,Area,services,Facilities,Feedback

# building the navigation bar
# https://github.com/facultyai/dash-bootstrap-components/blob/master/examples/advanced-component-usage/Navbars.py
dropdown = dbc.DropdownMenu(
    children=[
        dbc.DropdownMenuItem("Home", href="/home"),
        dbc.DropdownMenuItem("Bedrooms", href="/bedrooms"),
        dbc.DropdownMenuItem("Stories",href="/stories"),
        dbc.DropdownMenuItem("Furnish",href="/furnish"),
        dbc.DropdownMenuItem("Area",href="/area"),
        dbc.DropdownMenuItem("Services",href="/services"),
        dbc.DropdownMenuItem("Facilities",href="/facilities"),
        dbc.DropdownMenuItem("Feedback",href="/feedback")
        
  
    ],
    nav = True,
    in_navbar = True,
    label = "Explore Pages", 
)

navbar = dbc.Navbar(
    dbc.Container(
        [
            html.A(
                # Use row and col to control vertical alignment of logo / brand
                dbc.Row(
                    [
                       
                        dbc.Col(dbc.NavbarBrand("House Price Analysis Dashboard", className="ml-2")),
                    ],
                    align="center"
                   
                ),
                href="/home",
            ),
            dbc.NavbarToggler(id="navbar-toggler2"),
            dbc.Collapse(
                dbc.Nav(
                    # right align dropdown menu with ml-auto className
                    [dropdown], className="ml-auto", navbar=True
                ),
                id="navbar-collapse2",
                navbar=True,
            ),
        ]
    ),
    color="dark",
    dark=True,
    className="mb-4",
)

def toggle_navbar_collapse(n, is_open):
    if n:
        return not is_open
    return is_open

for i in [2]:
    app.callback(
        Output(f"navbar-collapse{i}", "is_open"),
        [Input(f"navbar-toggler{i}", "n_clicks")],
        [State(f"navbar-collapse{i}", "is_open")],
    )(toggle_navbar_collapse)

# embedding the navigation bar
app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    navbar,
    html.Div(id='page-content')
])
@app.callback(Output('page-content', 'children'),
              [Input('url', 'pathname')])
def display_page(pathname):
    if pathname in ['/', '/home']:
        return home.layout
    elif pathname == '/bedrooms':
        return bedrooms.layout
    elif pathname == '/stories':
        
        return Stories.layout
    elif pathname == '/furnish':
        return Furnish.layout
    elif pathname == '/area':
        return Area.layout
    elif pathname == '/services':
        return services.layout
    elif pathname == '/facilities':
        return Facilities.layout
         elif pathname == '/feedback':
        return Feedback.layout
    else:
        return html.Div("404 - Page not found")

if __name__ == '__main__':
    app.run_server(port=8099,debug=True)

