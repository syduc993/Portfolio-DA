import dash
from dash import dcc, html

dash.register_page(__name__, path='/project', name='Project')

layout = html.Div(
    [
        html.H1("Projects"),
        html.Div(
            [
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(src="/assets/untitled.png", alt="Project 1", className="small-image-1"),
                        ],
                        className="project-image-1",
                    ),
                    html.Div(
                        [
                            html.H3(
                                "1. Power BI Dashboard in MWG",
                                style={
                                'color': '#352c3e',  # Màu chữ
                                'font-size': '26px',  # Kích thước font
                                'text-align': 'left',  # Căn chỉnh văn bản
                                'font-family': 'Segoe UI Semi Bold, sans-serif',  # Kiểu font chữ
                                'font-weight': 'bold'  # Độ đậm của font chữ
                                }
                            ),
                            html.P(
                                "Python, Dax, Vega ...",
                                style={
                                'color': '#352c3e',  # Màu chữ
                                'font-size': '14px',  # Kích thước font
                                'text-align': 'left',  # Căn chỉnh văn bản
                                'font-family': 'Segoe UI, sans-serif',  # Kiểu font chữ
                                'font-weight': 'normal'  # Độ đậm của font chữ
                                }
                            ),
                            html.A(
                                "Read more", href="/project/mwgpowerbi",
                                style={
                                'color': '#352c3e',  # Màu chữ
                                'font-size': '14px',  # Kích thước font
                                'text-align': 'left',  # Căn chỉnh văn bản
                                'font-family': 'Segoe UI, sans-serif',  # Kiểu font chữ
                                'font-weight': 'normal'  # Độ đậm của font chữ
                                }
                            ),
                        ],
                        className="project-details-1",
                    )
                ],
                className="project-container-1",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(src="/assets/project2.jpeg", alt="Project 2", className="small-image-2"),
                        ],
                        className="project-image-2",
                    ),
                    html.Div(
                        [
                            html.H3("Project 2"),
                            html.P("Mô tả ngắn về dự án 2..."),
                            html.A("Read more", href="/project/mwgpowerbi"),
                        ],
                        className="project-details-2",
                    )
                ],
                className = "project-container-2",
            )
            ],
            className="project-container",
        )
    ]
)
