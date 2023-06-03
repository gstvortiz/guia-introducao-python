# Criar uma função externa que irá aceitar dois parametros, a e b
# Crie uma função interna dentro da função externa que irá retornar a soma os parametros a e b 
# Na função externa, adicione 5 ao retorno da funcao interna e escreva na tela este valor

def externa(a, b):
    def interna():
        return a + b
    return interna() + 5

print(externa(10,10))