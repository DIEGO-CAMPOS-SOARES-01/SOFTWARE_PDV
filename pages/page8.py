from PyQt5.QtWidgets import *
from packages.functions import *

def edit_pdf(self):
    self.change_pdf.triggered.connect(lambda: set_pdf(self))
    self.cancel_pdf.clicked.connect(clear)
    self.back_13.clicked.connect(lambda:self.pages.setCurrentWidget(self.central))
    self.alter_pdf_2.clicked.connect(lambda: enable_line(self))
    self.edit_pdf_2.clicked.connect(lambda: get_alter(self))

def set_pdf(self):
    self.pages.setCurrentWidget(self.alter_pdf)
    info = select('info')
    self.nome_pdf.setText(info[0][1])
    self.cpf_pdf.setText(info[0][2])
    self.end_pdf.setText(info[0][3])
    self.brr_pdf.setText(info[0][4])
    self.cdd_pdf.setText(info[0][5])
    self.uf.setText(info[0][6])
    self.cep.setText(info[0][7])
    self.tel1_pdf.setText(info[0][8])
    self.tel2_pdf.setText(info[0][9])
    self.email_pdf.setText(info[0][10])
    current = self.pages.currentWidget()
    for i in current.findChildren(QLineEdit):
        i.setEnabled(False)

def get_alter(self):
    nm = self.nome.text()
    cpf = self.cpf_pdf.text()
    end = self.end_pdf.text()
    brr = self.brr_pdf.text()
    cdd = self.cdd_pdf.text()
    uf = self.uf.text()
    cep = self.cep.text()
    tel1 = self.tel1_pdf.text()
    tel2 = self.tel2_pdf.text()
    email = self.email_pdf.text()
    lista = [nm,cpf,end,brr,cdd,uf,cep,tel1,tel2,email]

def enable_line(self):
    current = self.pages.currentWidget()
    for i in current.findChildren(QLineEdit):
        i.setEnabled(True)
        i.clear()