import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Répartition des catégories")

# Upload du fichier
uploaded_file = st.file_uploader("Importer le fichier Excel", type=["xlsx"])

if uploaded_file:

    # Lire la feuille
    df = pd.read_excel(uploaded_file, sheet_name="Tableau général")

    # Remplir les catégories vides (car elles sont fusionnées dans Excel)
    df["Type produit"] = df["Type produit"].ffill()

    # Compter le nombre de lignes par catégorie
    counts = df["Type produit"].value_counts()

    # Supprimer les lignes de total si besoin
    counts = counts[~counts.index.str.contains("Total|TOTAL", na=False)]

    st.write("Nombre de lignes par catégorie :")
    st.write(counts)

    # Camembert
    fig, ax = plt.subplots()
    ax.pie(counts, labels=counts.index, autopct='%1.1f%%')
    ax.set_title("Répartition des catégories")

    st.pyplot(fig)
