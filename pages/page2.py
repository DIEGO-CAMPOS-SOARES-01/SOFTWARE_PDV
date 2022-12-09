from packages.sql import *
# from sqlite import *
from packages.functions import *

def provider(self):
    self.provider.clicked.connect(lambda: self.pages.setCurrentWidget(self.providers))
    self.back_3.clicked.connect(lambda: self.pages.setCurrentWidget(self.central))
    self.edit_provider.clicked.connect(lambda: update(self,'fornecedor', self.table_provider))
    self.new_provider.clicked.connect(cadastro_fornecedor)
    self.delete_provider.clicked.connect(lambda: delete(self,'fornecedor', self.table_provider))

def cadastro_fornecedor(self):
    nm = self.nm_provider.text()
    tel1 = self.tel1_provider.text()
    tel2 = self.tel2_provider.text()

    show_messagebox('CADASTRADO', "Fornecedor Cadastrado Com Sucesso")
    clear()
    update_table('fornecedor', self.table_provider)
    self.pages.setCurrentWidget(self.providers)