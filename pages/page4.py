from packages.sql import *
# from sqlite import *
from packages.functions import *

def task(self):
        self.task.clicked.connect(lambda: self.pages.setCurrentWidget(self.tasks))
        self.new_task.clicked.connect(lambda: self.pages.setCurrentWidget(self.add_task))
        self.back_task.clicked.connect(lambda: self.pages.setCurrentWidget(self.tasks))
        self.back_6.clicked.connect(lambda: self.pages.setCurrentWidget(self.central))
        self.delete_task.clicked.connect(lambda: delete('agenda', self.table_tasks))
        self.cancel_task.clicked.connect(clear)
        self.save_task.clicked.connect(lambda: cadastro_agenda(self))
        self.edit_task.clicked.connect(lambda: update('agenda', self.table_tasks))
        self.search_task.textChanged.connect(lambda: search('agenda', self.search_agenda, self.table_tasks))

def cadastro_agenda(self):
    comp = self.com.text()
    nm = self.cliente.text()
    end = self.end.text()
    tel1 = self.tel1.text()
    tel2 = self.tel2.text()
    obs = self.obs.toPlainText()
    data = self.data.text()
    hora = self.hora.text()
    lista = [(comp,nm,tel1,tel2,data,hora,end,dt,obs)]
    for i in lista: str(f'{i}') 
    insert('agenda',lista)
    self.pages.setCurrentWidget(self.tasks)