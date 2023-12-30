def listar(conexao ):
    cursor = conexao.cursor()
    numeros = cursor.execute('select id, nome, email, ddd, telefone from lista;')
    print("id   |nome           |email              |telefone   ")
    for telefones in numeros:
        print(telefones[0], "|", telefones[1], "|", telefones[2],"|", telefones[3], " ", telefones[4])

        