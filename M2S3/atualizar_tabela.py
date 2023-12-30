import sqlite3

conecxao=sqlite3.connect('M2S3\db_fornecedor.sqlite3')
cursor=conecxao.cursor()

sql='''CREATE TABLE IF NOT EXISTS Fornecedor (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    endereco TEXT NOT NULL,
                    produto TEXT NOT NULL 
                )'''

cursor.execute(sql)
conecxao.commit()

sql ='''INSERT INTO Fornecedor
            (nome, endereco, produto)
            values
            ('Empresa de Leite Parmaleite', 'Rua dos Leites, 23', 'Leite'),
            ('Peixaria Abril' , 'Rua dos Leites, 26', 'Peixe'),
            ('Açougue Legal', 'Rua das Carnes, 30', 'Carne'),
            ('Açougue Novo', 'Rua das Carnes, 50', 'Carne' ) 
'''

cursor.execute(sql)
conecxao.commit()


sql = '''UPDATE Fornecedor SET endereco='Rua dos Peixes, 26' WHERE id=2'''

cursor.execute(sql)
conecxao.commit()

sql = '''DELETE from Fornecedor where id == 3 '''
cursor.execute(sql)
sql = '''DELETE from Fornecedor where id == 4''' 
cursor.execute(sql)

sql ='''

    INSERT INTO Fornecedor
            (id, nome, endereco, produto)
            values
            (3, 'Padaria do Pão', 'Rua dos Pães, 32', 'Pão'),
            (4, 'Marcenaria Martelo' , 'Rua dos martelos, 62', 'Martelo')
'''



cursor.execute(sql)
conecxao.commit()

sql = '''update Fornecedor set endereco='Rua dos Peixes, 26' where id=2'''

cursor.execute(sql)
conecxao.commit()

sql = "SELECT * FROM Fornecedor"

cursor.execute(sql)


for dados in cursor.fetchall():
    print(dados)
    
sql = '''SELECT * FROM Fornecedor where produto=='Carne' '''

cursor.execute(sql)
for dados in cursor.fetchall():
    
    print(dados)

sql = '''DELETE from Fornecedor where id == 1'''

cursor.execute(sql)
conecxao.commit()

sql = "SELECT * FROM Fornecedor"

cursor.execute(sql)

for dados in cursor.fetchall():
    print(dados)


conecxao.close()