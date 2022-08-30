"""
    Projeto Calc
Descrição: Faça um programa Python modularizado que seja uma calculadora com as 4 
operações aritméticas com dois números e que tenha um módulo principal
e um módulo - chamado aritmetico.py - além de módulos que forneçam
funções de entrada e saída de dados.
Autor: Eduardo S Venturini
Data: 29/08/2022
Versão: 0.0.6
"""

#Processamento de Dados
#O cálculo é feito aqui com o x, y e OP

def adicao(x: float, y: float) -> float:
    """
    Docstring de documentação da função.  Esta função soma dois números.
    """
    return x + y


def subtracao(x: float, y: float) -> float:
   """
   Esta função subtrai um número y de um número x.
   """
   return x - y

def multiplicacao(x: float, y: float) -> float:
    """
    Esta função multiplica dois números.
    """
    return x*y


def divisao(x: float, y: float) -> float:
    """
    Esta função pega dois números tais que o segundo é diferente de zero
    e calcula a sua divisão.
    """
    if y == 0:
        return "Não se pode dividir por zero."
    return x/y
