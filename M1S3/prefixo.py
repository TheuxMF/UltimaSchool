'''Crie uma função que receba duas palavras e retorne “True” caso a primeira palavra seja um prefixo da segunda,
e “False” caso contrário.

Exemplo: ’programa’ é prefixo de “programador”, pois todas as letras de ‘programa’ correspondem 
às primeiras letras de “programador”'''

def verificar_prefixo(prefixo, palavra):
    if palavra[:len(prefixo)]==prefixo:
        return f'As {len(prefixo)} letras de {prefixo} são exatamente as {len(palavra[:len(prefixo)])} primeiras letras de {palavra}, então é prefixo!'
    else:
        return f'As {len(prefixo)} letras de {prefixo} são diferentes das {len(palavra[:len(prefixo)])} primeiras letras de {palavra}, então é prefixo!'

# Exemplo de uso da função

palavra = input("Digite um palavra: ")
prefixo = input("digite um prefixo: ")

resultado = verificar_prefixo(prefixo, palavra)
print(resultado)