from dash import Dash, dcc, html, Output, Input
import pandas as pd
import plotly.graph_objects as go

app = Dash(__name__)

df = pd.read_csv('pink_morsel_sales_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# print(df[:5])


app.layout = html.Div(className='container', children=[
    html.H1(children='Pink Morsel Sales Data', style={'textAlign': 'center'}, className='main-title'),
    html.Br(),
    html.Div(
        id='dd-output-container',
        style={'textAlign': 'center', 'padding': '10px', 'fontSize': '18px'}, className='region-text'
    ),

    html.Div([
        dcc.Graph(id='pinkM_Sales', className='pink-morsel-sales'),


        html.Div(
            dcc.RadioItems(
                ['north', 'south', 'east', 'west', 'all'],
                id='region-radio',
                value='all',
                inline=True,
                className='region-selector',
                labelClassName='region-label',
                inputClassName='region-input'
            ),
            style={
                'position': 'absolute',
                'top': '60px',
                'right': '55px',
                'backgroundColor': 'rgba(255,255,255,0.8)',
                'padding': '5px 10px',
                'borderRadius': '5px'
            }
        )
    ], style={'position': 'relative'}),

], style={'maxWidth': '1200px', 'margin': '0 auto'})

region_colours = {
    'north': '#F2A7B0',
    'south': '#E8735A',
    'east': '#C4532A',
    'west': '#F5C5A3',
    'all': '#106bf7 ',
}

@app.callback(
[Output('dd-output-container', 'children'),
        Output('pinkM_Sales', 'figure'),],
    [Input('region-radio', 'value')]
)

def update_output(value):
    if value == 'all' or value is None:
        filtered_df = df
        region_text = 'Showing all regions'
        colour = region_colours['all']
    else:
        filtered_df = df[df['region'] == value]
        region_text = f"Displaying {value}'s data"
        colour = region_colours[value]

    fig = go.Figure()
    fig.add_scatter(x=filtered_df['date'], y=filtered_df['sales'], line = dict(color=colour))
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Sales',
        title='Pink Morsel Sales over time',
        annotations=[
            dict(
                text=f'Region: {value if value else 'all'}',
                xref='paper',
                yref='paper',
                x=0.5, y=1.15,
                showarrow=False,
                font=dict(size=25)
            )
        ]
    )
    fig.add_vline(x='2021-01-15', line_dash='dash', line_color='red')

    return region_text, fig

if __name__ == '__main__':
    app.run(debug=True)