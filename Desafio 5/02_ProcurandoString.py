#   Faça um funcão que leia o nome de uma pessoa
#   e diga se ela tem "Silva" no nome.

nome = input('Digite um nome: ')

if 'Silva' in nome:
    print(f'A pessoa "{nome}" tem "Silva" no nome')
else:
    print(f'A pessoa "{nome}" não tem "Silva" no nome')