<h1> 📚 Books Online - Scraper de Prix </h1>

<h2>Automatisation du suivi des prix des livres d’occasion</h2>
<h3>Un projet Python pour extraire les prix des livres de Books to Scrape</h3>

<br>

<h3>📝 Description du projet</h3>

Ce projet vise à automatiser la surveillance des prix des livres d’occasion sur le site [Books to Scrape](https://books.toscrape.com) afin d’aider Books Online, une librairie en ligne, à mieux suivre la concurrence.

Le programme est un scraper Python qui extrait les informations tarifaires et les enregistre sous forme exploitable pour des analyses ultérieures.

<h4>🎯 Objectifs</h4>
<li>Automatiser la collecte des prix des livres sur Books to Scrape.</li>
<li>Structurer les données extraites sous un format exploitable (CSV) par catégorie.</li>
<li>Récupérer les images de couverture de chaque livre et classer par catégorie.</li>

<h4>📂 Contenu du repository</h4>
<li>scraper.py → Script principal qui extrait les données.</li>
<li>requirements.txt → Liste des dépendances à installer.</li>
<li>README.md → Ce fichier expliquant le projet.</li>
<li>.gitignore → Exclut les fichiers temporaires et les données extraites.</li>

<h4>🛠️ Installation et exécution</h4>

1. Pré-requis

Assurez-vous d’avoir Python 3.x installé. Vérifiez avec :

<code>python --version</code>

2. Installation des dépendances

Clonez ce repository et installez les modules nécessaires :

<code>git clone https://github.com/sRuiiit/BookPriceScraper.git
cd books-online-scraper
pip install -r requirements.txt</code>

3. Lancer le scraper

Exécutez le script :

<code>python scraper.py</code>

Cela générera un dossier CSVparcategories contenant un fichier CSV par catégorie lui-même contenant les informations des livres extraits.

<h4>📊 Format des données extraites</h4>

Les données sont enregistrées sous forme de fichier CSV avec les colonnes suivantes :


| titre   | prix   | disponibilite | image_url   | image_locale                  |
|---------|--------|---------------|-------------|-------------------------------|
| Livre 1 | £45.17 | in stock      | https://... | images_couvertures/travel/... |
| Livre 2 | £49.43 | in stock      | https://... | images_couvertures/cat.../... |

<h4>🔧 Vers un pipeline ETL</h4>

Pour aller plus loin, ce scraper pourrait être intégré dans un pipeline ETL en plusieurs étapes :
<li>Extract → Extraction des données via ce scraper.</li>
<li>Transform → Nettoyage et enrichissement des données (ex. conversion des devises).</li>
<li>Load → Chargement des données dans une base de données ou un tableau d’analyse.</li>
<br>
L’utilisation de cron jobs ou d’un scheduler Python permettrait d’automatiser ce processus.

<h4>🚀 Améliorations futures</h4>
<li>Ajouter des librairies concurrentes pour élargir le suivi des prix.</li>
<li>Automatiser le scraping à intervalles réguliers.</li>
<li>Stocker les données dans une base SQL ou un tableau interactif.</li>
<li>Intégrer une visualisation des tendances de prix.</li>
<li>Récupérer le taux de change et afficher le prix en Euros.</li>
<li>Utiliser la librairie LXML plus rapide et robuste.</li>

<h4>👤 Auteur</h4>

Steve Raffner
📩 Contact : claudefrancois@gmail.com
🔗 GitHub : https://github.com/sRuiiit

💡 N’hésitez pas à contribuer ou à poser des questions ! 🚀
