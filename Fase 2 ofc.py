import csv
import matplotlib.pyplot as plt

def cargaDados(Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores):
    arquivo = open(Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores, 'r')
    dados = []
    for linha in arquivo:
        linha1 = linha[:-1]
        linha2 =linha1[1:len(linha1)]
        dados.append(linha2)
    arquivo.close()
    return dados

def escreveLista(lista):
    for item in lista:
        print(item)

def transformandoDados(linha):
    itens = linha.split(',')
    itens = itenstransformados = [itens[0]]
    cont = 1
    while cont <len(itens):
        itenstransformados.append(float(itens[cont]))
        cont = cont + 1
    return itenstransformados


def transformalista(lista):
    listadeitens = []
    cont = 1
    while cont< len(lista):
        listadeitens.append(transformandoDados(lista[cont]))
        cont = cont + 1
    return listadeitens

#DATAS -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


def datas(lista):
    datas:1
    for item in lista:
        print(item[1])
    return datas

#PRECIPTAÇÃO ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

def preciptação(lista):
    preciptação:2
    for item in lista:
        print(item[2])
    return preciptação

#MAXIMA

def maxima(lista):
    maxima:3
    for item in lista:
        print(item[3])
    return maxima

#MININA

def minina(lista):
    minina:4
    for item in lista:
        print(item[4])
    return minina












dadosbrutos = cargaDados(Anexo_Arquivo_Dados_Projeto_Logica_e_programacao_de_computadores=)
escreveLista(dadosbrutos)
print(dadosbrutos[0])
cabecalho = dadosbrutos[0].split(',')
print(cabecalho)
dados = transformalista(dadosbrutos)
escreveLista(dados)

print()

