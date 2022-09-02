"""
Projeto Python 1
Autor: Eduardo S Venturini
Data: 31/08/2022
Versão: 0.0.1
"""

import util
import os
import shutil

def main():
    print("""Este programa move os arquivos para a pasta Documentos e Planilhas.\n Os arquivos deverão estar dentro da pasta organizador para o devido funcionamento""")
    arquivos = os.listdir()
    for diretorio in ['documentos', 'planilhas']:
        util.cria_dir(diretorio)
    util.move_arq(arquivos)


if __name__ == "__main__":
    main()
