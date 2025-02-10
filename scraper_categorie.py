import requests
import csv
from bs4 import BeautifulSoup

# URL de la catégorie "Nonfiction"
url = "https://books.toscrape.com/catalogue/category/books/nonfiction_13/index.html"

# Effectuer une requête GET pour récupérer la page
response = requests.get(url)

if response.status_code == 200:
    print("C'est bon, j'ai eu un retour du site !")

    # Analyse du contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Liste pour stocker les livres extraits
    livres = []

    # Sélectionner tous les articles de livres sur la page
    for livre in soup.find_all("article", class_="product_pod"):
        titre = livre.h3.a["title"]  # Récupérer le titre du livre
        prix = livre.find("p", class_="price_color").get_text()  # Prix du livre
        disponibilite = livre.find("p", class_="instock availability").get_text(strip=True)  # Stock

        # Ajouter les informations dans une liste de dictionnaires
        livres.append({
            "Titre": titre,
            "Prix": prix,
            "Disponibilité": disponibilite
        })

    # Nom du fichier CSV
    nom_fichier = "livres_nonfiction.csv"

    # Création et écriture du fichier CSV
    with open(nom_fichier, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=["Titre", "Prix", "Disponibilité"])

        # Écrire l'en-tête des colonnes
        writer.writeheader()

        # Écrire les livres dans le fichier CSV
        writer.writerows(livres)

    print(f"Le fichier {nom_fichier} a été créé avec succès !")

else:
    print("Erreur lors de la récupération de la page :", response.status_code)