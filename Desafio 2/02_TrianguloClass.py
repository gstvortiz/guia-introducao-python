# Dados três valores X, Y e Z, verificar se eles podem ser os comprimentos dos lados de um triângulo, 
# e se forem verificar se é um triângulo equilátero, isóscele ou escaleno. 
# Se eles não formarem um triângulo, escrever uma mensagem.
def triangulo(X, Y, Z):
    if (abs(Y-Z) < X < Y+Z) and (abs(X-Z) < Y < X+Z) and (abs(X-Y) < Z < X+Y):
        if X == Y == Z:
            return 'O triângulo existe e é equilátero'
        elif(X != Y != Z):
            return 'O triângulo existe e é escaleno'
        else:
            return 'O triângulo existe e é isóscele'
    return 'O triângulo não existe'

X = int(input('Digite o lado X: '))
Y = int(input('Digite o lado Y: '))
Z = int(input('Digite o lado Z: '))
        
print(triangulo(X, Y, Z))