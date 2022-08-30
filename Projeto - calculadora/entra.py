"""
    Projeto Calc
Descrição: Faça um programa Python modularizado que seja uma calculadora com as 4 
operações aritméticas com dois números e que tenha um módulo principal
e um módulo - chamado aritmetico.py - além de módulos que forneçam
funções de entrada e saída de dados.
Autor: Eduardo S Venturini
Data: 29/08/2022
Versão: 0.0.9 - do zero
"""

#Entrada de dados

def entrada() -> list:
    #Entra os dados de número em uma lista
    x = float(input("\nDigite o primeiro número e clique enter: "))
    y = float(input("\nDigite o segundo número e clique enter: "))
    return [x, y]
