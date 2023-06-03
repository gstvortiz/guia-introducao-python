"""
referencia: https://docs.python.org/3/tutorial/inputoutput.html#reading-and-writing-files
"""

# 1-Abra o arquivo do diretorio atual "foo.txt"
# Printe todo o conteudo do arquivo , então feche o arquivo
arq = open('foo.txt', 'r')
for linha in arq:
    print(linha)
arq.close()

# 2- Crie um arquivo chamado "bar.txt" 
# Abra o arquivo e conte quanta vezes a palavra "sir" aparece 
# Escreva no arquivo que voce criou quantas palavras foram encontradas
# Feche o arquivo
contador = 0
arq = open('bar.txt', 'r')
for linha in arq:
    contador += linha.count('sir')
arq.close()
print(contador)