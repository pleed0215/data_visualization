import dash_html_components as html


def make_table(df):
    return html.Table(
        children=[
            html.Thead(
                children=[
                    html.Tr(
                        children=[
                            html.Th(
                                column_name.replace("_", " "),
                            )
                            for column_name in df.columns
                        ],
                        className="grid grid-cols-4 h-20 border-b border-white",
                        style={"alignItems": "center"},
                    ),
                ],
            ),
            html.Tbody(
                children=[
                    html.Tr(
                        children=[html.Td(column) for column in value],
                        className="grid grid-cols-4 h-20 border-b border-white",
                        style={"alignItems": "center"},
                    )
                    for value in df.values
                ],
                style={"height": "50vh"},
                className="block overflow-y-auto",
            ),
        ],
        style={"height": "50vh"},
    )
