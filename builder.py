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
                        className="grid grid-cols-4 h-20",
                        style={"alignItems": "center"},
                    ),
                ],
            ),
            html.Tbody(
                children=[
                    html.Tr(
                        children=[
                            html.Td(column, className="border-b border-white w-1/4")
                            for column in value
                        ],
                        className="grid grid-cols-4 h-20",
                    )
                    for value in df.values
                ],
                style={"height": "50vh"},
                className="block overflow-y-auto",
            ),
        ],
        style={"height": "50vh"},
    )
