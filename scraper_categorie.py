import requests
import csv
from bs4 import BeautifulSoup

# URL de la page à scraper
url = "https://books.toscrape.com/catalogue/rip-it-up-and-start-again_986/index.html"

# Effectuer une requête GET pour récupérer la page
response = requests.get(url)

if response.status_code == 200:
    print("C'est bon, j'ai eu un retour du site !")

    # Analyse du contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Définition des champs extraits et leurs sélecteurs CSS correspondants
    champs_extraits = {
        "div.col-sm-6.product_main > h1": soup.find("div", class_="col-sm-6 product_main").find("h1").get_text(),
        # "p.price_color": soup.find("p", class_="price_color").get_text(), <-- si je veux le champs couleur
        # "p.instock.availability": soup.find("p", class_="instock availability").get_text(strip=True) <-- si je veux le champs dispo
    }

    # Nom du fichier CSV
    nom_fichier = "donnees_extraites.csv"

    # Création et écriture du fichier CSV
    with open(nom_fichier, mode="w") as file:
        writer = csv.writer(file)

        # Écriture de l'en-tête avec les sources des données (titres de colonnes)
        writer.writerow(champs_extraits.keys())

        # Écriture des valeurs extraites
        writer.writerow(champs_extraits.values())

    print(f"Le fichier {nom_fichier} a été créé avec succès !")