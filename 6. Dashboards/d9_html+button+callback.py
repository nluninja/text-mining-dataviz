# -*- coding: utf-8 -*-
'''
Callbacks associated to a click on a button'''

# from emb_cov import *
import dash
import dash_html_components as html
from dash.dependencies import Input, Output

#app inizialization
app = dash.Dash()

#app layout
app.layout = html.Div(id = 'parent', children = [
    
    html.Button(id = 'html-button', children = 'Click the button !', n_clicks = 0),
    
    html.Br(),
    
    html.Div(id = 'output-text')
    
    
    ])

#app callback
@app.callback(Output(component_id='output-text', component_property='children'),
              [Input(component_id='html-button',component_property='n_clicks')])
def button_update(value): #function that given the Input, generates the Output
    return html.Div(str(value) + ' clicks !')


    

if __name__ == "__main__":
    app.run_server(debug=False)