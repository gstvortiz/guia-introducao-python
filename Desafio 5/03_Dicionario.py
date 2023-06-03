#   Faça um programa que leia nome e média de um aluno, guardando também a situação em um dicionário.
#   No final, mostre o conteúdo da estrutura na tela.

nome = input('Digite o nome do aluno: ')
media = input('Digite a média do aluno: ')

dicionario = {'Nome do Aluno': nome, 'Média do Aluno': media, 'Situação do Aluno': 'Aprovado' if float(media) >= 60 else 'Reprovado'}
print(dicionario)