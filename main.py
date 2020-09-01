import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd

from data import countries_df, totalcase_df, global_df, country_df
from builder import make_table

external_stylesheets = [
    "https://cdn.jsdelivr.net/npm/tailwindcss@1.7.6/dist/tailwind.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
map_figure = px.scatter_geo(
    countries_df,
    size="Confirmed",
    size_max=50,
    hover_data={
        "Confirmed": ":,2f",
        "Deaths": ":,2f",
        "Recovered": ":,2f",
        "Country_Region": False,
    },
    hover_name="Country_Region",
    locations="Country_Region",
    locationmode="country names",
    color="Confirmed",
    template="plotly_dark",
    projection="natural earth",
    title="World Confirmed status",
    color_continuous_scale=px.colors.sequential.Oryel,
    text="Deaths",
)

bar_fig = px.bar(
    totalcase_df,
    x="condition",
    y="count",
    template="plotly_dark",
    color="condition",
    title="Total cases",
    hover_data={
        "count": ":,",
    },
    labels={
        "count": "Counts",
        "condition": "Conditions",
    },
)

app.layout = html.Div(
    children=[
        html.H1(
            children="Corona Dashboard",
            style={"color": "white", "marginBottom": "30px"},
            className="text-3xl hover:underline text-blue-300 font-bold",
        ),
        html.Div(
            children=[
                html.Div(
                    children=[dcc.Graph(id="global_bubble_map", figure=map_figure)],
                    style={"gridColumn": "span 3", "height": "100%"},
                ),
                html.Div(
                    children=[
                        make_table(countries_df),
                    ]
                ),
                html.Div(
                    children=[dcc.Graph(id="total_case_bar", figure=bar_fig)],
                    style={"gridColumn": "span 2", "width": "100%", "height": "100%"},
                ),
                html.Div(
                    children=[
                        dcc.Dropdown(
                            id="country-dropdown",
                            options=[
                                {"label": country, "value": country}
                                for country in countries_df[
                                    "Country_Region"
                                ].sort_values()
                            ],
                            style={
                                "color": "black",
                                "width": "100%",
                                "marginBottom": "10px",
                            },
                        ),
                        html.Div(
                            children="",
                            id="country-fig",
                            style={"width": "100%", "height": "100%"},
                        ),
                    ],
                    style={
                        "display": "flex",
                        "flexDirection": "column",
                        "justifyContent": "start",
                        "alignItems": "center",
                        "width": "100%",
                        "height": "100%",
                        "gridColumn": "span 2",
                    },
                ),
            ],
            style={
                "display": "grid",
                "gridTemplateColumns": "repeat(4, 1fr)",
                "gridGap": "50px",
            },
        ),
    ],
    className="min-h-screen text-center bg-black pt-10 text-white px-10",
    style={
        "fontFamily": "'Open Sans', sans-serif",
    },
)


@app.callback(
    Output(component_id="country-fig", component_property="children"),
    [
        Input(component_id="country-dropdown", component_property="value"),
    ],
)
def on_select(value):
    if value is None:
        fig = px.line(
            global_df(),
            x="date",
            y=["confirmed", "recovered", "death"],
            title="Global daily COVID-19 status",
            hover_data={"value": ":,", "variable": False},
            labels={"value": "cases", "variable": "condition", "date": "Date"},
            template="plotly_dark",
        )
    else:
        fig = px.line(
            country_df(value),
            x="date",
            y=["confirmed", "recovered", "death"],
            title=f"{value} daily COVID-19 status",
            labels={"value": "cases", "variable": "condition", "date": "Date"},
            hover_data={"value": ":,", "variable": False},
            template="plotly_dark",
        )
    fig.update_xaxes(rangeslider_visible=True)
    return dcc.Graph(figure=fig)


if __name__ == "__main__":
    app.run_server(debug=True)
