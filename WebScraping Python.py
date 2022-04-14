import requests
from bs4 import BeautifulSoup
import pandas as pd

lista_noticias = []

response = requests.get('https://g1.globo.com')

content = response.content

site = BeautifulSoup(content, 'html.parser')

# HTML_DA_NOTICIA

noticias = site.findAll('div', attrs={'class': 'feed-post-body'})

for noticia in noticias:
    # Título
    titulo = noticia.find('a', attrs={'class': 'feed-post-link gui-color-primary gui-color-hover'})
    print(titulo.text)

    # Subtítulo

    subtitle = noticia.find('a', attrs={'class': 'gui-color-primary gui-color-hover feed-post-body-title bstn-relatedtext'})
    if subtitle:
        lista_noticias.append([titulo.text, subtitle.text, titulo['href']])
        print(subtitle.text)
    else:
        lista_noticias.append([titulo.text, '', titulo['href']])

news = pd.DataFrame(lista_noticias, columns=['Título',  'Subtítulo', 'Link'])

news.to_excel('noticias.xlsx', index=False)
