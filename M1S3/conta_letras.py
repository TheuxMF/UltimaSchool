'''Crie uma função que permita contar o número de vezes que aparece uma determinada letra em uma frase. 
A letra desejada e a frase a ser verificada serão passadas por parâmetro para a função, 
que retornará a quantidade da letra na frase.'''

def contaLetras(letra, frase):
    return frase.count(letra)

frase = input("digite a frase ")
letra = input("Digite a letra para encontrar ")

print(f"a frase {frase} tem {contaLetras(letra,frase)} letra(s) {letra} ")