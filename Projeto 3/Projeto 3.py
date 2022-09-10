"""
    Projeto 3
Buscar notícias no site G1 na internet e salvar um arquivo .html utilizando a biblioteca Requests
Autor: Eduardo S Venturini
Data: 08/09/2022
Versão: 0.0.2
"""

import requests
import webbrowser

#Módulo webbrowser já ok, instalo somente requests

pagina = requests.get('https://g1.globo.com/politica/')
print(pagina.status_code)

with open('politica.html', 'wb') as arquivo:
    for texto in pagina.iter_content(1048576):
        arquivo.write(texto)

webbrowser.open('politica.html')

input("A busca foi feita e o arquivo html foi criado. Tecle enter para finalizar.")

