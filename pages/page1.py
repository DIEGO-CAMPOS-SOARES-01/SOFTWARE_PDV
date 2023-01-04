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
        self.save_client.clicked.connect(lambda: cadastro_cliente(self))
        self.search_client.textChanged.connect(lambda: search('Cliente', self.search_client, self.table_Cliente))

def cadastro_cliente(self):
    nome = self.nm_cliente.text()
    tel1 = self.tel1.text()
    tel2 = self.tel2.text()
    end = self.end.text()
    brr = self.brr.text()
    cdd = self.cdd.text()
    email = self.email.text()
    cpf = self.cpf.text()
    desc =  self.desc.toPlainText()

    values = [(nome,tel1,tel2,end,brr,cdd,email,cpf,dt,desc)]
    
    insert_sql('cliente',values)
    show_messagebox(self,"CADASTRADO", "Cliente Cadastrado Com Sucesso")
    clear(self)
    update_table('cliente', self.table_Cliente)
    self.pages.setCurrentWidget(self.Cliente)