'''Crie um programa que seja capaz de obter e somar TODOS os números passados pelo usuário como entrada, 
permitindo somar qualquer quantidade de dados de entrada.'''
def somarTudo(numeros):
    numero =0
    for num in numeros:
        numero+=int(num)
        
    return numero

numeros=[]
while True:
    print("-1 para parar")
    numero = input("digite um numero :")
    if numero=="-1":
        break
    numeros.append(numero)
    
print(f" resultado {somarTudo(numeros)}")