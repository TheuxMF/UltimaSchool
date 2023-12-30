'''Crie um programa com uma função que necessite de três parâmetros e então que retorne a sua soma.'''
def separar_e_somar(numero):
    # Convertendo o número em uma string
    numero_str = str(numero)

    #separando 
    num1 = int(numero_str[0])
    print(num1)
    num2 = int(numero_str[1])
    print(num2)
    num3 = int(numero_str[2:])
    print(num3)
    
    return num1+num2+num3

numero = int(input("o numero"))


print(f"A soma dos dígitos do número {numero} é: {separar_e_somar(numero)}")