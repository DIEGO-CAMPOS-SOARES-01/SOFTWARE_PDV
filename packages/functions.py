from PySide2 import *
from PySide2.QtWidgets import *
from PySide2.QtCore import *
from PySide2.QtGui import *
from packages.sqlite import *
import ctypes
import os
import subprocess
from datetime import *


tempo = datetime.now()
dt = tempo.strftime("%x")

if os.name == 'nt':
    user32 = ctypes.windll.user32
    size = user32.GetSystemMetrics(0)
else:
        output = subprocess.Popen('xrandr | grep "\*" | cut -d" " -f4',shell=True, stdout=subprocess.PIPE).communicate()[0]
        size = int(output.split()[0].split(b'x')[0])


def updateTable(collumn, uitable):
    query = select(collumn)
    uitable.clearContents()                     
    uitable.setRowCount(len(query))
    uitable.horizontalHeader().setVisible(True)
    uitable.setAlternatingRowColors(True)
    for row, text in enumerate(query):
        for column, data in enumerate(text):
            uitable.setItem(row, column, QTableWidgetItem(str(data)))
            item = uitable.item(row, column)
            if item:
                item.setTextAlignment(Qt.AlignCenter)
                uitable.resizeColumnsToContents()
                if size > 1920:
                    uitable.setStyleSheet("font-size:16px;")
                else:
                     uitable.setStyleSheet("font-size:12px;")
                
        
def showMessagebox(self,title, text):
    msg = QMessageBox(self)
    msg.setIcon(QMessageBox.Information)
    msg.setWindowTitle(title)
    msg.setStyleSheet("font-size:16px;background-color:#343434;")
    msg.setText(str(text))
    msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
    msg.setFixedSize(800,800)
    msg.exec_()

def uploadTable(self):
    updateTable('agenda', self.tableAgenda)
    updateTable('Cliente', self.tableCliente)
    updateTable('fornecedor', self.tableFornecedor)
    updateTable('produto', self.tableProduto)
    updateTable('caixa', self.tableCaixa)
    #update_table('os', self.table_os)

def update(self,  column, table):
    input = QInputDialog()
    info, ok = input.getText(self, "Atualizar", "INSIRA NOVO DADO")
    if ok:
        try:
            codigo = table.item(table.currentRow(), 0).text()
            label = table.horizontalHeaderItem(table.currentColumn()).text().lower()
            update_sql(column, label, info, codigo)
            updateTable(column, table)
            showMessagebox(self,'ATUALIZADO', "Informaçao Atualizada Com Sucesso")
        except:
            showMessagebox(self,'ERROR', "Selecione Informaçao A ser Editada")
        
    else:
        return None

def delete(self,table, uitable):
    codigo, ok = QInputDialog.getText(self, "EXCLUIR", "INSIRA O CODIGO")
    if ok:
        excluir(table, codigo)
        updateTable(table, uitable)
    else:
        return None

def search(collumn, line, uitable):
    busca = line.text()
    rows = search_in(collumn, busca)
    if not busca:
        updateTable(collumn, uitable)
    else:
        uitable.clearContents()
        uitable.setRowCount(len(rows))
        for i in range(len(rows)):  # linha
            for j in range(len(rows[0])):  # coluna     
                item = QTableWidgetItem(f"{rows[i][j]}")
                uitable.setItem(i, j, item)

def clear(self):
    current = self.ui.pages.widget(self.ui.pages.currentIndex())
    for i in current.findChildren(QLineEdit):
        i.clear()
