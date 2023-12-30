'''Crie um programa em Python que gere tabelas para uma aplicação de gerenciamento de tarefas. As tabelas devem compreender as seguintes funcionalidades:
As tarefas devem ser divididas em “categorias”;
Uma tarefa deve ter nome, data, categoria e status de conclusão (se foi realizada ou não); 
As restrições/relacionamentos devem fazer sentido'''
import sqlite3

conecxao=sqlite3.connect('db_tarefas.sqlite3')
cursor=conecxao.cursor()

sql='''CREATE TABLE IF NOT EXISTS categorias (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL
                )'''

cursor.execute(sql)
conecxao.commit()

sql='''CREATE TABLE IF NOT EXISTS tarefas (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    nome TEXT NOT NULL,
                    data DATE NOT NULL,
                    categoria_id INTEGER NOT NULL,
                    concluida INTEGER,
                    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
                )'''
cursor.execute(sql)

conecxao.close()
