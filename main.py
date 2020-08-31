import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd

from data import countries_df
from builder import make_table

external_stylesheets = [
    "https://cdn.jsdelivr.net/npm/tailwindcss@1.7.6/dist/tailwind.min.css",
    "https://fonts.googleapis.com/css2?family=Open+Sans&display=swap",
]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options

app.layout = html.Div(
    children=[
        html.H1(
            children="Corona Dashboard",
            style={"color": "white"},
            className="text-3xl hover:underline text-blue-300 font-bold",
        ),
        html.Div(children=[make_table(countries_df)]),
    ],
    className="min-h-screen text-center bg-black pt-10 text-white",
    style={"fontFamily": "'Open Sans', sans-serif"},
)

map_figure = px.scatter_geo(countries_df)
map_figure.show()

if __name__ == "__main__":
    app.run_server(debug=True)