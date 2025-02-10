import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/rip-it-up-and-start-again_986/index.html"

# Vérification que la page URL est disponible
response = requests.get(url)

print(response.status_code) # Code 200 = tout va bien !
if response.status_code == 200:
    print("C'est bon, j'ai eu un retour du site !\n")

# Analyse du contenu HTML avec BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extraction du titre de la page (dans head)
# titre_page = soup.title.string
# print("Titre de la page :", titre_page[0:30])

# Ou aller chercher le titre dans (body)
titre_page_body = soup.find("h1").get_text()
print("Titre de la page :", titre_page_body)