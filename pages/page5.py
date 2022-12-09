from packages.sql import *
# from sqlite import *
from packages.functions import *

def cashier(self):
    self.cashier_2.clicked.connect(lambda: self.pages.setCurrentWidget(self.cashier))
    self.back_8.clicked.connect(lambda: self.pages.setCurrentWidget(self.central))
    self.back_cashier.clicked.connect(lambda: self.pages.setCurrentWidget(self.cashier))
    self.new_cashier.clicked.connect(lambda: self.pages.setCurrentWidget(self.add_cashier))
    #self.add_cashier.clicked.connect(lambda: self.pages.setCurrentWidget(self.entrada_caixa))
    #self.add_entry.clicked.connect(lambda: entrada_caixa(self,self.valor.value(),''))
    #self.search_cashier.textChanged.connect(lambda: search('caixa', self.search_cashier, self.table_cashier))
    #self.delete_cashier.clicked.connect(lambda: delete(self,'caixa', self.table_cashier))
    #self.edit_cashier.clicked.connect(lambda: update(self,'caixa', self.table_cashier))

def entrada_caixa(self,valor1, valor2):
    desc = self.desc.toPlainText()
    data = self.data.text()
    forma = self.forma.currentText()
    insert(desc,data,valor1,valor2,forma)
    show_messagebox('CADASTRADO', "Entrada Cadastrada Com Sucesso")
    clear()
    update_table('transferencia', self.table_cashier)
    self.pages.setCurrentWidget(self.cashier)