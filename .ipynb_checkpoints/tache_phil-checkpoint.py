import requests
from bs4 import BeautifulSoup as bs
# Demande à l'utilisateur d'entrer le nom d'utilisateur GitHub
github_user = input('Entrez le nom d\'utilisateur GitHub: ')
# Construit l'URL correcte
lien = 'https://github.com/' + github_user
# Envoie une requête GET à l'URL
r = requests.get(lien)
# Analyse le contenu de la page
soup = bs(r.content, 'html.parser')
    # Trouve l'élément img dans le conteneur du profil
profile_img = soup.find('img', class_='avatar-user')
print(profile_img)
    