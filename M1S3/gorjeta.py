'''Escreva uma função que, dado o valor da conta de um restaurante e um percentual de taxa de serviço, 
calcule e exiba a gorjeta do garçom, considerando o percentual do valor da conta.'''

def calcular_gorjeta(valor_conta, taxa_servico):
    gorjeta = valor_conta * taxa_servico / 100
    return gorjeta

# Obtendo o valor da conta e a taxa de serviço do usuário
valor_conta = float(input("Digite o valor da conta: "))
taxa_servico = int(input("Digite a taxa de serviço (em %): "))

# Chamando a função para calcular a gorjeta
resultado = calcular_gorjeta(valor_conta, taxa_servico)

# Exibindo o resultado com duas casas decimais
print(f"A gorjeta do garçom é: R${resultado:.2f}")