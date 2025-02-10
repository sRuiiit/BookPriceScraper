import requests
import csv
import os
from bs4 import BeautifulSoup

# URL de la page d'accueil
BASE_URL = "https://books.toscrape.com/"

# Créer un dossier pour stocker les fichiers CSV
CSV_FOLDER = "CSVparcategorie"
os.makedirs(CSV_FOLDER, exist_ok=True)


# Fonction pour récupérer la liste des catégories
def get_categories():
    url = BASE_URL + "index.html"
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Erreur lors de l'accès à la page d'accueil ({response.status_code})")
        return {}

    soup = BeautifulSoup(response.content, "html.parser")

    categories_section = soup.select("aside div.side_categories ul li ul li a")
    categories = {}

    for category in categories_section:
        nom_categorie = category.get_text(strip=True)
        url_categorie = os.path.join(BASE_URL, category["href"])
        categories[nom_categorie] = url_categorie

    print(f"{len(categories)} catégories trouvées")
    return categories


# Fonction pour scraper tous les livres d'une catégorie
def scrape_books(categorie, url):
    print(f"Scraping de la catégorie : {categorie}")
    livres = []
    page = 1

    while True:
        page_url = url.replace("index.html", f"page-{page}.html") if page > 1 else url
        response = requests.get(page_url)

        if response.status_code != 200:
            print(f"Fin du scraping pour {categorie}, {len(livres)} livres trouvés")
            break

        soup = BeautifulSoup(response.content, "html.parser")

        for livre in soup.find_all("article", class_="product_pod"):
            titre = livre.h3.a["title"]
            prix = livre.find("p", class_="price_color").get_text()
            disponibilite = livre.find("p", class_="instock availability").get_text(strip=True)

            livres.append({"titre": titre, "prix": prix, "disponibilite": disponibilite})

        page += 1

    return livres


# Fonction pour sauvegarder les livres dans un fichier CSV
def save_books_to_csv(categorie, livres):
    nom_fichier = os.path.join(CSV_FOLDER, f"{categorie.replace(' ', '_').lower()}.csv")

    with open(nom_fichier, mode="w") as file:
        writer = csv.DictWriter(file, fieldnames=["titre", "prix", "disponibilite"])
        writer.writeheader()
        writer.writerows(livres)

    print(f"Fichier '{nom_fichier}' créé avec {len(livres)} livres")


# Exécution directe du script
categories = get_categories()

for categorie, url in categories.items():
    livres = scrape_books(categorie, url)
    if livres:
        save_books_to_csv(categorie, livres)