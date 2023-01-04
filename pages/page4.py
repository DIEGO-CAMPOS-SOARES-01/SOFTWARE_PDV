# from packages.sql import *
from packages.sqlite import *
from packages.functions import *

def task(self):
        self.task.clicked.connect(lambda: self.pages.setCurrentWidget(self.agenda))
        self.new_task.clicked.connect(lambda: self.pages.setCurrentWidget(self.add_task))
        self.back_task.clicked.connect(lambda: self.pages.setCurrentWidget(self.agenda))
        self.back_6.clicked.connect(lambda: self.pages.setCurrentWidget(self.central))
        self.delete_task.clicked.connect(lambda: delete(self,'agenda', self.table_agenda))
        self.cancel_task.clicked.connect(clear)
        self.save_task.clicked.connect(lambda: cadastro_agenda(self))
        self.edit_task.clicked.connect(lambda: update(self,'agenda', self.table_agenda))
        self.search_task.textChanged.connect(lambda: search('agenda', self.search_task, self.table_agenda))

def cadastro_agenda(self):
    cmp = self.comp.text()
    nm = self.cliente.text()
    tel1 = self.tel1_3.text() 
    tel2 = self.tel2_3.text()
    data = self.data.text()
    hora = self.hora.text()
    end = self.end_2.text()
    obs = self.obs_agenda.toPlainText()
    
    values = [(cmp,nm,tel1,tel2,data,hora,end,dt,obs)]
    
    insert_sql('agenda',values) 
    show_messagebox(self,"CADASTRADO", "Compromisso Cadastrado Com Sucesso")
    clear(self)
    update_table('agenda',self.table_agenda)
    self.pages.setCurrentWidget(self.agenda)

 
