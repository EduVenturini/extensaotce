"""
    Projeto Calc
Descrição: Faça um programa Python modularizado que seja uma calculadora com as 4 
operações aritméticas com dois números e que tenha um módulo principal
e um módulo - chamado aritmetico.py - além de módulos que forneçam
funções de entrada e saída de dados.
Autor: Eduardo S Venturini
Data: 29/08/2022
Versão: 0.0.2
"""


#main (escrever o módulo principal)
def main():
    #Entrada
    lista = entra.entrada()
    operacao = entra.operacao()

    #Processamento
    aritmetica = entra.calc(opera, numero_1, numero_2)

    #Saida
    sai.saida(opera, x, y)




#Execução do programa
if __name__ == "__main__":
    main()
