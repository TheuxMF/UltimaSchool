'''Crie uma função que recebe um número inteiro por parâmetro e 
então imprime na tela do número recebido até o zero.'''
def conntadorRegresivo(numero):
    numeroInverso = []
    
    while numero>=0:
        numeroInverso.append(numero)
        numero-=1
        
    return numeroInverso

numero = int(input("digite o numero"))
numero = conntadorRegresivo(numero)

for num in numero:
    print(num ,end='')