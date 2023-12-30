import sqlite3

conexao = sqlite3.connect('db_agenda.sqlite3')
cursor = conexao.cursor()

sql = '''CREATE TABLE lista(
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT ,
    nome varchar(50) NOT NULL,
    email VARCHAR(4) NOT NULL,
    ddd VARCHAR(4) DEFAULT '65',
    telefone INT NOT NULL
    )'''
    
cursor.execute(sql)
conexao.commit()
conexao.close()