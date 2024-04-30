# -*- coding: utf-8 -*-
"""
Created on Tue Apr 30 02:31:23 2024

@author: tarek
"""

import dash
from dash import dcc, html
from dash.dependencies import Input, Output, State


app = dash.Dash(__name__)

layout = html.Div([
    html.H1("Feedback Form"),
    html.Label("Rate your experience (0-10):"),
    dcc.Slider(id='rating-slider', min=0, max=10, step=1, value=5),
    html.Label("Additional comments:"),
    dcc.Textarea(id='comments-textarea', placeholder='Enter your comments here...'),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='feedback-output')
])

@app.callback(
    Output('feedback-output', 'children'),
    [Input('submit-button', 'n_clicks')],
    [State('rating-slider', 'value')],
    [State('comments-textarea', 'value')]
)
def submit_feedback(n_clicks, rating, comments):
    if n_clicks > 0:
        # Here you can process the feedback, save it to a database, or perform any other action
        feedback_message = f"Thank you for your feedback! Rating: {rating}, Comments: {comments}"
        return html.Div(feedback_message)
    else:
        return html.Div()

if __name__ == '__main__':
    app.run_server(debug=True)
