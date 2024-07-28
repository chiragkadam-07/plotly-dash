# from dash import Dash, dcc, html, Output, Input
# import dash_bootstrap_components as dbc
# import pandas as pd
# import numpy as np
# import plotly.express as px
# import time

# app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP], suppress_callback_exceptions=True)


import dash
import dash_bootstrap_components as dbc

app = dash.Dash(__name__, suppress_callback_exceptions=True, external_stylesheets=[dbc.themes.CYBORG],
                meta_tags=[{'name': 'viewport',
                            'content': 'width=device-width, initial-scale=1.0'}]
                )
app.css.append_css({"external_url": "/assets/styles.css"})