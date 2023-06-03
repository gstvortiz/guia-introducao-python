# Construa um programa que receba como entrada três valores inteiros. Ao final imprima a soma, multiplicação e divisão deste itens.

a, b, c = map(int, input().split())

print(f'Soma: {a+b+c:.2f}')
print(f'Multiplicação: {a*b*c:.2f}')
print(f'Divisão: {a/b/c:.2f}')

# Escreva um programa que leia um número e apresente a raiz quadrada deste número.

x = int(input("Entre  a number: "))

print(f'{x**(1/2)}')

