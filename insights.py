# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

# Imports from this application
from app import app

# 1 column layout
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Insights
            
            The figure below demonstrates the predicting power of our prediction model as compared 
            to actual data. The horizontal columns denote if a project's campaign result was 'successful' 
            or 'failed.' The vertical columns indicate how our model predicts these results. As you can 
            see in the figure, our model does a decent job predicting project outcome with a precision 
            rate of 83% and 76% for the 'successful' and 'failed categories respectively. To put this 
            in plain English, when predicting if a project would be successful in getting funded, our 
            model is 83% correct; when predicting 'failed,' our model is 76% correct. In summary, our
            model is slightly better at predicting 'successful' campagins than 'failed.'   
            
            
            
            
            
            
             

            """
        
        ), 
    
    # html.Img(src='assets/Rating Distribution.PNG', className='img-fluid'),

    html.Img(src='assets/confusionMatrix.png', className='img-fluid')
    
    ],
)



       
layout = dbc.Row([column1])