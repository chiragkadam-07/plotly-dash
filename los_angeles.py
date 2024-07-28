from dash import Dash, dcc, html, Output, Input
import dash_bootstrap_components as dbc
import pandas as pd
import numpy as np
import plotly.express as px
# import time
# from dash_bootstrap_templates import load_figure_template
# load_figure_template('DARKLY')
from app2 import app


# start = time.time()

df = pd.read_csv("C:/Users/sahil/Downloads/New folder/Los_Angeles_subset.csv")
colorscales = px.colors.named_colorscales()
bar_colors = px.colors.qualitative.Plotly

# top_neighbourhood = df['neighbourhood'].value_counts().head(1).index[0]
# top_value = df['neighbourhood'].value_counts().head(1).values[0]

# Define the layout
Los_angeles_layout = dbc.Container([
    # dbc.Row([
    #     dbc.Col([
    #         dcc.Markdown('# Los Angeles Airbnb Analysis', style={'textAlign': 'center'})
    #     ], width=12)
    # ]),

    dbc.Row([
        dbc.Col([
            dbc.Card([
                dbc.CardHeader('AVG Price', className='custom-card-header1'),
                html.Hr(style={'margin':0}),
                dbc.CardBody(df['price'].mean().round(), className='custom-card-body')
            ], style={"width": "11rem"}, className='custom-card1')
        ], width={'size': 2}),

         dbc.Col([
              dbc.Card([
                   dbc.CardHeader("AVG Reviews", className='custom-card-header1'),
                   dbc.CardBody(df['number_of_reviews'].mean().round(), className='custom-card-body')
              ], style={"width": "11rem"}, className='custom-card1'
              )
         ], width={'size': 2}),

         dbc.Col([
              dbc.Card([
                   dbc.CardHeader("AVG Availability", className='custom-card-header1'),
                   dbc.CardBody(df['availability_365'].mean().round(), className='custom-card-body')
              ], style={"width": "11rem"}, className='custom-card1')
         ], width={'size': 2}),

         dbc.Col([
              dbc.Card([
                   dbc.CardHeader("Top Neighbourhood", className='custom-card-header1'),
                   dbc.CardBody(id='card-content',children=[], className='custom-card-body1')
              ], style={"width": "15rem"}, className='custom-card1')
         ], width={'size': 3}),

        #  dbc.Col([
        #         dcc.Markdown("nights"),
        #         nights := dbc.Input(type='number', min=df.minimum_nights.min(), max=df.minimum_nights.max(), value=1),
        #         nights_max := dbc.Input(type='number',  min=df.minimum_nights.min(), max=df.minimum_nights.max(), value=15),
        #         html.Div(id='output-range')
        #     ], width={'size': 1}),
         
        dbc.Col([
            dcc.Markdown("Interactivity", className='box',), # 6#=h6, __italic, *bold
            interact := dcc.RadioItems(options=[
                    {'label': 'Enabled', 'value': 'Enabled'},
                    {'label': 'Disabled', 'value': 'Disabled'}
                ],value='Enabled', className='radio-items2',
                
            )
        ], width={'size': 2, 'offset': 1}, style={'paddingTop': '11px'})
    ]),

    dbc.Row([
        dbc.Col([
            dcc.Markdown('###### Select price range'),
            price_slider := dcc.RangeSlider(min=df.price.min(), max=500, value=[0, 200], step=10,
                                            marks={'0': '0', '20': '20', '50': '50',
                                                   '100': '100', '150': '150',
                                                   '300': '300', '500': '500'},
                                            tooltip={"placement": "bottom", "always_visible": True}
                                            )
        ], width=5),

        # dbc.Col([
        #         html.Div([
        #             dcc.Markdown("minimum-Nights",),
        #         ],),
        #         nights := dbc.Input(type='number', min=df.minimum_nights.min(), max=df.minimum_nights.max(), value=1, #style={'marginRight': '10px'}
        #                             ),
        #         nights_max := dbc.Input(type='number',  min=df.minimum_nights.min(), max=df.minimum_nights.max(), value=15),
        #         ], 
        #         width={'size': 2}, #style={'display': 'flex', 'alignItems': 'center'}
        #         ),

        dbc.Col([
            html.Div([
                dcc.Markdown("###### Minimum-Nights", style={'textAlign': 'center', 'marginBottom': '10px'})
            ], style={'textAlign': 'center'}),
            html.Div([
                nights := dbc.Input(type='number', min=df.minimum_nights.min(), max=df.minimum_nights.max(), value=1, style={'marginRight': '10px', 'textAlign':'center'}),
                nights_max := dbc.Input(type='number', min=df.minimum_nights.min(), max=df.minimum_nights.max(), value=15, className='text-center')
            ], style={'display': 'flex', 'justifyContent': 'center'})
        ], width={'size': 2}),

        dbc.Col([
            dcc.Markdown('###### Available Days'),
            days_slider := dcc.RangeSlider(min=df.availability_365.min(), max=365, value=[0, 160], step=5,
                                           marks={'0': '0', '1': '1', '5': '5', '10': '10', '30': '30',
                                                  '60': '60', '120': '120', '200': '200', '300': '300', '365': '365'},
                                           tooltip={"placement": "bottom", "always_visible": True}
                                           )
        ], width=5),
    ]),


    dbc.Row([
        dbc.Col([
            map_chart := dcc.Graph(figure={}, className='graph-padding')
        ], width=12)
    ]),

    # dbc.Row([
    #     dbc.Col([
    #         map_chart1 := dcc.Graph(figure={})
    #     ], width=12)
    # ]),

    dbc.Row([
        dbc.Col([
            bar_chart := dcc.Graph(figure={}, className='graph-padding')
        ], width=6),

        dbc.Col([
            bar_chart1 := dcc.Graph(figure={}, className='graph-padding')
        ], width=6)
    ]),

    dbc.Row([
        dbc.Col([
            hist_chart2 := dcc.Graph(figure={}, className='graph-padding')
        ], width=6),

        dbc.Col([
            hist_chart := dcc.Graph(figure={}, className='graph-padding')
        ], width=6),
    ]),    

    dbc.Row([
        dbc.Col([
            map_chart2 := dcc.Graph(figure={}, className='graph-padding')
        ], width=12)
    ]),

    dbc.Row([
         dbc.Col([
              dcc.Graph(id='box_plot', figure={}, className='graph-padding')
         ], width= 12)
    ]),

    dbc.Row([
         dbc.Col([
              html.Div([
                    html.P("Color Scale"),
                    dcc.Dropdown(
                        id='dropdown', 
                        options=colorscales,
                        value='viridis')
            ])
        ]),

        dbc.Col([
             html.Div([
                html.P("Bar Color"),
                dcc.Dropdown(
                    id='dropdown-barcolor', 
                    options=bar_colors,
                    value='#636EFA'
                ),
                ])
                ])
        ])
], fluid=True)


