# from packages.sql import *
from packages.sqlite import *
from packages.functions import *

def provider(self):
    self.provider.clicked.connect(lambda: self.pages.setCurrentWidget(self.fornecedor))
    self.new_provider.clicked.connect((lambda: self.pages.setCurrentWidget(self.add_provider)))
    self.back_3.clicked.connect(lambda: self.pages.setCurrentWidget(self.central))
    self.edit_provider.clicked.connect(lambda: update('fornecedor', self.table_fornecedor))
    self.save_provider.clicked.connect(lambda: cadastro_fornecedor(self))
    self.delete_provider.clicked.connect(lambda: delete(self,'fornecedor', self.table_fornecedor))
    self.search_provider.textChanged.connect(lambda: search('fornecedor', self.search_provider, self.table_fornecedor))


def cadastro_fornecedor(self):
    nm = self.nome_provider.text()
    tel1 = self.tel1_provider.text()
    tel2 = self.tel2_provider.text()
    end = self.end_provider.text()
    cmpl = self.cmpl_provider.text()
    email = self.email_provider.text()
    obs = self.obs_provider.toPlainText()
    lista = [(nm,tel1,tel2,end,cmpl,email,obs,dt)]
    insert_sql('fornecedor',lista)
    show_messagebox(self,"CADASTRADO", " Fornecedor Cadastrado Com Sucesso")
    clear()
    update_table('fornecedor', self.table_fornecedor)
    self.pages.setCurrentWidget(self.fornecedor)
