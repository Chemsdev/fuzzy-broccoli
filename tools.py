
from   dotenv     import load_dotenv
from   sqlalchemy import create_engine
from   sqlalchemy import text 
import pandas     as pd 
import pymysql
import os



# ----------------------------------------------------------->

# Fonction configuration ENV.
def set_confg(liste_connexion:list):
    load_dotenv()
    host     = os.environ.get(liste_connexion[0])
    user     = os.environ.get(liste_connexion[1])
    password = os.environ.get(liste_connexion[2])
    database = os.environ.get(liste_connexion[3])
    config = {
        "host"     : host,
        "user"     : user,
        "password" : password,
        "database" : database,
    }  
    return config

# ----------------------------------------------------------->

# Fonction connexion SQL.
def connect_mysql(config:dict):
    host     = config.get('host','')
    user     = config.get('user','')
    password = config.get('password','')
    database = config.get('database','')
    engine   = create_engine(f'mysql+pymysql://{user}:{password}@{host}/{database}')
    print(config)
    return engine.connect()

# ----------------------------------------------------------->


# AZURE.
AZURE = [
    "DB_HOST",
    "DB_USERNAME",
    "DB_PASSWORD",
    "DB_DATABASE"
]