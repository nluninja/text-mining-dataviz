# -*- coding: utf-8 -*-

'''
html components: render web components using HTML
'''

import dash
import dash_html_components as html


app = dash.Dash()


app.layout = html.Div(id = 'parent', children = [
    
    #H1
    html.H1(id = 'H1', children = 'Hello! This is H1 tag', style = {'textAlign':'center'}),
    
    #H2
    html.H2(id = 'H2', children = 'Hello! This is H2 tag',style = {'textAlign':'center'}),
    
   
    #Paragraph
    html.P(id = 'para', children = 'This is paragraph tag', style = {'textAlign':'center'}), 
    
    #Link
    html.Div(id = 'link_div',children = [html.A(id = 'link', children = 'Unicatt link', href = 'https://www.unicatt.it', style = {'fontSize':30})],\
             style = {'textAlign':'center'}),

    #line break
    html.Br(),
    
    #image
    html.Img(id = 'image', src = 'https://www.unicatt.it/content/dam/siti-web/unicatt/it/logo-unicatt.svg', height = '100px'),
    
    #Rolling text
    html.Marquee(id = 'marquee',children = 'Hello! This can be used to show some notifications')
    
    ])


if __name__ == '__main__':
    app.run_server()





    
    
    






    
