# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 11:24:40 2020

@author: anmol
"""



import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output


app = dash.Dash()

app.layout = html.Div(id = 'parent', children = [
    
    #heading 
    html.H3(id = 'h3', children = 'Basic Callback example'),
    
    html.Br(),
    
    dcc.Dropdown(id = 'dropdown',
                 options = [
                     {'label':'amazing', 'value':5},
                     {'label':'average','value':3},
                     {'label':'below average', 'value':1}
                     
                     ],
                 value = 5,
                 
                 
                 ),
    html.Br(),
    
    html.Div(id = 'output-text')
    
    
    ])


@app.callback(Output(component_id='output-text',component_property='children'),
              [Input(component_id='dropdown',component_property='value')])
def basic_callback(input_value):
    return html.Div(input_value)


if __name__ == '__main__':
    app.run_server(debug=False)