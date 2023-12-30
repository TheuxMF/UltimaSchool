def filtrar (conexao):
    cursor = conexao.cursor()
    while True:
        print("(1)filtrar por nome\n(2) Filtrar por regiao(ddd)")
        opcao = int(input(" "))
        if opcao == 1:
            nome = input("digite o nome que deseja buscar :")
            sql = '''
            select * from lista where nome=?;
            '''
            nome = [nome]
            exibir = cursor.execute(sql,nome)
            break
            
        elif opcao == 2:
            ddd = input("digite o ddd que deseja buscar :")     
            sql = '''
            select * from lista where ddd = ?;
            '''
            ddd = [ddd]  
            exibir = cursor.execute(sql, ddd)
            break  
        else:
            print("opcao invalida")    
    for busca in exibir:
        print(busca[0], "|", busca[1], "|", busca[2],"|", busca[3], " ", busca[4])
