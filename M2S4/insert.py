def inserir_dados(valores, conexao):
        cursor = conexao.cursor()
        sql = '''INSERT INTO lista (nome, email, ddd, telefone)
                values
                (?,?,?,?)'''
        cursor.execute(sql, valores)

        conexao.commit()
