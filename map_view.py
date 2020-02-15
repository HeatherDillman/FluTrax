import pandas as pd
import plotly.express as px


def encode_date(row):
    return f"{row['Month']}/{row['Day']}/{row['Year']}"


def show_graph(data: pd.DataFrame):
    data = data.copy()
    data.sort_values(by=['Year', 'Month', 'Day'], inplace=True)
    data.reset_index(drop=True, inplace=True)
    data['Date'] = data.apply(encode_date, axis=1)
    fig = px.choropleth(data,
                        locations="State",
                        color="Population",
                        locationmode='USA-states',
                        hover_name="State",
                        color_continuous_scale='reds',
                        animation_frame="Date",
                        range_color=(data['Population'].min(), data['Population'].max()))
    fig.update_layout(
        title_text='FluTrax Map',
        geo_scope='usa'
    )
    fig.show()


if __name__ == '__main__':
    df = pd.read_csv('data.csv')
    show_graph(df)
