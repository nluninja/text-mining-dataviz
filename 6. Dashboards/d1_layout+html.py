# -*- coding: utf-8 -*-
"""
Layout and HTML with Dash applied to GapMinder dataset

Required steps for setting the environment:

pip install dash plotly

"""

import dash
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import dash_core_components as dcc


app = dash.Dash()


df = px.data.gapminder().query("country=='India'")
df2 = px.data.gapminder().query("country=='United States'")


# function that builds the bar chart
def bar_chart(df,df2):
    
    fig = go.Figure([go.Bar(x = df['year'], y = df['gdpPercap'], marker_color = 'indianred',name = 'India'),
                     go.Bar(x = df2['year'], y = df2['gdpPercap'], marker_color = 'blue', name = 'US')
                     ])
    
    fig.update_layout(title = 'GDP per capita over the years',
                      xaxis_title = 'Years',
                      yaxis_title = 'GDP per capita', 
                       barmode = 'group'
                      )

    return fig  

#function that builds the line chart

def line_chart(df, df2):
    fig = go.Figure(data = [go.Scatter(x = df['year'], y = df['lifeExp'],\
                                       line = dict(color = 'firebrick', width = 4), text = df['country'], name = 'India'),
                            go.Scatter(x = df2['year'], y = df2['lifeExp'],\
                                       line = dict(color = 'firebrick', width = 4), text = df2['country'], name = 'US')])
    
        
    fig.update_layout(title='Life Expectency over the years',
                       xaxis_title='Years',
                       yaxis_title='Life Expectancy (years)',
                       )


    return fig 

#layout definition

app.layout = html.Div(id = 'parent', children = [
    html.H1(id = 'H1', children = 'Styling using html components', style = {'textAlign':'center',\
                                            'marginTop':40,'marginBottom':40}),
    html.Div(id = 'bar_div', children = [dcc.Graph(id = 'bar_plot', figure = bar_chart(df, df2))],style = {'width':'50%','display':'inline-block'}),
    
    html.Div(id = 'line_div', children = [dcc.Graph(id = 'line_plot', figure = line_chart(df, df2))],style = {'width':'50%','display':'inline-block'})
    
    ])

if __name__ == '__main__': 
    app.run_server()