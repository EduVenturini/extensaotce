"""
Projeto Python 1
Autor: Eduardo S Venturini
Data: 31/08/2022
Versão: 0.0.2
"""

import util
import os
import shutil

def main():
    print("""Este programa move os arquivos para as pastas Documentos e Planilhas.\n Os arquivos a serem organizados deverão estar dentro da pasta do app Organizador para o devido funcionamento.""")
    input("Clique Enter para iniciar.")
    arquivos = os.listdir()
    for diretorio in ['documentos', 'planilhas']:
        util.cria_dir(diretorio)
    util.move_arq(arquivos)
    print("Procedimento concluído!")
    input("Clique Enter para finalizar.")


if __name__ == "__main__":
    main()
