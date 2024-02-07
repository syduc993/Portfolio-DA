import dash
from dash import dcc, html

dash.register_page(__name__, path='/cv', name='CV')

layout = html.Div(
    [
        html.H1(
            "Lê Sỹ Đức",
            style={"margin-bottom": "10px"}
        ),
        html.P(
            "Data Analyst"
        ),
        html.Div(
            [
                html.Div(
                    [
                        html.Img(src="/assets/avatar.jpg", alt="Project 1", className="small-image-1",style={'width': '42.5%', 'height': 'auto'})
                    ],
                    className="cv-image-1"
                ),
                html.Div(
                    [
                        html.P("Ngày sinh:	 07/06/1993"),
                        html.P("Giới tính:	 Nam"),
                        html.P("Điện thoại:	 0876762208"),
                        html.P("Email:	 le.syduc.993@gmail.com"),
                        html.P("Địa chỉ:	 Bắc Sơn Bỉm Sơn Thanh Hóa"),
                    ],
                    className="cv-info"
                )
            ],
            className="cv-container-1"
        ),
        html.H2(
            "MỤC TIÊU NGHỀ NGHIỆP",
            style={"margin-bottom": "10px"}
        ),
        html.P("- Nhanh chóng tiếp cận được các dự án thực tế, qua đó xây dựng được hướng phát triển bản thân trở thành Junior Data Analysttrong 1 năm tới "),
        html.P("- Mong muốn được phân tích những dữ liệu đem đến quyết định chính xác cho doanh nghiệp để nâng cao hiệu quả kinh doanh "),
        html.H2(
            "HỌC VẤN",
            style={"margin-bottom": "10px"}
        ),

        html.Div(
            [
                html.Div(
                    [
                    html.P("10/2011 - 05/2014"),
                    ],
                    className="year-education"
                ),
                html.Div(
                    [
                    html.P("Đại học Công Nghiệp Hà Nội"),
                    html.P("Chuyên ngành: Công nghệ thông tin"),
                    ],
                    className="info-education"
                )
            ],
            className="cv-container-2"
        ),

        html.H2(
            "KINH NGHIỆM LÀM VIỆC",
            style={"margin-bottom": "10px"}
        ),

        html.Div(
            [
                html.Div(
                    [
                    html.P("Bách Hóa Xanh - Tập đoàn MWG"),
                    html.P("2022 - Hiện tại"),
                    ],
                    className="year-career-1"
                ),
                html.Div(
                    [
                    html.P("NHÂN VIÊN BỘ PHẬN DỰ BÁO VÀ PHÂN TÍCH BÁCH HÓA XANH"),
                    html.P("1. Vận hành hệ thống mua chia"),
                    html.P("- Tính toán và phân tích số lượng hàng hóa mua và phân phối cho các siêu thị trong hệ thống."),
                    html.P("- Theo dõi và đánh giá hiệu quả phân bổ hàng hóa cho hệ thống siêu thị."),
                    html.P("2. Hệ thống báo cáo mô tả và phân tích"),
                    html.P("- Xây dựng Dashboard theo dõi toàn bộ quy trình từ hệ thống - nhà cung cấp - kho vận - tình hình kinh doanh của siêu thị, sản phẩm."),
                    html.P("- Báo cáo kết quả hoạt động kinh doanh theo tuần, tháng cho cấp quản lý."),
                    html.P("- Phân tích hiệu quả kinh doanh, thử nghiệm và các chương trình khuyến mãi."),
                    ],
                    className="info-career-1"
                )
            ],
            className="cv-container-3"
        ),

        html.Div(
            [
                html.Div(
                    [
                    html.P("Công ty TokyoLife"),
                    html.P("2017 - 2021"),
                    ],
                    className="year-career-2"
                ),
                html.Div(
                    [
                    html.P("1. QUẢN LÝ CỬA HÀNG TOKYOLIFE"),
                    html.P("- Phát triển và xây dựng file kiểm soát kho bằng Microsoft Excel, giúp kiểm soát hàng hóa và hỗ trợ trưng bày hiệu quả trong cửa hàng."),
                    html.P("- Xây dựng báo cáo tự động để kiểm soát tình hình cửa hàng."),
                    html.P("2. QUẢN LÝ HỖ TRỢ VẬN HÀNH"),
                    html.P("- Viết excel như 1 phần mềm để hỗ trợ tuyển dụng và chọn lọc ứng viên."),
                    html.P("- Thực hiện phân tích và báo cáo số liệu của khu vực."),
                    html.P("- Nghiên cứu đề xuất các phương án hỗ trợ khối sale."),
                    ],
                    className="info-career-2"
                )
            ],
            className="cv-container-4"
        ),
        html.H2(
            "KỸ NĂNG",
            style={"margin-bottom": "10px"}
        ),
        html.P("Python: Phân tích dữ liệu bằng Pandas, numpy, polars. Trực quan hóa dữ liệu bằng plotly và triển khai 1 ứng dụng lên nền tảng web bằng flask"),
        html.P("Power BI: Xử lý dữ liệu với Dax Funcition. Sử dụng vega để trực quan hóa 1 số hình ảnh không được hỗ trợ tốt bởi Power BI"),
        html.P("SQL: Triển khai 1 postgresql cho cá nhân nhằm lưu trữ và sử lý dữ liệu"),
        html.P("Excel: Thành thạo các hàm excel, có khả năng viết VBA để bổ trợ công việc"),
        html.P([
                html.Span( "Excel: ",style={"font-weight": "bold"}),
                "Thành thạo các hàm excel, có khả năng viết VBA để bổ trợ công việc"
                ]),
        html.H2(
            "DỰ ÁN",
            style={"margin-bottom": "10px"}
        ),
        html.P("PowerBI DashBoard:   http://procurement.pythonanywhere.com/"),
        html.P("Triển khai một dự án sử dụng Python để xử lý các tệp Excel (50 triệu dòng - update 1 triệu dòng mới mỗi ngày), Power BI để trực quan hóa dữ liệu và Flask để triển khai ứng dụng web cho người dùng cuối. "),
        html.P("EDA - SALE: https://github.com/syduc993/EDA_Sale"),
        html.P("Phân tích bán lẻ sử dụng Pandas, SQL, PLotly, Sklearn"),
        html.P("Excel DashBoard:	https://github.com/syduc993/Excel-Dashboard"),
        html.P("Excel Tuyển dụng:	https://github.com/syduc993/Tuyen_dung"),
    ]
)