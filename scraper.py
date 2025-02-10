import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com/catalogue/rip-it-up-and-start-again_986/index.html"

# Vérification que la page URL est disponible avec requests
response = requests.get(url)

print(response.status_code) # Code 200 = tout va bien !
if response.status_code == 200:
    print("C'est bon, j'ai eu un retour du site !\n")

# Analyse du contenu HTML avec BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Chercher la div avec la classe "col-sm-6 product_main"
div_product_main = soup.find("div", class_="col-sm-6 product_main")

# Chercher le h1 à l'intérieur de cette div
titre_page_body = div_product_main.find("h1").get_text()

print("Titre de la page :", titre_page_body)





