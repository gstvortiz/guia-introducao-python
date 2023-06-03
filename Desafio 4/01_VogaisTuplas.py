#   Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
#   Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.

frutas = ('banana', 'abacate', 'pera', 'uva', 'abacaxi')

for palavra in frutas:
    lista = []
    for letra in palavra:
        if letra in 'AaEeIiOoUu':
            lista.append(letra)
    print(palavra, ':', lista)