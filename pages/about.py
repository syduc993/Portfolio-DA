import dash
from dash import dcc, html
import dash_bootstrap_components as dbc

dash.register_page(__name__, path='/about', name='About')

# Khởi tạo layout trang web
layout = html.Div(
    [
        # Phần đầu trang
        html.Div(
            children=[
                # Nhãn chào mừng
                html.Label(
                    "Welcome to my portfolio website!",
                    style={
                        'color': '#352c3e',  # Màu chữ
                        'font-size': '32px',  # Kích thước font
                        'text-align': 'left',  # Căn chỉnh văn bản
                        'font-family': 'Segoe UI Semi Bold, sans-serif',  # Kiểu font chữ
                        'font-weight': 'bold'  # Độ đậm của font chữ
                    }
                ),
                html.Br(),
                # Nhãn mô tả
                html.Label(
                    "Data. Learning. Creativity.",
                    style={
                        'text-align': 'left',  # Căn chỉnh văn bản
                        'color': '#352c3e',  # Màu chữ
                        'font-size': '16px',  # Kích thước font
                        'font-family': 'Segoe UI, sans-serif',  # Kiểu font chữ
                        'font-weight': 'normal'  # Độ đậm của font chữ
                    }
                )
            ],
            style={
                'padding': 10,  # Khoảng cách viền nội dung
                'flex': 1,  # Tự động điều chỉnh kích thước theo trình duyệt
                'display': 'flex',  # Sử dụng flexbox layout
                'flex-direction': 'column',  # Hiển thị các phần tử con theo chiều dọc
                'align-items': 'flex-start'  # Căn chỉnh các phần tử con theo phía trên bên trái
            }
        ),
        # Phần thân trang
        html.Div(
            children=[
                # Hình ảnh
                html.Img(src="/assets/download.jpg", className="img-fluid", style={'width': '75%', 'height': 'auto'})
            ],
            style={
                'padding': 10,  # Khoảng cách viền nội dung
                'flex': 1,  # Tự động điều chỉnh kích thước theo trình duyệt
                'display': 'flex',  # Sử dụng flexbox layout
                'justify-content': 'center',  # Căn chỉnh theo giữa theo chiều ngang
                'align-items': 'center',  # Căn chỉnh theo giữa theo chiều dọc
                'height': '100%'  # Chiều cao của phần tử con
            }
        )
    ],
    style={
        'display': 'flex',  # Sử dụng flexbox layout
        'flex-direction': 'row',  # Hiển thị các phần tử con theo chiều ngang
        'justify-content': 'center',  # Căn chỉnh các phần tử con theo giữa theo chiều ngang
        'align-items': 'center',  # Căn chỉnh các phần tử con theo giữa theo chiều dọc
        'height': '100vh'  # Chiều cao của layout
    }
)