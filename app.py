from PyQt5.QtWidgets import *
from PyQt5 import uic
from pages import page1, page2,page4, page5, page6,page7
from packages.functions import *
from packages import icons
# from ui_tela import Ui_widget

app = QApplication([])


class Main(QWidget):
    def __init__(self):
        super(Main, self).__init__()
        uic.loadUi('tela.ui', self)
        customs(self,app)
        fill_tables(self)

        page1.client(self)
        page2.provider(self)
        page4.task(self)
        page6.product(self)
        page5.cashier(self)
        page7.os(self)

if __name__ == "__main__":
    import sys
    w = Main()
    w.showMaximized()
    sys.exit(app.exec_())