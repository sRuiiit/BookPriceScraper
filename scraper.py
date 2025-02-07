import requests
from bs4 import BeautifulSoup

url = "https://books.toscrape.com"

response = requests.get(url)

print(response.status_code) # Code 200 = tout va bien !
if response.status_code == 200:
    print("C'est bon, j'ai eu un retour du site !")

# print(response.headers) # affiche les headers de booktoscrape
print(response.text) # le contenu en texte
