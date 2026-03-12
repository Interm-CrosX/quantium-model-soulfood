from dash import Dash, dcc, html, Output, Input
import pandas as pd
import plotly.graph_objects as go

app = Dash(__name__)

df = pd.read_csv('pink_morsel_sales_data.csv')
df['date'] = pd.to_datetime(df['date'])
df = df.sort_values('date')

# print(df[:5])


fig = go.Figure()
fig.add_scatter(
    x=df['date'], y=df['sales'])
fig.update_layout(
    xaxis_title="Date",
    yaxis_title="Sales",
    title="Pink Morsel Sales over time",
)
fig.add_vline(
    x='2021-01-15', line_dash='dash', line_color='red',)

app.layout = html.Div([
    html.H1(children='Pink Morsel Sales Data', style={'textAlign': 'center'}),
    dcc.Dropdown(['north', 'south', 'east', 'west'], value='north', id='region-dropdown', placeholder='Select a region...'),
    html.Div(id='dd-output-container'),
    dcc.Graph(id='pinkM_Sales', figure=fig),
])

@app.callback(
[Output('dd-output-container', 'children'),
        Output('pinkM_Sales', 'figure'),],
    [Input('region-dropdown', 'value')]
)

def update_output(value):
    filtered_df = df[df['region'] == value]
    return f'You have selected {value}', fig



if __name__ == '__main__':
    app.run(debug=True)