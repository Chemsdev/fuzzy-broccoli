from    sqlalchemy import create_engine
import  os
from    dotenv import load_dotenv
import  pandas as pd
from    sqlalchemy import text 
import  pymysql
import streamlit as st
from tools import *


# ----------------------------------------------------------->

query_table =  """
CREATE TABLE IF NOT EXISTS jeux_olympiques (
    id_resultat INT AUTO_INCREMENT PRIMARY KEY,
    id_resultat_source INT,
    source VARCHAR(255),
    id_athlete_base_resultats INT,
    id_personne INT,
    athlete_nom VARCHAR(255),
    athlete_prenom VARCHAR(255),
    id_equipe INT,
    equipe_en VARCHAR(255),
    id_pays INT,
    pays_en_base_resultats VARCHAR(255),
    classement_epreuve VARCHAR(50),
    performance_finale_texte VARCHAR(255),
    performance_finale FLOAT,
    id_evenement INT,
    evenement VARCHAR(255),
    evenement_en VARCHAR(255),
    categorie_age VARCHAR(100),
    id_edition INT,
    id_competition_sport INT,
    competition_en VARCHAR(255),
    id_type_competition INT,
    type_competition VARCHAR(255),
    edition_saison VARCHAR(50),
    date_debut_edition DATE,
    date_fin_edition DATE,
    id_ville_edition INT,
    edition_ville_en VARCHAR(255),
    id_nation_edition_base_resultats INT,
    edition_nation_en VARCHAR(255),
    id_sport INT,
    sport VARCHAR(255),
    sport_en VARCHAR(255),
    id_discipline_administrative INT,
    discipline_administrative VARCHAR(255),
    id_specialite INT,
    specialite VARCHAR(255),
    id_epreuve INT,
    epreuve VARCHAR(255),
    epreuve_genre VARCHAR(50),
    epreuve_type VARCHAR(50),
    est_epreuve_individuelle BOOLEAN,
    est_epreuve_olympique BOOLEAN,
    est_epreuve_ete BOOLEAN,
    est_epreuve_handi BOOLEAN,
    epreuve_sens_resultat VARCHAR(50),
    id_federation INT,
    federation VARCHAR(255),
    federation_nom_court VARCHAR(100),
    dt_creation DATETIME,
    dt_modification DATETIME,
    annee INT
)
"""

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



# Fonction permettent de vérifier si les données existe déjà dans la db.
def check_db(df):

    # Connexion à la base de données AZURE.
    config = set_confg(liste_connexion=AZURE)
    engine = connect_mysql(config=config)

    # On récupère les référéences déjà présente dans la base de données
    query    = "SELECT id_resultat FROM jeux_olympiques"
    id_in_db = pd.read_sql(query, engine)
    id_in_db = id_in_db['id_resultat'].tolist()
    engine.close()
    
    
    for i in id_in_db:
        
        if 'id_resultat' not in df.columns:
            st.error("Données icompatibles avec la base de données...")
            return False
        
    return True



# Fonction permettent d'insérer les données en db.
def send_data_db(uploaded_file):
    try:
        # Lire le CSV
        df = pd.read_csv(uploaded_file)
        st.success("CSV chargé avec succès !")
        st.write("Aperçu des données :", df.head())

        if st.button("📤 Envoyer dans la base SQL"):
            
            
            if check_db(df=df):
                
                
                # Connexion à la base de données AZURE.
                config = set_confg(liste_connexion=AZURE)
                engine = connect_mysql(config=config)
                
                # Écriture dans la base (remplace si la table existe)
                df.to_sql("jeux_olympiques", con=engine, if_exists='replace', index=False)
                st.success(f"✅ Données insérées dans la table jeux_olympiques avec succès.")
                
            else:
                return False

    except Exception as e:
        st.error(f"❌ Une erreur est survenue : {e}")

# Création de la table
# create_table(name_table="jeux_olympiques", query_table=query_table)

