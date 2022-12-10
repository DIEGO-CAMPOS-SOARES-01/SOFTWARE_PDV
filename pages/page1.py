from packages.sql import *
# from sqlite import *
from packages.functions import *


def client(self):
        self.client.clicked.connect(lambda: self.pages.setCurrentWidget(self.clients))
        self.new_client.clicked.connect(lambda: self.pages.setCurrentWidget(self.add_client))
        self.back_1.clicked.connect(lambda: self.pages.setCurrentWidget(self.central))
        self.back_client.clicked.connect(lambda: self.pages.setCurrentWidget(self.clients))
        self.delete_client.clicked.connect(lambda: delete('cliente', self.table_clients))
        self.edit_client.clicked.connect(lambda: update('cliente', self.table_clients))
        self.cancel_client.clicked.connect(clear)
        self.save_client.clicked.connect(lambda: cadastro_cliente(self))
        self.search_client.textChanged.connect(lambda: search('cliente', self.search_client, self.table_clients))


def cadastro_cliente(self):
    nm = self.nome.text()
    desc = self.desc.toPlainText()
    tel1 = self.tel1.text()
    tel2 = self.tel2.text()
    cmpl = self.cmpl.text()
    end = self.end.text()
    lista = [(nm,tel1,tel2,end,cmpl,dt,desc)]
    for i in lista: str(f'{i}') 
    insert('cliente',lista)
    #show_messagebox("CADASTRADO", "Cliente Cadastrado Com Sucesso")
    clear()
    update_table("cliente", self.table_clients)
    self.pages.setCurrentWidget(self.clients)