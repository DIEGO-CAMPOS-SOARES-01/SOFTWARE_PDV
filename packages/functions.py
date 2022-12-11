from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from datetime import *
#from packages.sql import *
from packages.sqlite import *
import ctypes
import os
import subprocess
from qt_material import *



tempo = datetime.now()
dt = tempo.strftime("%x")

if os.name == 'nt':
    user32 = ctypes.windll.user32
    size = user32.GetSystemMetrics(0)
else:
        output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
        size = int(output.split()[0].split(b'x')[0])

def customs(self,app):
    extra = {'font_size': '7px'}
    extra_2 =  {'font_size': '14px'}
    if size > 1920:
        self.frame.setMinimumSize(130,110)
        apply_stylesheet(app,theme = "dark_cyan.xml",extra=extra_2)
    elif size > 1360:
        self.frame.setMinimumSize(110,90)
        apply_stylesheet(app,theme = "dark_cyan.xml",extra=extra_2)
    elif size == 1360:
        self.frame.setMinimumSize(90,70)
        apply_stylesheet(app,theme = "dark_cyan.xml",extra=extra)


def update_table(collumn, uitable):
    query = select(collumn)
    uitable.clearContents()                     
    uitable.setRowCount(len(query))
    uitable.horizontalHeader().setVisible(True)
    for row, text in enumerate(query):
        for column, data in enumerate(text):
            uitable.setItem(row, column, QTableWidgetItem(str(data)))
            item = uitable.item(row, column)
            if item:
                item.setTextAlignment(Qt.AlignCenter)
                if size > 1920:
                    uitable.setStyleSheet("font-size:16px;")
                else:
                     uitable.setStyleSheet("font-size:12px;")
                uitable.resizeColumnsToContents()
        
def show_messagebox(self,title, text):
    msg = QMessageBox(self)
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(title)
    msg.setStyleSheet("font-size:16px;")
    msg.setText(str(text))
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.setFixedSize(800,800)
    msg.exec_()
    


def clear():
    for widget in qApp.allWidgets():  # widgets retorna todos os objetos de todos os widgets
        if isinstance(widget, QLineEdit):
            widget.clear()

def fill_tables(self):
    update_table('agenda', self.table_agenda)
    update_table('Cliente', self.table_Cliente)
    update_table('fornecedor', self.table_fornecedor)
    update_table('produto', self.table_produto)
    #update_table('usuario', self.table_users)
    update_table('caixa', self.table_caixa)
    #update_table('os', self.table_os)


def update(column, table):
    info, ok = QInputDialog.getText(None, "Atualizar", "INSIRA NOVO DADO")
    if ok:
        codigo = table.item(table.currentRow(), 0).text()
        label = table.horizontalHeaderItem(table.currentColumn()).text().lower()
        update_sql(column, label, info, codigo)
        update_table(column, table)
        #show_messagebox('ATUALIZADO', "Informaçao Atualizada Com Sucesso")

        #show_messagebox('ERROR', "Selecione Informaçao A ser Editada")
    else:
        return None

def delete(self,table, uitable):
    codigo, ok = QInputDialog.getText(self, "EXCLUIR", "INSIRA O CODIGO")
    if ok:
        excluir(table, codigo)
        update_table(table, uitable)
    else:
        return None

def search(collumn, line, uitable):
    busca = line.text()
    rows = search_in(collumn, busca)
    if not busca:
        update_table(collumn, uitable)
    else:
        uitable.clearContents()
        uitable.setRowCount(len(rows))
        for i in range(len(rows)):  # linha
            for j in range(len(rows[0])):  # coluna     
                item = QTableWidgetItem(f"{rows[i][j]}")
                uitable.setItem(i, j, item)

def atalho(p, f):
    QShortcut("Return" , p).activated.connect(f)    