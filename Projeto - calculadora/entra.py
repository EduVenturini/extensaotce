"""
    Projeto Calc
Descrição: Faça um programa Python modularizado que seja uma calculadora com as 4 
operações aritméticas com dois números e que tenha um módulo principal
e um módulo - chamado aritmetico.py - além de módulos que forneçam
funções de entrada e saída de dados.
Autor: Eduardo S Venturini
Data: 29/08/2022
Versão: 0.0.3 - cria a lista com tudo
"""

#Entrada de dados

def entra_dados():
    #Entra os dados de número e operação em uma lista
    lista_numeros = []
    numero = float(input("\nDigite o primeiro número: "))
    lista_numeros.append(numero)
    numero = float(input("\nDigite o segundo número: "))
    lista_numeros.append(numero)
    numero = input("\nInforme a operação desejada:\n1 para adição\n2 para subtração\n3 para multiplicação\n4 para divisão\n")
    lista_numeros.append(numero)
