import requests
import csv
import os
from bs4 import BeautifulSoup
import re
from urllib.parse import urljoin

# URL de la page d'accueil
BASE_URL = "https://books.toscrape.com/"

# Créer un dossier pour stocker les fichiers CSV
CSV_FOLDER = "CSVparcategorie"
os.makedirs(CSV_FOLDER, exist_ok=True)

# Ajouter ces constantes après les existantes
IMAGES_FOLDER = "images_couvertures"
os.makedirs(IMAGES_FOLDER, exist_ok=True)


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


def nettoyer_nom_fichier(titre):
    """Nettoie le titre pour créer un nom de fichier valide"""
    # Garder uniquement les 50 premiers caractères et remplacer les caractères spéciaux
    titre_court = titre[:50]
    titre_propre = re.sub(r'[^a-zA-Z0-9\s-]', '', titre_court)
    return titre_propre.strip().replace(' ', '_').lower()


def telecharger_image(url, chemin_fichier):
    """Télécharge une image depuis son URL"""
    try:
        response = requests.get(url)
        if response.status_code == 200:
            with open(chemin_fichier, 'wb') as f:
                f.write(response.content)
            return True
        return False
    except Exception as e:
        print(f"Erreur lors du téléchargement de l'image: {e}")
        return False


# Fonction pour scraper tous les livres d'une catégorie
def scrape_books(categorie, url):
    print(f"Scraping de la catégorie : {categorie}")
    livres = []
    page = 1
    
    # Créer le dossier pour cette catégorie
    categorie_folder = os.path.join(IMAGES_FOLDER, categorie.replace(' ', '_').lower())
    os.makedirs(categorie_folder, exist_ok=True)

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
            
            # Récupération de l'URL de l'image
            image_relative = livre.find("img")["src"]
            image_url = urljoin(BASE_URL, image_relative)
            
            # Création du nom de fichier pour l'image
            nom_fichier = f"{nettoyer_nom_fichier(titre)}.jpg"
            chemin_image = os.path.join(categorie_folder, nom_fichier)
            
            # Téléchargement de l'image
            succes_telechargement = telecharger_image(image_url, chemin_image)
            
            livres.append({
                "titre": titre, 
                "prix": prix, 
                "disponibilite": disponibilite,
                "image_url": image_url,
                "image_locale": chemin_image if succes_telechargement else "non_telecharge"
            })

        page += 1

    return livres


# Fonction pour sauvegarder les livres dans un fichier CSV
def save_books_to_csv(categorie, livres):
    nom_fichier = os.path.join(CSV_FOLDER, f"{categorie.replace(' ', '_').lower()}.csv")

    with open(nom_fichier, mode="w", newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=["titre", "prix", "disponibilite", "image_url", "image_locale"])
        writer.writeheader()
        writer.writerows(livres)

    print(f"Fichier '{nom_fichier}' créé avec {len(livres)} livres")


# Exécution directe du script
categories = get_categories()

for categorie, url in categories.items():
    livres = scrape_books(categorie, url)
    if livres:
        save_books_to_csv(categorie, livres)