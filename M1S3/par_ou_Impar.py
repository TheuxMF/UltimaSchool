'''Crie uma função que, ao receber um número inteiro, retorna se um número é par ou ímpar.'''
def parImpar(numero):
    return 'par' if numero%2==0 else 'impar'

numero = int(input("digite o numero :"))
print(parImpar(numero))