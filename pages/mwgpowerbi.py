import dash
from dash import dcc, html

dash.register_page(__name__, path='/project/mwgpowerbi', name='Project')

layout = html.Div(
    children=[
        html.Div(
            children=[
                    html.Img(
                        src="/assets/mwgpowerbi.png",
                        alt="Project 1",
                        className="mwgpowerbi-image-1",
                        style={'width': '100%', 'height': 'auto'}
                    ),
            ],
            className="mwgpowerbi-image-1",
        ),
        html.Div(
            children=[
                html.P(
                    ["You can see Power BI Dashboard here: ", html.A("http://procurement.pythonanywhere.com/", href="http://procurement.pythonanywhere.com/")]
                ),
                html.P(
                    "At MWG, we highly value data. Meetings revolve around data, and decisions are made based on data. When I first joined the corporation, our operations department primarily used Excel as the main tool. Below is one of the Excel reports I constructed in the early days."
                ),
                html.Img(
                    src="/assets/image-excel-1.png",
                    alt="Project 1",
                    className="mwgpowerbi-image-1",
                    style={'width': '100%', 'height': 'auto'}
                ),
                html.P(
                    "The drawback of these reports is that they overlook the context of the data.\
                    We can see the difference in metrics between two periods, but we cannot determine the underlying factors contributing to that difference.\
                    We cannot identify which specific days had a positive or negative impact on that difference. Reports of this nature have very low interactivity and weak analytical capabilities. As a result, the ability to effectively harness the data is severely limited."
                ),
                html.P(
                    "When we reach a point where we need a more powerful reporting solution, we should consider building a dashboard using Power BI.\
                    Power BI provides a comprehensive set of tools and features to create interactive and visually appealing dashboards that can provide deeper insights into our data.\
                    With Power BI, we can connect to various data sources, transform and model the data, and create interactive visualizations and reports. The ability to drill down into specific details, apply filters, and perform advanced analytics makes Power BI an excellent choice for building robust and insightful dashboards."
                ),
                html.P(
                    "STEP 1: Download data",
                    style={
                        'color': '#352c3e',  # Màu chữ
                        'font-size': '18px',  # Kích thước font
                        'text-align': 'left',  # Căn chỉnh văn bản
                        'font-family': 'Segoe UI Semi Bold, sans-serif',  # Kiểu font chữ
                        'font-weight': 'bold'  # Độ đậm của font chữ
                        }
                ),
                html.P(
                    "The data was manually downloaded, and it took us anywhere from 20 minutes to 1 hour each day just to download the data. To address this, I developed a tool using the Selenium library in Python to automate the data downloading process."
                ),
                html.P(
                    ["You can find my code here: ", html.A("https://github.com/syduc993/Streanlit-Project", href="https://github.com/syduc993/Streanlit-Project")]
                ),
                html.P(
                    "STEP 2: Transform Data",
                    style={
                        'color': '#352c3e',  # Màu chữ
                        'font-size': '18px',  # Kích thước font
                        'text-align': 'left',  # Căn chỉnh văn bản
                        'font-family': 'Segoe UI Semi Bold, sans-serif',  # Kiểu font chữ
                        'font-weight': 'bold'  # Độ đậm của font chữ
                        }
                ),
                html.P(
                    "We can use Power BI to directly connect with these Excel files. However, it may not be the most efficient approach. There are approximately 1 million rows of data per day for system operations, which translates to processing around 30 million rows of data per month."
                ),
                html.P(
                    "Using Power BI with direct connections to Excel files may indeed result in slower performance given the large volume of data you mentioned. Therefore, your approach of pushing the Excel data into a database and incorporating a data cleaning step before connecting it to Power BI is a wise choice. This allows for better data management and can significantly improve the performance and efficiency of your Power BI reports and dashboards."
                ),
                html.P(
                    "STEP 3: Data Visualization",
                    style={
                        'color': '#352c3e',  # Màu chữ
                        'font-size': '18px',  # Kích thước font
                        'text-align': 'left',  # Căn chỉnh văn bản
                        'font-family': 'Segoe UI Semi Bold, sans-serif',  # Kiểu font chữ
                        'font-weight': 'bold'  # Độ đậm của font chữ
                        }
                ),
                html.P(
                    "In this section, I will present some special charts that cannot be handled using conventional techniques in Power BI. Here is an example image below."
                ),
                html.Div(
                    children=[
                            html.Img(
                                src="/assets/mwgpowerbi - 2.png",
                                alt="Project 1",
                                className="mwgpowerbi-image-1",
                                style={'width': '50%', 'height': 'auto'}
                            ),
                    ],
                    className="mwgpowerbi-image-1",
                ),
                html.P(
                    "Can you see the image drawn by Vega? It shows the changes in import prices. The color shifting from dark to light indicates a gradual decrease in purchasing prices. Meanwhile, the image above drawn by Power Bi failed to accomplish that."
                )
            ]
        ),
    ]
)