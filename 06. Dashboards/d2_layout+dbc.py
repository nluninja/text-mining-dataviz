# -*- coding: utf-8 -*-
"""
Layout and HTML with Dash applied to GapMinder dataset with Themes

Required steps for setting the environment:

  pip install dash-bootstrap-components

The full list of available themes is CERULEAN, COSMO, CYBORG, DARKLY, FLATLY, JOURNAL, LITERA, LUMEN, LUX, MATERIA, MINTY, MORPH, PULSE, QUARTZ, SANDSTONE, SIMPLEX, SKETCHY, SLATE, SOLAR, SPACELAB, SUPERHERO, UNITED, VAPOR, YETI, ZEPHYR.

https://dash-bootstrap-components.opensource.faculty.ai/docs/themes/
"""

import dash
import dash_html_components as html
import plotly.graph_objects as go
import plotly.express as px
import dash_core_components as dcc
import dash_bootstrap_components as dbc


"""A layout is a grid based visualization that considers the page splitted into 12 columns, and rows: 
components are arranged into the page accordingly: Bootstrap approach"""

app = dash.Dash(external_stylesheets=[ dbc.themes.DARKLY])


df = px.data.gapminder().query("country=='India'")
df2 = px.data.gapminder().query("country=='United States'")


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

"""
the layout in this case is a container with 2 rows of 12 columns each size, and put inside
two columns objects
"""
app.layout = dbc.Container([
    dbc.Row([dbc.Col([html.H1(id = 'H1', children = 'Styling using bootstrap components')],xl=12,lg=12,md = 12,sm=12,xs = 12)],style = {'textAlign':'center', 'marginTop':30, 'marginBottom':30}),
    
    dbc.Row([ 
        dbc.Col([dcc.Graph(id = 'bar_plot',figure = bar_chart(df, df2))],xl=6,lg=6,md = 6,sm=12,xs = 12),
        dbc.Col([dcc.Graph(id = 'line_plot', figure = line_chart(df, df2))],xl=6,lg=6,md = 6,sm=12,xs = 12)
        
        ])
    
    ],fluid = True)

"""
The Bootstrap 4 grid system has five classes for devices:

.xs- (extra small devices - screen width less than 576px)
.sm- (small devices - screen width equal to or greater than 576px)
.md- (medium devices - screen width equal to or greater than 768px)
.lg- (large devices - screen width equal to or greater than 992px)
.xl- (xlarge devices - screen width equal to or greater than 1200px)

"""

if __name__ == "__main__":
    app.run_server()
