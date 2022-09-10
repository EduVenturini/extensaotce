"""
    Projeto 2
Criar planilhas no excel com python usando openpyxl em um ambiente virtual
Autor: Eduardo S Venturini
Version: 0.0.3
Data: 08/09/2022
"""
from openpyxl import Workbook

wb = Workbook()

for planilha in ["receitas", "despesas", "resultado"]:
    wb.create_sheet(planilha)

wb.save("orcamento.xlsx")

input("Planilhas criadas com sucesso. Clique enter para finalizar.")


