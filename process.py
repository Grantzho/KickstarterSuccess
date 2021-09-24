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
        
            ## Process

            We combined Kickstarter's project data from 2010 to 2020. Our pre-processed 
            dataset has more than 180,000 entries. Upon exploring with different feature
            matrix and classfiers, we decided to focus on six features to predict project 
            success rate using a random forest classfier. The hyper-parameters of the 
            classifier were tuned using a random search cross validation method.  
            
            The figure below shows the feature importance in our model ranked from high to
            low. The sub-category and funding goal of a project appear to be the most salient 
            features when it comes to predicting a successful campaign. This makes a lot of
            sense as a project needs to both gauge their audience interest and set a 
            reasonable funding expectation in order to have a successful campaign on 
            Kickstarter.
            
            
            
            """
        ),
        html.Img(src='assets/featureImportance.png', className='img-fluid'),
    ],
    
)

layout = dbc.Row([column1])