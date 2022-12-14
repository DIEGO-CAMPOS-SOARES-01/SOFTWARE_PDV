from packages.sqlite import *
from packages.functions import *

def client(self):
        self.client.clicked.connect(lambda: self.pages.setCurrentWidget(self.Cliente))
        self.new_client.clicked.connect(lambda: self.pages.setCurrentWidget(self.add_client))
        self.back_1.clicked.connect(lambda: self.pages.setCurrentWidget(self.central))
        self.back_client.clicked.connect(lambda: self.pages.setCurrentWidget(self.Cliente))
        self.delete_client.clicked.connect(lambda: delete(self,'cliente', self.table_Cliente))
        self.edit_client.clicked.connect(lambda: update(self,'Cliente', self.table_Cliente))
        self.cancel_client.clicked.connect(lambda: clear(self))
        self.save_client.clicked.connect(lambda: cadastro(self,'Cliente','Cliente Cadastrado',self.table_Cliente,self.Cliente))
        self.search_client.textChanged.connect(lambda: search('Cliente', self.search_client, self.table_Cliente))