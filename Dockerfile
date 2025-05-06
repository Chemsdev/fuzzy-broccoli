# On utilise l'image de base Python
FROM python:3.8-slim-buster

# On spécifie le chemin où on souhaite copier l'app dans le conteneur.
WORKDIR /app

# Création du dossier pour les images
RUN mkdir /app/image

# Exécution du fichier requirements pour installer toutes les dépendances nécessaires.
COPY requirements.txt .

# Installation des dépendances Python
RUN pip install --no-cache-dir -r requirements.txt



# ---------------------------------------------------->
# Copier les fichiers dans le dossier main.
COPY app.py            /app
COPY db_init.py       /app
COPY tools.py         /app
# ---------------------------------------------------->

# ---------------------------------------------------->
# Copier les autres fichiers à la racine.
COPY .gitignore    /app/
# ---------------------------------------------------->

# ---------------------------------------------------->
# Port & Lancement de l'app
EXPOSE 8501
CMD ["streamlit", "run", "app.py"]
# ---------------------------------------------------->

# STEP 1 : docker build -t lambdalauncher:lambdalauncher .  
# STEP 2 : docker run -p 8501:8501 lambdalauncher:lambdalauncher
# STEP 3 : Launch http://localhost:8501/