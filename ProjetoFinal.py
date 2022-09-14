"""
    Projeto Final - Curso Extensão TCE/RS

Autor: Eduardo S Venturini
Data: 12/09/2022 a 14/09/2022
Versão: 1.0.0 - versão para .zip
"""
import requests
import pandas as pd
from openpyxl import Workbook, load_workbook


#abrindo a página
def catch(site):
    dados = requests.get(site)
    return dados

#gravando o arquivo com as informações da variável 'dados'
def save(dados):
    with open('balancete.csv','wb') as arquivo:
        for texto in dados.iter_content():
            arquivo.write(texto)
        arquivo.close()

#Usando o Pandas e Openpyxl para transformar em .xlsx
def xlsx(dados):
    balancete = pd.read_csv('balancete.csv')
    balancete.to_excel("balancete.xlsx", sheet_name="despesas", index = False)
    novo_balancete = load_workbook(filename = 'balancete.xlsx')
    novo_balancete.save("Novo Balancete.xlsx")

#'módulo principal'
def main():
    site = "http://dados.tce.rs.gov.br/dados/municipal/balancete-despesa/2022.csv" 
    dados = catch(site)
    save(dados)
    xlsx(dados)
    print("Balancetes salvos com sucesso!")
    input("Tecle Enter para Finalizar.")

if __name__ == "__main__":
    main()
