#   Faça um programa que leia uma frase pelo teclado e mostre:
#       - Quantas vezes aparece a letra 'A'
#       - Em que posição ela aparece a primeira vez
#       - Em que posição ela aparece a última vez

frase = input('Digite sua frase: ')

print(f'A letra "A" aparece {frase.upper().count("A")} vezes na frase "{frase}"')
print(f'A letra "A" aparece pela primeira vez na posição {frase.upper().find("A")} na frase "{frase}"')
print(f'A letra "A" aparece pela última vez na posição {frase.upper().rfind("A")} na frase "{frase}"')