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
    self.cancel_os.clicked.connect(lambda: reset(self))
    self.remove_product.clicked.connect(lambda: delete_prod(self))
    self.cancel_client_os.clicked.connect(clear)
    self.back_os_2.clicked.connect(lambda: self.pages.setCurrentWidget(self.os))
    self.next.clicked.connect(lambda: self.tab_os.setCurrentIndex(1))  
    self.save_client_os.clicked.connect(lambda: save_client(self,True))
    self.date_aprove.setDateTime(QDateTime.currentDateTime())
    self.date_delivery.setDateTime(QDateTime.currentDateTime().addMonths(1))

def delete_prod(self):
    row = self.table_add_os.currentRow()
    if row >= 0:
        self.table_add_os.removeRow(row)
        get_total(self)
    else:
        show_messagebox(self,'Atençao','Selecione Produto A Ser Apagado')
    

def save_client(self,confirm):
    nm = self.nm_os.text()
    end = self.end_os.text()
    tel1 = self.tel1_os.text()
    tel2 = self.tel2_os.text()
    email = self.email_os.text()
    cpf = self.cpf_os.text()
    brr = self.brr_os.text()
    cdd = self.cdd_os.text()
    info = {'Nome': nm,
            'Tel1': tel1,
            'Tel2': tel2,
            'cpf': cpf,
            'email': email,
            'end': end,
            'brr': brr,
            'cdd': cdd
            }
    lista = [(nm,tel1,tel2,end,brr,cdd,email,cpf,dt,'')]
    if confirm == True:
        insert_sql('Cliente',lista)
        show_messagebox(self,"CADASTRADO", " Cliente Cadastrado Com Sucesso")
        clear()
        update_table('Cliente', self.table_Cliente)
        self.tab_os.setCurrentIndex(1)
    else:
        return info

def add_produto(self):
    cod = self.search_product_2.text()
    query = search_in('produto', cod)
    alt = self.altura.value()
    lar = self.largura.value()
    qt = self.qt.value()
    nm = self.nm_produto.text()
    com = self.comp.value()

    if query[0][5] == 'M2':
        m2 = float(query[0][3])
        valor = "{:.2f}".format(alt * lar *  qt * m2)
        

    elif query[0][5] == 'uni':
        uni = float(query[0][3])
        valor = "{:.2f}".format(uni * qt)

    
    elif query[0][5] == "KG/Barra":
        kg = float(query[0][3])
        price = kg / 6
        valor = "{:.2f}".format(price * com * qt)


    lista = [cod, nm, qt, alt, lar, com, valor]
    l = self.table_add_os.rowCount()
    self.table_add_os.insertRow(l)

    for column, text in enumerate(lista):
        self.table_add_os.setItem(l, column, QTableWidgetItem(str(text)))
    reset(self)
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
    total = get_total(self)
    info = save_client(self,False)
    info["total"] = total
    info["emiçao"] = ''
    info["delivery"] = ''
    info["obs"] = ''
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

    if self.check_aprove.isChecked:
        emiçao = self.date_aprove.date().toString(self.date_aprove.displayFormat())
        info["emiçao"] = emiçao
    
    if self.check_delivery.isChecked():
        delivery = self.date_delivery.date().toString(self.date_delivery.displayFormat())
        info["delivery"] = delivery
    
    if self.check_obs.isChecked():
        obs = self.obs_os.toPlainText()
        info["obs"] = obs
    gen_os(df,info)

def select_prod(self):
    cod = self.search_product_2.text()
    query = select_one_produto(cod)
    try:
        self.nm_produto.setText(query[0][0])
        if query[0][1] == 'M2':
            self.comp.setEnabled(False)
            self.altura.setEnabled(True)
            self.largura.setEnabled(True)

        elif query[0][1] == 'uni':
            self.altura.setEnabled(False)
            self.largura.setEnabled(False)
            self.comp.setEnabled(False)
        elif query[0][1] == "KG/Barra":
            self.altura.setEnabled(False)
            self.largura.setEnabled(False)
            self.comp.setEnabled(True)
    except:
        self.nm_produto.setText('')

def reset(self):
    self.nm_produto.clear()
    self.search_product_2.clear()
    self.altura.setValue(0.00)
    self.largura.setValue(0.00)
    self.comp.setValue(0.00)
    self.qt.setValue(1)
