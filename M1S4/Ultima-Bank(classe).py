class cliente:
    def __init__(self,nome,cpf,idade):
        self.nome=nome
        self.cpf=cpf
        self.idade=idade

    def __str__(self):
        return f'nome : {self.nome}\ncpf : {self.cpf}\nidade : {self.idade}'
    
if __name__=='__main__':
    clientes=[]
    for cont in range(2):
        print("-"*10 + "Ultima-Bank" + '-'*10)
        nome = input("Digite seu nome : ")
        cpf = input("Digite seu cpf : ")
        idade = input("digite sua idade : ")
        dados = cliente(nome,cpf,idade)
        clientes.append(dados)
        
    for cliente in clientes:
        print("-"*10 + "Ultima-Bank dados" + '-'*10)
        print(cliente)