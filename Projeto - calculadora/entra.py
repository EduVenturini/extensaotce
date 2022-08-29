"""
    Projeto Calc
Descrição: Faça um programa Python modularizado que seja uma calculadora com as 4 
operações aritméticas com dois números e que tenha um módulo principal
e um módulo - chamado aritmetico.py - além de módulos que forneçam
funções de entrada e saída de dados.
Autor: Eduardo S Venturini
Data: 29/08/2022
Versão: 0.0.2 - entrada dos números somente
"""

#Entrada de dados

def entra_dados():
    """Esta função (procedimento) lê dois números digitados pelo usuário."""
    i = 0
    lista_numeros = []
    while i < 2:
        numeros = float(input("\nDigite um número: "))
        lista_numeros.append(numero)
        i+=1
    return lista_numeros
    operacao = input("\nInforme a operação desejada:\n+ para adição\n- para subtração\n* para multiplicação\n/ para divisão\n")
    return operacao