@app.callback(
    [Output(map_chart, 'figure'), Output(hist_chart, 'figure'),
    #  Output(map_chart1, 'figure'), 
     Output(bar_chart, 'figure'),
     Output(bar_chart1, 'figure'), Output(hist_chart2, 'figure'),
     Output(map_chart2, 'figure'), Output('card-content', 'children'),
     Output('box_plot', 'figure')
     ],
    [Input(interact, 'value'), Input(price_slider, 'value'),
     Input(days_slider, 'value'), Input(nights, 'value'),
     Input(nights_max, 'value'), Input("dropdown", "value"),
     Input("dropdown-barcolor", "value")
     ]
)
def update_graph(option, prices_value, days_value, nights_min, nights_max, scale, barcolor):
        print(prices_value)
        print(days_value)
        # dff = df[df.minimum_nights >= nights_value]
        # dff = df[(df.minimum_nights > nights_value[0]) & (df.minimum_nights < nights_value[1])]
        if option == "Enabled":
            # dff = df
            # print("total dff rows", dff.shape[0])
            dff = df[(df.price >= prices_value[0]) & (df.price <= prices_value[1])]
            dff = dff[(dff.availability_365 >= days_value[0]) & (dff.availability_365 <= days_value[1])]
            dff = dff[(dff.minimum_nights >= nights_min) & (dff.minimum_nights <= nights_max)]
            # dff = dff[dff.minimum_nights >= nights_min]
            # dff = dff[dff.minimum_nights >= nights_max]
        else:
            dff = df

        if not dff.empty:
            top_neighbourhood = dff['neighbourhood'].value_counts().idxmax()
            top_value = dff['neighbourhood'].value_counts().max()

        else:
            top_neighbourhood = "None"
            top_value = 0    

        dff['group'] = np.where(dff['availability_365'] < 91, 'High',
                                np.where(dff['availability_365'] < 181, 'Moderate',
                                        np.where(dff['availability_365'] <= 365, 'low', 'No')))

        fig_map = px.scatter_mapbox(data_frame=dff, lat='latitude', lon='longitude', color='price', height=580, title='Price Heatmap by Location',
                                    range_color=[0, 500], zoom=11, #color_continuous_scale=px.colors.sequential.Sunset,
                                    hover_data={'latitude': False, 'longitude': False, 'room_type': True,
                                                'availability_365': True, 'host_name': True, 'neighbourhood':True}, template='plotly_dark',
                                                color_continuous_scale=scale)
        fig_map.update_layout(mapbox_style='carto-positron', coloraxis_colorbar=dict(title='Price'),
                              margin=dict(l=10, r=10, t=50, b=10))

        fig_hist = px.histogram(dff, x='availability_365', histfunc='count', title='Days Availability Count',
                                template='plotly_dark')
        fig_hist.update_layout(yaxis_title='Count', xaxis_title='Available Days', margin=dict(r=20))

        # Bar chart for room types
        room_type_counts = dff['room_type'].value_counts().reset_index()
        room_type_counts.columns = ['room_type', 'count']
        fig_bar = px.bar(room_type_counts, x='room_type', y='count', title='Listings Count by Room Type',
                         labels={'room_type':'Room Type', 'count':'Count'}, template='plotly_dark', color_continuous_scale=scale, color='count'
                        )
        fig_bar.update_layout(coloraxis_showscale=False)

        # fig_mp1 = px.scatter_mapbox(data_frame=dff, lat='latitude', lon='longitude', color='availability_365',
        #                             height=580,
        #                             range_color=[0, 365], zoom=11, color_continuous_scale=px.colors.sequential.Sunset,
        #                             hover_data={'latitude': False, 'longitude': False, 'room_type': True,
        #                                         'minimum_nights': True})
        # fig_mp1.update_layout(mapbox_style='carto-positron')

        a = df['host_name'].value_counts().reset_index(name='count')
        fig_bar1 = px.bar(a.sort_values(ascending=False, by='count').iloc[:5], 'host_name', 'count',
                        template='plotly_dark', title='Top 5 Host Listings', labels={'host_name':'Host Name', 'count':'Count'},
                        color_discrete_sequence=[barcolor])

        fig = px.histogram(dff, 'price', histfunc='count', title='Price Frequency Distribution', template='plotly_dark')
        fig.update_layout(xaxis_title='Price', yaxis_title='Count', margin=dict(r=20), 
                          )

        fig_mp2 = px.scatter_mapbox(data_frame=dff, lat='latitude', lon='longitude', color='minimum_nights',
                                    height=580, title='Minimum Nights by Location',
                                    range_color=[0, 31], zoom=11, #color_continuous_scale=px.colors.sequential.Sunset,
                                    hover_data={'latitude': False, 'longitude': False, 'room_type': True,
                                                'minimum_nights': True, 'neighbourhood':True}, template='plotly_dark', color_continuous_scale=scale)
        fig_mp2.update_layout(mapbox_style='carto-positron', coloraxis_colorbar=dict(title='Minimum Nights'),
                              margin=dict(l=10, r=10, t=50, b=10))

        card_content = [
                 html.H6(f'{top_neighbourhood}'),
                 html.H6(f"{top_value}")
            ] 

        fig_box = px.box(dff, x='room_type', y='price', title='Price Distribution by Room Type',
                         labels={'room_type':'Room Type', 'price':'Price'}, template='plotly_dark')
        fig_box.update_layout(margin=dict(t=50, r=10, b=40))

               

        print("dff rows after filter", dff.shape[0])

        # fig = px.bar(dff, x='group', template='ggplot2')

        return fig_map, fig_hist, fig_bar, fig_bar1, fig, fig_mp2,  card_content, fig_box,



# end = time.time()
# print(f"execution time is : {(end-start)*10**3} ms")
