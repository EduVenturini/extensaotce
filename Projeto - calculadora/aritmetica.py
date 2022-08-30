"""
    Projeto Calc
Descrição: Faça um programa Python modularizado que seja uma calculadora com as 4 
operações aritméticas com dois números e que tenha um módulo principal
e um módulo - chamado aritmetico.py - além de módulos que forneçam
funções de entrada e saída de dados.
Autor: Eduardo S Venturini
Data: 29/08/2022
Versão: 0.0.8
"""

#Processamento de Dados

def adicao(x: float, y: float) -> float:
    #soma dois números.
    return x + y


def subtracao(x: float, y: float) -> float:
   #subtrai um número x de um número y.
   return x - y

def multiplicacao(x: float, y: float) -> float:
    #multiplica os dois números.
    return x*y


def divisao(x: float, y: float) -> float:
    #divide x por y sendo y diferente de zero
    if y == 0:
        return "Não se pode dividir por zero."
    return x/y
