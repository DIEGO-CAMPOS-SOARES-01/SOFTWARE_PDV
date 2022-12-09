from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt
from datetime import *
from packages.sql import *
# from sqlite import *
import ctypes
from qt_material import *


tempo = datetime.now()
dt = tempo.strftime("%x")
user32 = ctypes.windll.user32
size = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

def customs(self,app):
    extra = {'font_size': '7px'}
    extra_2 =  {'font_size': '14px'}

    if size[0] > 1920:
        self.frame.setMinimumSize(130,110)
        apply_stylesheet(app,theme = "dark_cyan.xml",extra=extra_2)
    elif size[0] > 1360:
        self.frame.setMinimumSize(110,90)
        apply_stylesheet(app,theme = "dark_cyan.xml",extra=extra_2)
    elif size[0] == 1360:
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
                if size[0] > 1920:
                    uitable.setStyleSheet("font-size:16px;")
                else:
                     uitable.setStyleSheet("font-size:12px;")
                uitable.resizeColumnsToContents()
        
def show_messagebox(title, text):
    msg = QMessageBox()
    msg.information(None, title, text)
    #msg.setIcon(QMessageBox.Question)
    #msg.setWindowTitle(title)
    msg.setStyleSheet("font-size:16px;")
    #msg.setText(str(text))
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.setFixedSize(800,800)
    msg.exec_()
    


def clear():
    for widget in qApp.allWidgets():  # widgets retorna todos os objetos de todos os widgets
        if isinstance(widget, QLineEdit):
            widget.clear()

def fill_tables(self):
    update_table('agenda', self.table_tasks)
    update_table('cliente', self.table_clients)
    update_table('produto', self.table_products)
    #update_table('usuario', self.table_users)
    update_table('transferencia', self.table_cashier)
    #update_table('os', self.table_os)


def update(column, table):
    info, ok = QInputDialog.getText(None, "Atualizar", "INSIRA NOVO DADO")
    if ok:
        try:
            codigo = table.item(table.currentRow(), 0).text()
            label = table.horizontalHeaderItem(table.currentColumn()).text().lower()
            update(column, label, info, codigo)
            update_table(column, table)
            show_messagebox('ATUALIZADO', "Informaçao Atualizada Com Sucesso")
        except:
            show_messagebox('ERROR', "Selecione Informaçao A ser Editada")
    else:
        return None

def delete(table, uitable):
    codigo, ok = QInputDialog.getText(None, "EXCLUIR", "INSIRA O CODIGO")
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