import dash
from dash import dcc, html

dash.register_page(__name__, path='/', name='CV')

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
                        html.Img(src="/assets/avatar.jpg", alt="Project 1", className="small-image-1",style={'width': '62.5%', 'height': 'auto'})
                    ],
                    className="cv-image-1"
                ),
                html.Div(
                    [
                        html.P([html.Strong("Date of birth:"), "          07/06/1993"]),
                        html.P([html.Strong("Gender:"), "                   Nam"]),
                        html.P([html.Strong("Contact number:"), "    0876762208"]),
                        html.P([html.Strong("Email:"), "                       le.syduc.993@gmail.com"]),
                        html.P([html.Strong("Adress:"), "                    Bắc Sơn Bỉm Sơn Thanh Hóa"]),
                    ],
                    className="cv-info"
                )
            ],
            className="cv-container-1"
        ),
        html.H2(
            "EDUCATION QUALIFICATIONS",
            style={"font-size": "16px","margin-bottom": "10px"}
        ),
        html.Hr(className="solid-line"),
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
                    html.P(html.Strong("Ha Noi University of industry")),
                    html.P("Information Technology"),
                    ],
                    className="info-education"
                )
            ],
            className="cv-container-2"
        ),
        html.H2(
            "WORK EXPERIENCES",
            style={"font-size": "16px","margin-bottom": "10px"}
        ),
        html.Hr(className="solid-line"),
        html.Div(
            [
                html.Div(
                    [
                    html.P(html.Strong("MWG Corporation")),
                    html.P("2022 - Now"),
                    ],
                    className="year-career-1"
                ),
                html.Div(
                    [
                    html.P(html.Strong("Forecasting and Analysis Department Staff")),
                    html.P(html.Strong("1. Operating the procurement and distribution system")),
                    html.P("- Calculating and analyzing the quantity of goods to be purchased and distributed to supermarkets within the system."),
                    html.P("- Monitoring and evaluating the effectiveness of goods allocation for the supermarket system."),
                    html.P(html.Strong("2. The reporting system for description and analysis")),
                    html.P("- Building a dashboard to monitor the entire process from system-supplier-warehouse-logistics to the business situation of the supermarket and its products."),
                    html.P("- Reporting weekly and monthly business performance results to the management."),
                    html.P("- Analyzing business effectiveness, conducting experiments, and evaluating promotional programs."),
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
                    html.P(html.Strong("TokyoLife Company")),
                    html.P("2017 - 2021"),
                    ],
                    className="year-career-2"
                ),
                html.Div(
                    [
                    html.P(html.Strong("1. TokyoLife Store’s Manager")),
                    html.P("- Using excel software to create files of checking warehouse, solving problems of checking merchandise and supporting display."),
                    html.P("- Create of automatic reports to get control of strore situation store."),
                    html.P(html.Strong("2. Operation support management")),
                    html.P("- Create excel software as supporting software to recruit and choose candidates."),
                    html.P("- Implementing analysis and report area’s data."),
                    html.P("- Research proposing solutions to support the sales department."),
                    ],
                    className="info-career-2"
                )
            ],
            className="cv-container-4"
        ),
        html.H2(
            "SKILLS",
            style={"font-size": "16px","margin-bottom": "10px"}
        ),
        html.Hr(className="solid-line"),
        html.P(html.Strong("Technical skills:")),
        html.P([html.Strong("- Python:")," Data analysis using Pandas, NumPy, and Polars. Data visualization using Plotly, and deploying a web application on the Flask framework"]),
        html.P([html.Strong("- Power B:"), " Data processing with DAX functions. Using Vega to visualize certain images that are not well-supported by Power BI."]),
        html.P([html.Strong("- SQL:"), " Deploying a PostgreSQL database for personal use to store and process data"]),
        html.P([html.Strong("- Excel:"), " Proficient in Excel, with the ability to write VBA code to enhance work tasks."]),
        html.P(html.Strong("Business skill:")),
        html.P("- Leadership, Time Management, Problem solving"),
        html.H2(
            "PROJECTS",
            style={"font-size": "16px","margin-bottom": "10px"}
        ),
        html.Hr(className="solid-line"),
        html.A([html.Strong("PowerBI Dashboard: "), "http://procurement.pythonanywhere.com/"], href="http://procurement.pythonanywhere.com/", style={"text-decoration": "none", "color": "inherit"}, target="_blank"),
        html.P("Implementing a project using Python to process Excel files (50 million rows - update 1 million new rows daily), Power BI for data visualization, and Flask for deploying a web application for end users."),
        html.A([html.Strong("EDA - SALE: "), "https://github.com/syduc993/EDA_Sale"], href="https://github.com/syduc993/EDA_Sale", style={"text-decoration": "none", "color": "inherit"}, target="_blank"),
        html.P("Analyzing retail data using Pandas, SQL, Plotly, and Scikit-learn."),
        html.A([html.Strong("Excel DashBoard: "), "https://github.com/syduc993/Excel-Dashboard"], href="https://github.com/syduc993/Excel-Dashboard", style={"text-decoration": "none", "color": "inherit"}, target="_blank"),
        html.P(""),
        html.A([html.Strong("Excel Recruitment: "), "https://github.com/syduc993/Tuyen_dung"], href="https://github.com/syduc993/Tuyen_dung", style={"text-decoration": "none", "color": "inherit"}, target="_blank"),
    ]
)