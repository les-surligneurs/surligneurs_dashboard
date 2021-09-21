import os
import json
import pandas as pd
from data.Connector import Connector
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash import dcc


class  Article:
    def __init__(self) -> None:

        path  = os.getcwd() + "/config/" +  "config.json"
        with open(path, "r") as read_file:
            config = json.load(read_file)
        self.cnt = Connector(config["param"]["user"], config["param"]["host"], config["param"]["mdp"], config["param"]["port"], config["param"]["db"])
        self.cur = self.cnt.connect()
        self.cnt.conn.autocommit = True


    # apartir du titre elle retourne toutes les info de cette article pour les afficher ensuite sur une page
    def affichage_complet(self , titre :str  ) -> list ():
        info = pd.read_sql_query("  select  * from commentaire where titre =  " +"\'"  + str (titre) + "\';" , self.cnt.conn )

        row1 = html.Tr([html.Td("Titre : "), html.Td(info["titre"])])
        row2 = html.Tr([html.Td("Corps : "), html.Td(info["corps"])])
        row3 = html.Tr([html.Td("commentaire: "), html.Td(info["resume"])])
        row4 = html.Tr([html.Td("Tag : "), html.Td(info["tag"])])
        row5 = html.Tr([html.Td("Url : "), html.Td(dcc.Link (href = info["url"]))])

        info = pd.read_sql_query("  select  * from resnlp where titrecomm =  \'" + str (titre)  +"\' ;" , self.cnt.conn )

        row9 = html.Tr([html.Td("NNP : "), html.Td(info["namedentities"])])

        table_body = [html.Tbody([row1 , row2 , row3 , row4 , row5 , row9 ])]

        return dbc.Table( table_body, bordered=True ,dark=True,hover=True,responsive=True, striped=True)



    #retourne tout les titres des articles pour les afficher ensuite sur une page ou chaque lien est cliquable
    def get_all_artcile(self ):
        all_titles  = pd.read_sql_query("  select  titre  from commentaire ;", self.cnt.conn )
        return all_titles
