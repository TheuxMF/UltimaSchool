def atualizar (valores, conexao):
    cursor = conexao.cursor()
    sql = '''update lista set nome = ?, email = ?, ddd = ?, telefone = ? where id = ?;'''
    cursor.execute(sql, valores)
    conexao.commit()