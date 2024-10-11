# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 20:32:35 2020

@author: anmol
"""


import dash
import dash_html_components as html
import dash_table
import pandas as pd

# df = pd.read_csv("https://raw.githubusercontent.com/plotly/datasets/master/multiple_y_axis.csv")



data = {'Date': ['July 12th, 2013 - July 25th, 2013','July 12th, 2013 - July 25th, 2013'],
        'Election Polling Organization':['The New York Times','Pew Research'],
        'Rep':[10,15],
        'Dem':[5,20],
        'Region':['Northern New York State to the Southern Appalachian Mountains','Canada']}

df=pd.DataFrame(data)

app = dash.Dash()


table = dash_table.DataTable(
    data = df.to_dict('records'),
    columns = [{'id':c, 'name':c} for c in df.columns],
    
    fixed_rows = {'headers':True},
    
    style_table = {'maxHeight':'450px'},
    
    style_header = {'backgroundColor':'rgb(224,224,224)',
                    'fontWeight':'bold',
                    'border':'4px solid white'},
    
    style_data_conditional = [
        
        { 'if':{'row_index':'odd'},
         'backgroundColor':'rgb(224,224,224)',
         'fontSize':'15px'
            
            },
        
        { 'if':{'row_index':'even'},
         'backgroundColor':'rgb(255,255,255)',
         'fontSize':'15px'
            
            
            }
        
        
        
        ],
    
    style_cell = {
        'textAlign':'center',
        'border':'4px solid white',
        'maxWidth':'50px',
        # 'whiteSpace':'normal'
        'textOverflow':'ellipsis'
        
      
        }
    
    
  )


app.layout = html.Div(id = 'parent_div', children = [table])





if __name__ == '__main__':
    app.run_server() 
    