import os 
import json
import pandas as pd 
from data.Connector import Connector



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
        pass 


    #retourne tout les titres des articles pour les afficher ensuite sur une page ou chaque lien est cliquable 
    def get_all_artcile(self ):
        all_titles  = pd.read_sql_query("  select  titre  from commentaire ;", self.cnt.conn ) 
        return all_titles



        
