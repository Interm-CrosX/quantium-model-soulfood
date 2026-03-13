from dash import Dash, dcc, html, Output, Input
import pandas as pd
import plotly.graph_objects as go

app = Dash(__name__)

df = pd.read_csv('pink_morsel_sales_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# print(df[:5])


app.layout = html.Div([
    html.H1(children='Pink Morsel Sales Data', style={'textAlign': 'center'}),
    dcc.RadioItems(['north', 'south', 'east', 'west', 'all'], id='region-radio', value='all', inline=True),
    html.Div(id='dd-output-container'),
    dcc.Graph(id='pinkM_Sales'),
])

@app.callback(
[Output('dd-output-container', 'children'),
        Output('pinkM_Sales', 'figure'),],
    [Input('region-radio', 'value')]
)

def update_output(value):
    if value == 'all' or value is None:
        filtered_df = df
        region_text = 'Showing all regions'
    else:
        filtered_df = df[df['region'] == value]
        region_text = f'You have selected {value}'

    fig = go.Figure()
    fig.add_scatter(x=filtered_df['date'], y=filtered_df['sales'])
    fig.update_layout(
        xaxis_title='Date',
        yaxis_title='Sales',
        title='Pink Morsel Sales over time'
    )
    fig.add_vline(x='2021-01-15', line_dash='dash', line_color='red')

    return region_text, fig

if __name__ == '__main__':
    app.run(debug=True)