#!/usr/bin/python3
# -*- coding: utf-8 -*-

# - - - - - - - - - - - - - - [ Bloco de Importar Bibliotecas (libs) ] - - - - - - - - - - - - - - #

try:
    import os

except Exception as E:
    print('Erro ao Importar Bibliotecas: ' + E)


# - - - - - - - - - - - - - - [ Bloco de Definicao de Variaveis (1o) ] - - - - - - - - - - - - - - #

# [ Define as Variaveis ]
try:
    diretorio = os.path.join(os.getcwd(), '_BASESPAGTONETS')  # Define o Diretorio onde serao listados os arquivos TXT e CSV

except Exception as E:
    print('Erro ao Definir as Variaveis: ' + E)


# - - - - - - - - - - - - - - [ Bloco de Execucao (2o) ] - - - - - - - - - - - - - - #

# [ Lista os arquivos TXT e CSV do diretorio definido ]
try:
    for _, _, arquivos in os.walk(diretorio):
        for arquivo in arquivos:
            if ('.txt' in arquivo.lower() or '.csv' in arquivo.lower()):
                print(arquivo)

except Exception as E:
    print('Erro ao Listar Arquivos: ' + E)
