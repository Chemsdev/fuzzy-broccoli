from    sqlalchemy import create_engine
import  os
from    dotenv import load_dotenv
import  pandas as pd
from    sqlalchemy import text 
import  pymysql




# ----------------------------------------------------------->

query_table =  """
    CREATE TABLE IF NOT EXISTS table... (
        id_formation INT AUTO_INCREMENT PRIMARY KEY,
        ref VARCHAR(100),
        titre VARCHAR(255),
        sous_titre VARCHAR(255),
        resume TEXT,
        objectives TEXT,
        schedule TEXT,
        prerequisite TEXT,
        methods TEXT,
        keywords TEXT
    )
""",

# ----------------------------------------------------------->

# Fonction permettant de créer une table.
def create_table(name_table: str, query_table: str):
    config       = set_confg(liste_connexion=AZURE)
    engine_azure = connect_mysql(config=config)
    try:
        with engine_azure as connection:
            connection.execute(text(query_table)) 
        print(f"Table '{name_table}' créée avec succès.")
        
    except Exception as e:
        print(f"Erreur lors de la création de la table {name_table} : {e}")
    
    engine_azure.close()
    
# ----------------------------------------------------------->

# Création de la table
reate_table(name_table="jeux_olympiques", query_table=query_table)

