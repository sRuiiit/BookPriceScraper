import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/rip-it-up-and-start-again_986/index.html"

response = requests.get(url)

print(response.status_code) # Code 200 = tout va bien !
if response.status_code == 200:
    print("C'est bon, j'ai eu un retour du site !")

# Analyse du contenu HTML avec BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Extraction du titre de la page
titre_page = soup.title.string
print("Titre de la page :", titre_page)

