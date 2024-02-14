import dash
from dash import dcc, html

dash.register_page(__name__, path='/project/algorithm_procurement', name='Project')

layout = html.Div(
    children=[
        html.Div(
            children=[
                    html.P("Please take a look at the table below."),
                    html.Img(
                        src="/assets/projects2_img2.png",
                        alt="Project 1",
                        className="algorithm-image-1",
                        style={'width': '50%', 'height': 'auto'}
                    ),
            ],
            className="algorithm-image-1",
        ),
        html.Div(
            children=[
                html.P(
                   " We have one product and 20 supermarkets. Each supermarket will make purchases on a different day. You can see that the quantity of goods purchased each day is uneven. The highest day requires double the amount of goods compared to the lowest day."
                ),
                html.P("Facing the uneven quantity of goods purchased at the supermarkets in our retail chain, the supplier has encountered difficulties in predicting and planning the amount of goods to be prepared for Bách Hóa Xanh (BHX).\
                        This situation has caused not only inconvenience for the supplier but also a loss of trust. To address this issue, I have developed an algorithm to ensure that the daily quantity of goods to be purchased does not vary too much.\
                        This has brought significant benefits for both the supplier and BHX because the reliability of the supplier and the favorable prices they provide to BHX have been maintained.")
            ]
        ),
    ]
)