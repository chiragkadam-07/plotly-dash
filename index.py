from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px

from app2 import app
from los_angeles import Los_angeles_layout
from san_diego import San_diego_layout
from san_francisco import San_Francisco_layout

app_tabs = html.Div([
    dbc.Tabs([
        dbc.Tab(label="Los Angeles", tab_id="tab-LA", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger", id='tab-LA'),
        dbc.Tab(label="San Diego", tab_id="tab-SD", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger", id='tab-SD'),
        dbc.Tab(label="San Francisco", tab_id="tab-SF", labelClassName="text-success font-weight-bold", activeLabelClassName="text-danger", id='tab-SF'),
    ],
    id="tabs", active_tab="tab-LA",)
], className="mt-3"
)

app.layout = dbc.Container([
    dbc.Row(dbc.Col(html.H1("Airbnb California Dashboard",
                            style={"textAlign": "center"}), width=12)),
    html.Hr(),
    dbc.Row(dbc.Col(app_tabs, width=12), className="mb-3"
            ),
    html.Div(id='content', children=[])
    ], fluid=True)


@app.callback(
    Output("content", "children"),
    [Input("tabs", "active_tab")]
)
def switch_tab(tab_chosen):
    if tab_chosen == "tab-LA":
        return Los_angeles_layout
    if tab_chosen == "tab-SD":
        return San_diego_layout
    elif tab_chosen == "tab-SF":
        return San_Francisco_layout
    return html.P("This shouldn't be displayed for now...")

if __name__=='__main__':
    app.run_server(debug=True, port=8002)
