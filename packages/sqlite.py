import os
import sqlite3

home_directory = os.path.expanduser( '~' )
path = os.path.join( home_directory,'Xsession.db')

 

con = sqlite3.connect(path)
c = con.cursor()


c.execute("""CREATE TABLE IF NOT EXISTS Cliente (
	Codigo INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT,
	tel1 TEXT(18),
	tel2 TEXT(18),
	endereço TEXT,
	bairro TEXT,
	cidade TEXT,
	email TEXT,
	cpf TEXT(15),
	"data" TEXT(10),
	descriçao TEXT
);
""")
c.execute("""CREATE TABLE IF NOT EXISTS fornecedor (
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


c.execute("""CREATE TABLE IF NOT EXISTS agenda (
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

c.execute("""CREATE TABLE IF NOT EXISTS caixa (
	codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	"data" TEXT,
	entrada TEXT,
	saida TEXT,
	pagamento TEXT,
	descriçao TEXT
);""")

c.execute("""CREATE TABLE IF NOT EXISTS produto (
	codigo INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
	nome TEXT,
	descriçao TEXT,
	valor TEXT,
	estoque TEXT,
	categoria TEXT,
	grupo TEXT,
	"data" TEXT
);""")
c.execute("""CREATE TABLE IF NOT EXISTS info (
	codigo INTEGER PRIMARY KEY AUTOINCREMENT,
	nome TEXT,
	cnpj TEXT,
	endereço TEXT,
	bairro TEXT,
	municipio TEXT,
	UF TEXT,
	cep TEXT,
	tel1 TEXT,
	tel2 TEXT,
	email TEXT
);""")
con.commit()

def info():
	result = select('info')
	if result:
		pass
	else:
		c.execute("""INSERT  INTO info 
		VALUES 
		(0,'NOME DA LOJA', 'X.XXX.XXX/0001-XX', 'ENDEREÇO DA LOJA', 'Bairro','Cidade','UF','CEP','(21)99999-9999','(21)99999-9999','email@gamil.com')""")
		con.commit()

def select(table):
    c.execute(f"select * from {table}")
    result = c.fetchall()
    return result
    

def insert_sql(table,values):
	c.execute(f"select group_concat(name,',') from pragma_table_info('{table}')")
	columns = c.fetchall()
	c.execute(f"insert into {table} ({columns[0][0][7:]}) values {values[0]}")
	con.commit()


def update_sql(table,column,info,codigo):
	try:
		c.execute(f"UPDATE {table} set {column} = '{info}' where codigo = {codigo}")
		con.commit()
	except:
		pass

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
    c.execute(f"SELECT nome,categoria from produto where codigo == '{codigo}'")
    result = c.fetchall()
    return result

info()