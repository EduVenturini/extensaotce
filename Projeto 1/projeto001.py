"""
Projeto Python 1
ordens
Vocˆe tem dentro de uma pasta os seguintes arquivos:
• orcamento.xls
• orcamento.docx
• clientes.xls
• clientes.doc
• relatorio.doc
Sua tarefa ´e organizar tais arquivos nas pastas planilhas e documentos
de acordo com a extens˜ao do arquivo.
Para executar sua tarefa, escreva um programa em Python que crie as pastas
e mova os arquivos para as devidas pastas.
No GitHub, crie um reposit´orio denominado organizador e suba seu programa para l´a.
Observa¸c˜oes:
1. N˜ao se esque¸ca de deixar seu reposit´orio p´ublico e de responder `a pergunta
”Qual o link de seu reposit´orio” no Moodle .
2. Use os pacotes OS e SHUTILS da biblioteca padr˜ao do Python para lhe
ajudar nesta tarefa.
Autor: Eduardo S Venturini
Data: 29/08/2022
Versão: 0.0.0 - alfa
"""
# pasta testes está no caminho C:\Users\eduar\Desktop\extensaotce-main\teste

import os

#Entrada
#Insira o local do arquivo
#Posso também nem entrar com o local, deixar o python procurar
diretorio = input("Insira o caminho até a pasta com os arquivos: ")


#Processamento
# 1 - criar os diretórios dentro da pasta onde os arquivos estão
# 2 - separar os documentos conforme extensão
os.mkdir(diretorio\documentos')



#Saída
print("os arquivos foram movidos com sucesso")
