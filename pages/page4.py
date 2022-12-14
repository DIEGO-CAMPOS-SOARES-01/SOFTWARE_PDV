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
        self.search_task.textChanged.connect(lambda: search('agenda', self.search_agenda, self.table_agenda))

def cadastro_agenda(self):
    cadastro(self, 'agenda', 'Comprimisso Cadastrado', self.table_agenda, self.agenda)
 
