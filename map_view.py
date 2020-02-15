import plotly.graph_objects as go
import pandas as pd

if __name__ == '__main__':
    df = pd.read_csv('https://raw.githubusercontent.com/plotly/datasets/master/2011_us_ag_exports.csv')

    fig = go.Figure(data=go.Choropleth(
        locations=df['code'],  # Spatial coordinates
        z=df['total exports'].astype(float),  # Data to be color-coded
        locationmode='USA-states',  # set of locations match entries in `locations`
        colorscale='Reds',
        colorbar_title="People",
    ))

    fig.update_layout(
        title_text='FluTrax Flu map',
        geo_scope='usa',  # limite map scope to USA
    )

    fig.show()
