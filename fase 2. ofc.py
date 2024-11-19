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
