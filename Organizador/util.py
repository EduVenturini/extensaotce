"""
Projeto Python 1
Autor: Eduardo S Venturini
Data: 31/08/2022
Versão: 0.0.1
"""
import os
import shutil

def cria_dir(nome: str):
   
    if os.path.exists(nome) == False:
        os.mkdir(nome)


def move_arq(arquivos: list):

    arquivos = os.listdir()
    
    for arquivo in arquivos:
        if ".xls" in arquivo:
            shutil.move(arquivo, f"./planilhas/{arquivo}")
        elif ".doc" in arquivo:
            shutil.move(arquivo, f"./documentos/{arquivo}")
        elif ".docx" in arquivo:
            shutil.move(arquivo, f"./documentos/{arquivo}")
