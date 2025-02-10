import requests
import csv
import lxml
from bs4 import BeautifulSoup

# URL de base pour les catégories (sans catégorie, sans numéro de page de catégorie)
categories_base_url = "https://books.toscrape.com/catalogue/category/books/"

# Effectuer une requête GET pour récupérer la page
response = requests.get(url)

if response.status_code == 200:
    print("C'est bon, j'ai le retour du site pour chopper les catégories !")

    # Analyse du contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, "lxml")

    # Sélectionner la liste des catégories
    categories_section = soup.select("aside div.side_categories ul li ul li a")

    # Liste pour stocker les catégories
    categories = []

    # Extraire les noms et les URLs des catégories
    for category in categories_section:
        nom_categorie = category.get_text(strip=True)  # Récupère le nom de la catégorie
        url_categorie = "https://books.toscrape.com/" + category["href"]  # Construit l'URL complète

        categories.append({"nom": nom_categorie, "url": url_categorie})

    # Afficher les catégories trouvées
    for cat in categories:
        print(f"{cat['nom']} → {cat['url']}")

else:
    print("Erreur lors de la récupération de la page :", response.status_code)








# ------ script précédent -------

"""
# URL de base pour la catégorie Nonfiction (sans numéro de page)
base_url = "https://books.toscrape.com/catalogue/category/books/nonfiction_13/"

# Liste pour stocker tous les livres
livres = []

# Numéro de page initial
page = 1

while True:  # Boucle infinie, on arrête quand il n'y a plus de page
    url = f"{base_url}page-{page}.html" if page > 1 else f"{base_url}index.html"

    # Effectuer une requête GET pour récupérer la page
    response = requests.get(url)

    # Vérifier si la page existe (évite les erreurs 404)
    if response.status_code != 200:
        print(f"Fin du scraping, dernière page trouvée : {page - 1}")
        break

    print(f"Scraping de la page {page}...")

    # Analyse du contenu HTML avec BeautifulSoup
    soup = BeautifulSoup(response.content, "html.parser")

    # Sélectionner tous les articles de livres sur la page
    for livre in soup.find_all("article", class_="product_pod"):
        titre = livre.h3.a["title"]  # Récupérer le titre du livre
        prix = livre.find("p", class_="price_color").get_text()  # Prix du livre
        disponibilite = livre.find("p", class_="instock availability").get_text(strip=True)  # Stock

        # Ajouter les informations dans la liste de livres
        livres.append({
            "titre": titre,
            "prix": prix,
            "disponibilite": disponibilite
        })

    # Passer à la page suivante
    page += 1

# Nom du fichier CSV
nom_fichier = "livres_nonfiction.csv"

# Création et écriture du fichier CSV
with open(nom_fichier, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["titre", "prix", "disponibilite"])

    # Écrire l'en-tête des colonnes
    writer.writeheader()

    # Écrire tous les livres récupérés dans le fichier CSV
    writer.writerows(livres)

print(f"Le fichier {nom_fichier} a été créé avec succès, {len(livres)} livres trouvés !")
"""