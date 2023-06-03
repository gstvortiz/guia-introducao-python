# Defina a função soma_nat de forma recursiva que recebe como argumento um número natural  n  e devolve a soma de todos os números naturais até  n .

#Exemplo
def soma_nat(n):
    return sum([i for i in range(n+1)])