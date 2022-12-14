# from packages.sql import *
from packages.sqlite import *
from packages.functions import *

def cashier(self):
    self.cashier_2.clicked.connect(lambda: self.pages.setCurrentWidget(self.caixa))
    self.back_8.clicked.connect(lambda: self.pages.setCurrentWidget(self.central))
    self.back_cashier.clicked.connect(lambda: self.pages.setCurrentWidget(self.caixa))
    self.new_cashier.clicked.connect(lambda: self.pages.setCurrentWidget(self.add_cashier))
    self.add_entry.clicked.connect(lambda: entrada_caixa(self,True))
    self.add_out.clicked.connect(lambda: entrada_caixa(self,False))
    self.search_cashier.textChanged.connect(lambda: search('caixa', self.search_cashier, self.table_caixa))
    self.delete_cashier.clicked.connect(lambda: delete(self,'caixa', self.table_caixa))
    self.delete_cashier.clicked.connect(lambda: get_total(self))
    self.edit_cashier.clicked.connect(lambda: update(self,'caixa', self.table_caixa))
    self.edit_cashier.clicked.connect(lambda: get_total(self))
    self.date_cashier.setDateTime(QDateTime.currentDateTime())
    get_total(self)

def entrada_caixa(self,entry):
    desc = self.desc.toPlainText()
    data = self.data.text()
    forma = self.forma.currentText()
    valor = self.valor.value()
    if entry == True:
        lista = [(data,valor,'',forma,desc)]
        insert_sql('caixa',lista)
        show_messagebox(self,'CADASTRADO', "Entrada Cadastrada Com Sucesso")
    else:
        lista = [(data,'',valor,forma,desc)]
        insert_sql('caixa',lista)
        show_messagebox(self,'CADASTRADO', "Saida Cadastrada Com Sucesso")
    clear()
    update_table('caixa', self.table_caixa)
    get_total(self)
    self.pages.setCurrentWidget(self.caixa)

def get_total(self):
    entrada = []
    for i in range(self.table_caixa.rowCount()):
        entrada.append(str(self.table_caixa.item(i, 2).text()))
    value_entry = 0
    for i in entrada:
        value_entry += float(i.strip() or 0)
    saida = []
    for i in range(self.table_caixa.rowCount()):
        saida.append(str(self.table_caixa.item(i, 3).text()))
    value_out = 0
    for i in saida:
        value_out += float(i.strip() or 0)
    saldo = value_entry - value_out
    self.saldo.setText(str("{:.2f}".format(saldo)))
