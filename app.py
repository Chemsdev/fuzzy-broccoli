import streamlit as st

from db_init import *

def main():
    st.title("JEUX OLYMPIQUES")
    
    
    # Upload du fichier
    uploaded_file = st.file_uploader("Déposez un fichier CSV ici", type=["csv"])
    if uploaded_file:
    
        send_data_db(uploaded_file=uploaded_file)
        
main()