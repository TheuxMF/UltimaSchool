'''Crie um programa em Python que gere tabelas para uma aplicação de gerenciamento de tarefas. As tabelas devem compreender as seguintes funcionalidades:
As tarefas devem ser divididas em “categorias”;
Uma tarefa deve ter nome, data, categoria e status de conclusão (se foi realizada ou não); 
As restrições/relacionamentos devem fazer sentido.'''

import sqlite3

conecxao=sqlite3.connect('db_eventos.sqlite3')
cursor=conecxao.cursor()

sql='''CREATE TABLE IF NOT EXISTS organizadores (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    email TEXT NOT NULL,
                    cpf TEXT NOT NULL UNIQUE
                )'''

cursor.execute(sql)
conecxao.commit()

sql='''CREATE TABLE IF NOT EXISTS eventos (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    titulo TEXT NOT NULL,
                    data DATE NOT NULL,
                    local TEXT NOT NULL,
                    organizador_id INTEGER NOT NULL,
                    FOREIGN KEY (organizador_id) REFERENCES organizadores(id)
                )'''

cursor.execute(sql)
conecxao.commit()
conecxao.close()