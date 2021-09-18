from logging import PlaceHolder
import dash
import dash_html_components as html
import dash_bootstrap_components as dbc
from data.Article import Article 
from dash.dependencies import Input, Output, State
import dash_core_components as dcc

article = Article()
all_titles = article.get_all_artcile()



table_header = [html.Thead(html.Tr([html.Th("Titres des Articles")]))]

table_body = [html.Tbody([ html.Tr(
                    [html.Td(
                                article.affichage_complet (data['titre'])
                                
                            )]) for ind , data in all_titles.iterrows()])]


index = dbc.Table(table_header + table_body, bordered=True)


