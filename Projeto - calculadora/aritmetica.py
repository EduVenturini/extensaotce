"""
    Projeto Calc
Descrição: Faça um programa Python modularizado que seja uma calculadora com as 4 
operações aritméticas com dois números e que tenha um módulo principal
e um módulo - chamado aritmetico.py - além de módulos que forneçam
funções de entrada e saída de dados.
Autor: Eduardo S Venturini
Data: 29/08/2022
Versão: 0.0.3
"""
import entra

#Processamento de Dados

def calc(numero_1, numero_2, numero_3):
    if numero_3 == 1:
        calculo = numero_1 + numero_2
    elif numero_3 == 2:
        calculo = numero_1 - numero_2
    elif numero_3 == 3:
        calculo = numero_1 * numero_2
    elif numero_3 == 4:
        if numero_2 == 0:
             "Não se pode dividir por zero."
        calculo = numero_1 / numero_2
    return calculo
