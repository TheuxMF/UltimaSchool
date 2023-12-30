dados = []
for cont in range(2):
    print("-"*10 + "Ultima-Bank" + '-'*10)
    nome = input("Digite seu nome : ")
    cpf = input("Digite seu cpf : ")
    idade = input("digite sua idade : ")
    dados.append(
        {
            'nome': nome,
            'cpf':cpf,
            'idade':idade
        }
    )
    
for dados in dados:
    print("-"*10 + "Ultima-Bank" + '-'*10)
    print(f"Cliente : {dados['nome']}")
    print(f"cpf : {dados['cpf']}")
    print(f"idade : {dados['idade']}")