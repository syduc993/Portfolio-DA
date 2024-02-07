from dash import Dash, html, dcc
import dash


app = Dash(__name__, pages_folder='pages', use_pages=True, assets_folder='assets')


# app.layout = html.Div(
#     style={"width": "80%", "margin": "auto"},
#     children=[
#         html.Br(),
#         html.Div(
#             style={"text-align": "center"},
#             children=[
#                 dcc.Link(
#                     page['name'],
#                     href=page["relative_path"],
#                     style={"text-decoration": "none", "color": "#352c3e", "font-size": "1.2rem",'font-family': 'Segoe UI, sans-serif', "margin-right": "20px"}
#                 )
#                 for page in dash.page_registry.values()
#             ]
#         ),
#         dash.page_container
#     ]
# )

page_links = [
    dcc.Link('Home', href='/', style={"text-decoration": "none", "color": "#352c3e", "font-size": "1.2rem",'font-family': 'Segoe UI, sans-serif', "margin-right": "20px"}),
    dcc.Link('CV', href='/cv', style={"text-decoration": "none", "color": "#352c3e", "font-size": "1.2rem",'font-family': 'Segoe UI, sans-serif', "margin-right": "20px"}),
    dcc.Link('Project', href='/project', style={"text-decoration": "none", "color": "#352c3e", "font-size": "1.2rem",'font-family': 'Segoe UI, sans-serif', "margin-right": "20px"})
]

app.layout = html.Div(
    style={"width": "80%", "margin": "auto"},
    children=[
        html.Br(),
        html.Div(
            style={"text-align": "center"},
            children=page_links
        ),
        dash.page_container
    ]
)

if __name__ == '__main__':
    app.run(debug=True)