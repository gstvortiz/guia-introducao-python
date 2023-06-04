import os
from time import sleep

def inserir_filme(arquivos_txt, legenda):
    nome_filme = input('Digite o nome do filme: ')
    data = input('Digite a data de visualização do filme: ')
    nota = input('Digite a nota do filme: ')
    i = int(input(f'Digite o gênero do filme ({legenda}): '))
    arq = open(f'{arquivos_txt[i]}', 'a')
    arq.write(f'{nome_filme},{data},{nota}\n')
    arq.close()
    print('\nO filme foi adicionado com sucesso! :)')
    sleep(2)

def ver_filmes(arquivos_txt, legenda):
    i = int(input(f'Digite o gênero do filme ({legenda}): '))
    arq = open(f'{arquivos_txt[i]}', 'r')
    for linha in arq:
        nome, data, nota = linha.split(',')
        print(f'Filme: {nome} | Data: {data} | Nota: {nota}', end = '')
    arq.close()
    sleep(2)

def buscar_filme(arquivos_txt):
    filme = input('Qual nome do filme que você deseja buscar?\n')
    for genero in arquivos_txt:
        arq = open(f'{genero}', 'r')
        for linha in arq:
            if filme.upper() in linha.upper():
                nome, data, nota = linha.split(',')
                print(f'Filme: {nome} | Data: {data} | Nota: {nota}', end = '')
                break
        arq.close()
    sleep(2)

arquivos_txt = sorted([arquivo for arquivo in os.listdir() if arquivo.endswith('.txt')])
legenda = "".join(f'[{arquivos_txt.index(genero)}]:{genero[:genero.find(".txt")]} ' for genero in arquivos_txt)

while(True):
    print(''.join("-" for i in range(100)))
    select_case = input('Olá! O que você deseja?\n[1]: Inserir um Novo Filme\n[2]: Visualizar Filmes por Gênero\n[3]: Buscar um Filme por Nome\n')
    print(''.join("-" for i in range(100)))
    if select_case == '1': 
        inserir_filme(arquivos_txt, legenda)
    elif select_case == '2': 
        ver_filmes(arquivos_txt, legenda)
    elif select_case == '3': 
        buscar_filme(arquivos_txt)
    else:
        print('Opção Inválida. Tente novamente.')
        break