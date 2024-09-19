# frontend/app.py

import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import requests

app = dash.Dash(__name__)

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='This app communicates with a Flask backend.'),

    dcc.Input(id='input-number', value='1', type='number'),
    html.Button('Submit', id='submit-button', n_clicks=0),
    html.Div(id='output-div'),

    dcc.Graph(
        id='example-graph'
    )
])

@app.callback(
    Output('output-div', 'children'),
    Input('submit-button', 'n_clicks'),
    Input('input-number', 'value')
)
def update_output(n_clicks, input_value):
    if n_clicks > 0:
        try:
            response = requests.get(f'http://backend:5000/api/square?number={input_value}')
            data = response.json()
            return f"The square of {data['number']} is {data['square']}"
        except Exception as e:
            return f"Error: {e}"
    return ""

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', port=8050, debug=True)
