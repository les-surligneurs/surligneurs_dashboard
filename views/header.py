import dash
import dash_core_components as dcc
import dash_html_components as html
import os
import json
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px



# Conteneur du menu
header = html.Div(
                className="Header",
                children=[html.Header(
                                    className="header",
                                    children=[
                                        #Bannière si pas besoin juste mette 'display:none'
                                        html.Div(
                                                className="header banner",
                                        ),
                                        #menu avec les liens
                                        html.Div(
                                                className="header menu",
                                                children=[
                                                    html.Div(
                                                        className='logo_uvsq',
                                                        children=[
                                                            html.A (
                                                                children=[
                                                                    html.Img(
                                                                        src="/assets/icon/logo-david.png",
                                                                        alt="Logo de l'université de Versailles"
                                                                    )
                                                                ],
                                                                className="logo_lien",
                                                                href="https://www.uvsq.fr/"
                                                            )
                                                        ]
                                                    ),
                                                    html.Div(
                                                        className="logo_github",
                                                        children=[
                                                            html.A(
                                                                children=[
                                                                    html.Img(
                                                                        src="/assets/icon/github_white.svg",
                                                                        alt="logo github"
                                                                    )
                                                                ],
                                                                id="Github",
                                                                href="https://github.com/les-surligneurs"
                                                            )
                                                        ]
                                                    )
                                                ]
                                            )

                                    ]
                            )
                        ]
        )
