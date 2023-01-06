from PySide2 import*
from ui_main import *
from Custom_Widgets.Widgets import *
import sys

settings = QSettings()

app = QApplication([])

class Main(QMainWindow):
    def __init__(self):
        super(Main, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        loadJsonStyle(self, self.ui)



if __name__ == "__main__":

    w = Main()
    w.show()
    sys.exit(app.exec_())