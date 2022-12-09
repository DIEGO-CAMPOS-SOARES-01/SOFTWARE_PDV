import os
import sqlite3


con = sqlite3.connect('banco.db')
c = con.cursor()

c.execute("""CREATE TABLE IF NOT EXISTS Usuario (
    codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    nome TEXT,
    email TEXT,
    "data" TEXT,
    perfil TEXT,
    usuario TEXT,
    senha TEXT
);""")
#c.execute("insert or ignore into Usuario (perfil,usuario,senha)values ('Admin','admin','admin')")
#con.commit()

c.execute("""CREATE TABLE IF NOT EXISTS Cliente (
	codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT,
	tel1 TEXT,
	tel2 TEXT,
	endereço TEXT,
	complemento TEXT,
	"data" TEXT,
	descriçao TEXT
);""")
c.execute("""CREATE TABLE IF NOT EXISTS Fornecedor (
	codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT,
	tel1 TEXT,
    tel2 TEXT,
	endereço TEXT,
	complemento TEXT,
	email TEXT,
	observaçoes TEXT,
	"data" TEXT
);""")


c.execute("""CREATE TABLE IF NOT EXISTS Agenda (
	codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	compromisso TEXT,
	cliente TEXT,
	tel1 TEXT,
	tel2 TEXT,
	"data" TEXT,
	hora TEXT,
	endereço TEXT,
	agendado TEXT,
	observcaçoes TEXT
);""")

c.execute("""CREATE TABLE IF NOT EXISTS Trasferencia (
	codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"data" TEXT,
	entrada TEXT,
	saida TEXT,
	pagamento TEXT,
	descriçao TEXT
);""")

c.execute("""CREATE TABLE IF NOT EXISTS Produto (
	codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT,
	descriçao TEXT,
	valor TEXT,
	estoque TEXT,
	categoria TEXT,
	grupo TEXT,
	"data" TEXT
);""")

def select(table):
    c.execute(f"select * from {table}")
    result = c.fetchall()
    return result
    

def insert(table,values):
    #c.execute(f"select group_concat(name,',') from pragma_table_info('{table}')")
	
    #c.execute(f"insert into {table} ({columns[0][0][7:]}) values {values[0]}")
    #con.commit()


def update(table,column,info,codigo):
    c.execute(f"UPDATE {table} set {column} = '{info}' where codigo = {codigo}")
    con.commit()

def excluir(table, codigo):
    c.execute(f"DELETE from '{table}' WHERE codigo = '{codigo}'")
    con.commit()

def select_user(user):
    c.execute(f"select usuario,senha,perfil from Usuario where upper(trim(usuario)) == upper('{user}')")
    result = c.fetchall()
    return result

def search_in(collumn,nome):
    try:
        c.execute(f"select  * from {collumn} where upper(trim(nome)) = upper('{nome}') or codigo = '{nome}' or upper(descriçao) = upper('{nome}')")
        result = c.fetchall()
        return result
    except:
        all = select(collumn)
        return all

def select_one_produto(codigo):
    c.execute(f"SELECT nome from produtos where codigo == '{codigo}'")
    result = c.fetchall()
    return result

