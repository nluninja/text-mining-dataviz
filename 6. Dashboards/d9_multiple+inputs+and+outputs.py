# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 14:48:27 2020

@author: anmol
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
from dash.dependencies import Input, Output
import numpy as np


df = px.data.gapminder()




app = dash.Dash()

app.layout = html.Div(id = 'parent', children = [
   
    html.Div(id = 'slider-div', children = [
    dcc.Slider(id = 'year-slider',
               min = df['year'].min(),
               max = df['year'].max(),
               value = df['year'].min(),
               marks = {str(year) : str(year) for year in df['year'].unique() },
               step = None)],style = {'width':'50%', 'display':'inline-block'}), 
    
    
    html.Div( id = 'dropdown-div', children = [
    dcc.Dropdown(id = 'continent-dropdown', 
                 options = [{ 'label':i, 'value':i} for i in np.append(['All'],df['continent'].unique())],
                 value = 'All')],style = {'width':'50%', 'display':'inline-block'}),
    
    html.Div(id = 'filters-selected', style = {'textAlign':'center'}),
    
    dcc.Graph(id = 'scatter-plot')
    
    ])


@app.callback([Output(component_id= 'filters-selected', component_property = 'children'),
              Output(component_id='scatter-plot', component_property='figure')],
              [Input('year-slider', 'value'),
               Input('continent-dropdown', 'value')])
def graph_update(slider_value, dropdown_value):
    
    if dropdown_value == 'All':
        filtered_df=df.loc[(df['year']==slider_value) ]
    else :
        filtered_df=df.loc[(df['year']==slider_value) & (df['continent']==dropdown_value)]
    
    fig = px.scatter(filtered_df, x="gdpPercap", y="lifeExp", 
        size="pop", color="continent", hover_name="country",
        log_x=True, 
        size_max=55, 
        range_x=[100,100000], range_y=[25,90]
        )
            
    return html.Div('Selected year {} and selected continent {}'.format(slider_value, dropdown_value)), fig
    

if __name__== '__main__':
    app.run_server()
