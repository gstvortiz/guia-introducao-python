# Escreva uma função que receba um numero pelo entrada e retorna se aquele numero é primo ou não 
def eh_primo(numero):
    if numero < 2: return False
    for i in range(2, int(numero/2)):
        if numero % i == 0:
            return False
    return True