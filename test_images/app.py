# app.py

import dash
from dash import dcc, html
from dash.dependencies import Input, Output

# สร้างแอป Dash
app = dash.Dash(__name__)

# Layout ของแอป
app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children='Dash: A web application framework for Python.'),

    dcc.Input(id='input-text', value='Dash', type='text'),
    html.Div(id='output-div'),

    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3, 4, 5], 'y': [10, 20, 30, 40, 50], 'type': 'line', 'name': 'Line Chart'},
            ],
            'layout': {
                'title': 'Example Line Chart'
            }
        }
    )
])

# Callback สำหรับการโต้ตอบของแอป
@app.callback(
    Output(component_id='output-div', component_property='children'),
    Input(component_id='input-text', component_property='value')
)
def update_output_div(input_value):
    return f'You\'ve entered: {input_value}'


if __name__ == '__main__':
    app.run_server(debug=True)
