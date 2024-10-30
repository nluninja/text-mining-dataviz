# -*- coding: utf-8 -*-
"""
NLP Question Answering App

requirements: 

pip install transformers

"""


from transformers import pipeline
import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input, Output, State
import dash_bootstrap_components as dbc

app = dash.Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])

PLOTLY_LOGO = "https://images.plot.ly/logo/new-branding/plotly-logomark.png"

navbar = dbc.Navbar( id = 'navbar', children = [
    dbc.Row([
        dbc.Col(html.Img(src = PLOTLY_LOGO, height = "70px")),
        dbc.Col(
            dbc.NavbarBrand("Question Answering App", style = {'color':'white', 'fontSize':'25px','fontFamily':'Times New Roman'}
                            )
            
            )
        
        
        ],align = "center",
        # no_gutters = True
        ),
    
    
    ], color = '#000000')

body_app = dbc.Container([
    
    html.Br(),
    html.Br(),
    
    dbc.Row([
        dbc.Col(html.H4('Enter the context paragraph'), width = {'size':10, 'offset':2}),
    
        ]),
    
    dbc.Row([
        dbc.Col(dcc.Textarea(id = 'context-area', value = '', style = {'height':'200px','width':'80%'}),\
                width = {'size':10, 'offset':2}),
    
        ]),
        
    html.Br(),
    html.Br(), 
        
       dbc.Row([
        dbc.Col(html.H4('Enter your question'), width = {'size':10, 'offset':2}),
    
        ]),
       
           dbc.Row([
        dbc.Col(dcc.Textarea(id = 'ques-area', value = '', style = {'height':'100px','width':'80%'}),\
                width = {'size':10, 'offset':2}),
    
        ]),
               
      dbc.Row([
        dbc.Col(dbc.Button(id = 'generate-ans', children = 'Generate Answer', color = 'dark', n_clicks = 0),\
                width = {'size':10, 'offset':2}),
    
        ]),    
          
        dbc.Row([
        dbc.Col(
            dcc.Loading(
                id = 'load-ans',
                type = 'default',
                children = html.Div(id = 'div-answer',style = {'textAlign':'center','color':'black'})
                )
            
            ),
    
        ]),    
          
    
    
    ], 
    # style = {'backgroundColor':'#f7f7f7'},
    fluid = True)
    
@app.callback(Output('div-answer','children'),
              [Input('generate-ans','n_clicks')],
              [State('context-area', 'value'),
               State('ques-area','value')])

def show_answer(clicks, context, ques):
    if clicks > 0:
        
        nlp = pipeline("question-answering")
        
        context_para = r"""{}""".format(context)
        
        return nlp(question="{}".format(ques), context=context_para)['answer']
        
        
    else :
        return ""



app.layout = html.Div(id = 'parent', children = [navbar,body_app])


if __name__ == "__main__":
    app.run_server(debug = True)

