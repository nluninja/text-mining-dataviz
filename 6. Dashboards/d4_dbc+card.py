# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 01:10:57 2020

@author: anmol
"""

import dash
import dash_bootstrap_components as dbc
import dash_html_components as html


app = dash.Dash(external_stylesheets = [ dbc.themes.FLATLY],)

card_content = [
    dbc.CardHeader("Card Header"),
    
    dbc.CardBody(
        [
            html.H5("Card Title", className = "card-title"),
            
            html.P("This is some card content that we will reuse",
                   className = "card-text")
            
            
            ]
               
        )  
    ]

app.layout = dbc.Container([
    dbc.Row([
        dbc.Col(dbc.Card(card_content, color = 'primary', inverse = True)),
        dbc.Col(dbc.Card(card_content, color = 'info', inverse = True)),
        dbc.Col(dbc.Card(card_content, color = 'secondary', outline = True))
        
        
        ])
    
    
    ],fluid = True)

if __name__ == "__main__":
    app.run_server()