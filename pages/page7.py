# from packages.sql import *
from packages.sqlite import *
from packages.functions import *
from packages.pdf import gen_os
import pandas as pd
from subprocess import call

def os(self):
    self.os_2.clicked.connect(lambda: self.pages.setCurrentWidget(self.os))
    self.back_os.clicked.connect(lambda: self.pages.setCurrentWidget(self.os))
    self.new_os.clicked.connect(lambda: self.pages.setCurrentWidget(self.add_os))
    self.back_12.clicked.connect(lambda: self.pages.setCurrentWidget(self.central))
    self.calc.clicked.connect(lambda: call(["calc.exe"]))
    self.search_product_2.textChanged.connect(lambda: select_prod(self))
    self.insert_product.clicked.connect(lambda: add_produto(self))
    self.finish_os.clicked.connect(lambda: print_os(self))
    self.cancel_os.clicked.connect(lambda: self.table_add_os.setRowCount(0))
    self.remove_product.clicked.connect(lambda: self.table_add_os.removeRow(self.table_add_os.currentRow()))
    self.cancel_client_os.clicked.connect(clear)
    self.back_os_2.clicked.connect(lambda: self.pages.setCurrentWidget(self.os))
    self.next.clicked.connect(lambda: self.tab_os.setCurrentIndex(1))  
    self.save_client_os.clicked.connect(lambda: save_client(self))

def save_client(self):
    nm = self.nm_os.text()
    end = self.end_os.text()
    tel1 = self.tel1_os.text()
    tel2 = self.tel2_os.text()
    email = self.email_os.text()
    cpf = self.cpf_os.text()
    brr = self.brr_os.text()
    cdd = self.cdd_os.text()
    
    lista = [(nm,tel1,tel2,end,brr,cdd,email,cpf,dt,'')]
    insert_sql('Cliente',lista)
    show_messagebox(self,"CADASTRADO", " Cliente Cadastrado Com Sucesso")
    clear()
    update_table('Cliente', self.table_Cliente)
    self.tab_os.setCurrentIndex(1)
    
def add_produto(self):
    cod = self.search_product_2.text()
    query = search_in('produto', cod)
    alt = self.altura.value()
    lar = self.largura.value()
    qt = self.qt.value()
    nm = self.nm_produto.text()
    com = 0

    if query[0][5] == 'M2':
        m2 = query[0][3]
        valor = "{:.2f}".format(alt * lar * float(m2) * qt)

    elif query[0][5] == 'uni':
        valor = query[0][3]
        

    lista = [cod, nm, qt, alt, lar, com, valor]
    l = self.table_add_os.rowCount()
    self.table_add_os.insertRow(l)

    for column, text in enumerate(lista):
        self.table_add_os.setItem(l, column, QTableWidgetItem(str(text)))
        self.table_add_os.setItem(l, 6, QTableWidgetItem(str(lista[6])))
        self.table_add_os.resizeColumnsToContents()
    self.nm_produto.clear()
    self.search_product_2.clear()
    get_total(self)

def get_total(self):
    checked_list = []
    for i in range(self.table_add_os.rowCount()):
        checked_list.append(str(self.table_add_os.item(i, 6).text()))
    r = 0
    for i in checked_list:
        r += float(i)
        self.total.setText(str("{:.2f}".format(r)))
    return r

def print_os(self):
        dados = []
        all_dados = []
        for row in range(self.table_add_os.rowCount()):
            for column in range (self.table_add_os.columnCount()):
                dados.append(str(self.table_add_os.item(row,column).text()))

            all_dados.append(dados)
            dados = []
        colunas = ['Codigo','Descrição','QT','largura','altura','Comprimento','Valor']

        data = pd.DataFrame(all_dados,columns=colunas)
        df = data.style.hide_index()
        total = get_total(self)
        gen_os(df,total)

def excluir_produto(self):
    self.table_add_os.removeRow(self.table_add_os.currentRow())
    get_total()


def select_prod(self):
    cod = self.search_product_2.text()
    produto = select_one_produto(cod)
    try:
        self.nm_produto.setText(produto[0][0])
    except:
        self.nm_produto.setText('')
