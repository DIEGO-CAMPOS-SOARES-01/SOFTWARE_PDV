import mysql.connector
from mysql.connector import Error

try:
    con = mysql.connector.connect(host='localhost',database='banco',user='root',password='1234')
    c= con.cursor(buffered=True)
    c.execute("select database();")
    if con.is_connected():
        db_Info = con.get_server_info()
        print("Connected to MySQL Server version ", db_Info)
        
        record = c.fetchone()
        print("You're connected to database: ", record)

except Error as e:
    print("Error while connecting to MySQL", e)

c.execute("""CREATE TABLE IF NOT EXISTS `banco`.`cliente` (
  `codigo` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NULL,
  `tel1` VARCHAR(18) NULL,
  `tel2` VARCHAR(18) NULL,
  `endereço` VARCHAR(100) NULL,
  `complemento` VARCHAR(100) NULL,
  `data` VARCHAR(10) NULL,
  `descriçao` VARCHAR(200) NULL,
  PRIMARY KEY (`codigo`),
  UNIQUE INDEX `codigo_UNIQUE` (`codigo` ASC) VISIBLE,
  UNIQUE INDEX `tel1_UNIQUE` (`tel1` ASC) VISIBLE,
  UNIQUE INDEX `tel2_UNIQUE` (`tel2` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;""")
con.commit()


c.execute("""CREATE TABLE IF NOT EXISTS `banco`.`fornecedor` (
  `codigo` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NULL,
  `tel1` VARCHAR(18) NULL,
  `tel2` VARCHAR(18) NULL,
  `endereço` VARCHAR(100) NULL,
  `complemento` VARCHAR(100) NULL,
  `email` VARCHAR(100) NULL,
  `observaçoes` VARCHAR(200) NULL,
  `data` VARCHAR(10) NULL,
  PRIMARY KEY (`codigo`))
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;""")
con.commit()


c.execute("""CREATE TABLE IF NOT EXISTS`banco`.`usuario` (
  `codigo` INT NOT NULL,
  `nome` VARCHAR(45) NULL,
  `email` VARCHAR(45) NULL,
  `data` VARCHAR(10) NULL,
  `perfil` VARCHAR(5) NULL,
  `usuario` VARCHAR(45) NULL,
  `senha` VARCHAR(45) NULL,
  PRIMARY KEY (`codigo`),
  UNIQUE INDEX `codigo_UNIQUE` (`codigo` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;
""")
con.commit()


c.execute("""CREATE TABLE IF NOT EXISTS `banco`.`agenda` (
  `codigo` INT NOT NULL AUTO_INCREMENT,
  `compromisso` VARCHAR(100) NULL,
  `cliente` VARCHAR(100) NULL,
  `tel1` VARCHAR(18) NULL,
  `tel2` VARCHAR(18) NULL,
  `data` VARCHAR(10) NULL,
  `hora` VARCHAR(5) NULL,
  `endereço` VARCHAR(100) NULL,
  `agendado` VARCHAR(10) NULL,
  `observaçoes` VARCHAR(200) NULL,
  PRIMARY KEY (`codigo`),
  UNIQUE INDEX `codigo_UNIQUE` (`codigo` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;""")
con.commit()


c.execute("""CREATE TABLE IF NOT EXISTS `banco`.`transferencia` (
  `codigo` INT NOT NULL AUTO_INCREMENT,
  `data` VARCHAR(10) NULL,
  `entrada` VARCHAR(20) NULL,
  `saida` VARCHAR(20) NULL,
  `pagamento` VARCHAR(15) NULL,
  `descriçao` VARCHAR(100) NULL,
  PRIMARY KEY (`codigo`),
  UNIQUE INDEX `codigo_UNIQUE` (`codigo` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;""")
con.commit()


c.execute("""CREATE TABLE IF NOT EXISTS`banco`.`produto` (
  `codigo` INT NOT NULL AUTO_INCREMENT,
  `nome` VARCHAR(100) NULL,
  `descriçao` VARCHAR(100) NULL,
  `valor` VARCHAR(20) NULL,
  `estoque` VARCHAR(5) NULL,
  `categoria` VARCHAR(45) NULL,
  `grupo` VARCHAR(45) NULL,
  `data` VARCHAR(10) NULL,
  PRIMARY KEY (`codigo`),
  UNIQUE INDEX `codigo_UNIQUE` (`codigo` ASC) VISIBLE)
ENGINE = InnoDB
DEFAULT CHARACTER SET = utf8mb4;""")
con.commit()

def select(table):
    c.execute(f"select * from {table}")
    result = c.fetchall()
    return result
    

def insert(table,values):
  c.execute(f"select * from {table}")
  field = [field[0] for field in c.description]
  #print(f"insert into {table} ({field}) values {values}")
  c.execute(f'INSERT INTO {table} (' + ', '.join(field[1:]) + ')' + f"VALUES {values[0]}")
  con.commit()

def update_sql(table,column,info,codigo):
    c.execute(f"UPDATE {table} set {column} = '{info}' where codigo = {codigo}")
    con.commit()

def excluir(table, codigo):
    c.execute(f"DELETE from {table} WHERE codigo = {codigo}")
    con.commit()

def select_user(user):
    c.execute(f"select usuario,senha,perfil from Usuario where upper(trim(usuario)) == upper('{user}')")
    result = c.fetchall()
    return result

def search_in(collumn,nome):

    c.execute(f"select  * from {collumn} where upper(trim(nome)) = upper('{nome}') or codigo = {nome} or upper(descriçao) = upper('{nome}')")
    result = c.fetchall()
    if result:
      return result
    else:
      return []


def select_one_produto(codigo):
  try:
    c.execute(f"SELECT nome from produto where codigo = {codigo}")
    result = c.fetchall()
    return result
  except:
    pass