import sqlite3
from insert import inserir_dados
from selecionar import listar
from input_dados import input_dados
from update import atualizar
from busca_avancada import filtrar

conexao = sqlite3.connect('db_agenda.sqlite3')
cursor = conexao.cursor()

while True:
    print("-"*10, "Agenda", "-"*10)
    print("(1) listar telefones")
    print("(2) adicionar telefones")
    print("(3) deletar telefones")
    print("(4) Atualizar dados")
    print("(5) busca por filtros ")
    opcao = int(input("Selecione o que deseja fazer : "))

    if opcao==0:
        print("Adeus")
        break
    elif opcao == 1:
        listar(conexao)
    elif opcao == 2:
        valores = input_dados()
        inserir_dados(valores, conexao)
        print("dados inseridos ")
    elif opcao == 3:
        listar(conexao)
        id = input("dgite o id para deletar : ")
        cursor.execute('delete from lista where id = ?', id)
        conexao.commit()
    elif opcao == 4:
        listar(conexao)
        id_atualizar = input("qual usuario voce deseja atualizar :")
        valores = input_dados()
        valores.append(id_atualizar)
        atualizar(valores, conexao)
        print("dados atualizados com sucesso")
    elif opcao == 5:
        filtrar(conexao)
    else :
        print("opcao invalida")
    
conexao.close()