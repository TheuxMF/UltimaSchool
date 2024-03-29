def menu (cod):
    if cod == 100:
        print('Você pediu um Cachorro Quente no valor de 9,00')
        total = 9.00           
    elif cod == 101:
        print('Você pediu um Cachorro Quente Duplo no valor de 11,00')
        total = 11.00
    elif cod == 102:
        print('Você pediu um X-Egg no valor de 12,00')
        total = 12.00
    elif cod == 103:
        print('Você pediu um X-Salada no valor de 12,00')
        total = 12.00
    elif cod == 104:
        print('Você pediu um X-Bacon no valor de 14,00')
        total = 14.00
    elif cod == 105:
        print('Você pediu um X-Tudo no valor de 17,00')
        total = 17.00
    elif cod == 200:
        print('Você pediu um Refrigerante Lata no valor de 5,00')
        total = 5.00
    elif cod == 201:
        print('Você pediu um Chá Gelado no valor de 4,00')
        total = 4.00
    else:
        print('Opção inválida')
        total = 0
        
    return total


if __name__ == '__main__':
    cardapio = """
    *******************Cardápio*******************
    ----------------------------------------------
    | Código |        Descrição        |  Valor  |
    |   100  |     Cachorro Quente     |   9,00  |
    |   101  |  Cachorro Quente Duplo  |  11,00  |
    |   102  |           X-Egg         |  12,00  |
    |   103  |         X-Salada        |  12,00  |
    |   104  |          X-Bacon        |  14,00  |
    |   105  |           X-Tudo        |  17,00  |
    |   200  |    Refrigerente Lata    |   5,00  |
    |   201  |         Chá Gelado      |   4,00  |
    ----------------------------------------------
    """
    print(cardapio)

    valor = 0.0
    codigo = int(input('Entre com o código desejado: '))

    while True:
        
        valor += menu(codigo) 

        print('Deseja pedir mais alguma coisa?')
        print('1 - Sim')
        print('2 - Não')
        pedir_mais = int(input())

        if pedir_mais == 2:
            break

        codigo = int(input('Entre com o código desejado: '))

    print(f'O total a ser pago é: {valor:.2f} R$')

