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
                                'font-size': '16px',  # Kích thước font
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
                            html.Img(src="/assets/projects_img2.png", alt="Project 2", className="small-image-2"),
                        ],
                        className="project-image-2",
                    ),
                    html.Div(
                        [
                            html.H3(
                                "2. Algorithm procurement",
                                style={
                                'color': '#352c3e',  # Màu chữ
                                'font-size': '16px',  # Kích thước font
                                'text-align': 'left',  # Căn chỉnh văn bản
                                'font-family': 'Segoe UI Semi Bold, sans-serif',  # Kiểu font chữ
                                'font-weight': 'bold'  # Độ đậm của font chữ
                                }
                            ),
                            html.P("Python"),
                            html.A("Read more", href="/project/algorithm_procurement"),
                        ],
                        className="project-details-2",
                    )
                ],
                className = "project-container-2",
            ),
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(src="/assets/projects3_img1.png", alt="Project 3", className="small-image-3"),
                        ],
                        className="project-image-3",
                    ),
                    html.Div(
                        [
                            html.H3(
                                "3. Excel tuyển dụng",
                                style={
                                'color': '#352c3e',  # Màu chữ
                                'font-size': '16px',  # Kích thước font
                                'text-align': 'left',  # Căn chỉnh văn bản
                                'font-family': 'Segoe UI Semi Bold, sans-serif',  # Kiểu font chữ
                                'font-weight': 'bold'  # Độ đậm của font chữ
                                }
                            ),
                            html.P(
                                "Excel, VBA .",
                                style={
                                'color': '#352c3e',  # Màu chữ
                                'font-size': '14px',  # Kích thước font
                                'text-align': 'left',  # Căn chỉnh văn bản
                                'font-family': 'Segoe UI, sans-serif',  # Kiểu font chữ
                                'font-weight': 'normal'  # Độ đậm của font chữ
                                }
                            ),
                            html.A(
                                "Read more on Github", href="https://github.com/syduc993/Tuyen_dung",target="_blank",
                                style={
                                'color': '#352c3e',  # Màu chữ
                                'font-size': '14px',  # Kích thước font
                                'text-align': 'left',  # Căn chỉnh văn bản
                                'font-family': 'Segoe UI, sans-serif',  # Kiểu font chữ
                                'font-weight': 'normal'  # Độ đậm của font chữ
                                }
                            ),
                        ],
                        className="project-details-3",
                    )
                ],
                className="project-container-3",
            ),            
            html.Div(
                [
                    html.Div(
                        [
                            html.Img(src="/assets/projects4_img1.png", alt="Project 4", className="small-image-4"),
                        ],
                        className="project-image-4",
                    ),
                    html.Div(
                        [
                            html.H3(
                                "4. Excel dashboard",
                                style={
                                'color': '#352c3e',  # Màu chữ
                                'font-size': '16px',  # Kích thước font
                                'text-align': 'left',  # Căn chỉnh văn bản
                                'font-family': 'Segoe UI Semi Bold, sans-serif',  # Kiểu font chữ
                                'font-weight': 'bold'  # Độ đậm của font chữ
                                }
                            ),
                            html.P(
                                "Excel, VBA .",
                                style={
                                'color': '#352c3e',  # Màu chữ
                                'font-size': '14px',  # Kích thước font
                                'text-align': 'left',  # Căn chỉnh văn bản
                                'font-family': 'Segoe UI, sans-serif',  # Kiểu font chữ
                                'font-weight': 'normal'  # Độ đậm của font chữ
                                }
                            ),
                            html.A(
                                "Read more on Github", href="https://github.com/syduc993/Excel-Dashboard",target="_blank",
                                style={
                                'color': '#352c3e',  # Màu chữ
                                'font-size': '14px',  # Kích thước font
                                'text-align': 'left',  # Căn chỉnh văn bản
                                'font-family': 'Segoe UI, sans-serif',  # Kiểu font chữ
                                'font-weight': 'normal'  # Độ đậm của font chữ
                                }
                            ),
                        ],
                        className="project-details-4",
                    )
                ],
                className="project-container-4",
            )
            ],
            className="project-container",
        )
    ]
)
