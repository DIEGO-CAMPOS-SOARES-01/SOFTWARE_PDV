# from packages.sql import *
from packages.sqlite import *
from packages.functions import *

def product(self):
    self.product.clicked.connect(lambda: self.pages.setCurrentWidget(self.produto))
    self.new_product.clicked.connect(lambda: self.pages.setCurrentWidget(self.add_product))
    self.back_product.clicked.connect(lambda: self.pages.setCurrentWidget(self.produto))
    self.back_10.clicked.connect(lambda: self.pages.setCurrentWidget(self.central))
    self.cancel_product.clicked.connect(clear)
    self.save_product.clicked.connect(lambda: cadastro_produto(self))
    self.delete_product.clicked.connect(lambda: delete('produto', self.table_produto))
    self.search_product.textChanged.connect(lambda: search('produto', self.search_product, self.table_produto))
    self.edit_product.clicked.connect(lambda: update('produto', self.table_produto))


def cadastro_produto(self):
    nm = self.nm_prod.text()
    grupo = self.grup_prod.text()
    desc = self.desc_prod.toPlainText()
    qt = self.qt_prod.text()
    if self.uni.isChecked() == True:
        valor = self.valor_uni.value()
        categoria = "uni"
    elif self.m2.isChecked() == True:
        valor = self.valor_m2.value()
        categoria = "M2" 
    else:
        valor = self.valor_kg.value()
        categoria = "KG/Barra"
    lista = [(nm,desc,valor,qt,categoria,grupo,dt)]
    insert_sql('produto',lista)
    show_messagebox(self,"CADASTRADO", " Produto Cadastrado Com Sucesso")
    clear()
    update_table('produto', self.table_produto)
    self.pages.setCurrentWidget(self.produto)
