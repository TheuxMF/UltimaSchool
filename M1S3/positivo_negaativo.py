'''Faça um programa com uma função que necessite de um parâmetro. 
A função deve retornar “Positivo”, se seu o número for maior que zero, “Negativo” 
se o número for menor que zero, e “Zero” se o número for igual a zero.'''

def positivoNegativo(numero):
    if numero>0:
        return 'positivo'
    elif numero<0:
        return 'negativo'
    else:
        return 'zero'
    
numero=int(input("digite um numero "))
print(f"{numero} é {positivoNegativo(numero)}")