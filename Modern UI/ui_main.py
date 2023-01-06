# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainlzqOAZ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from Custom_Widgets.Widgets import QCustomSlideMenu


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1329, 770)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"*{\n"
"	border: none;\n"
"	background-color: transparent;\n"
"	color: #fff;\n"
"}\n"
"#centralwidget{\n"
"	background-color: #040f13;\n"
"}\n"
"#header_menu{\n"
"	background-color: rgb(12, 12, 12);\n"
"}\n"
"#side_menu{\n"
"	background-color: #071e26;\n"
"	border-radius: 20px;\n"
"}\n"
"QPushButton{\n"
"	padding: 10px;\n"
"	background-color: #040f13;\n"
"	border-radius: 5px;\n"
"}\n"
"#body{\n"
"	background-color: #071e26;\n"
"	border-radius: 10px;\n"
"}\n"
"QLineEdit{\n"
"	border-bottom: 3px solid  rgb(0, 255, 247);\n"
"	border-radius:2px;\n"
"}\n"
"QTableWidget{\n"
"	background-color: rgb(36, 36, 36);\n"
"}\n"
"QHeaderView:section{\n"
"	background-color: rgb(26, 12, 26);\n"
"	height:40px;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.header_menu = QFrame(self.centralwidget)
        self.header_menu.setObjectName(u"header_menu")
        self.header_menu.setMinimumSize(QSize(0, 50))
        self.header_menu.setFrameShape(QFrame.StyledPanel)
        self.header_menu.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_7 = QHBoxLayout(self.header_menu)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label = QLabel(self.header_menu)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))
        font = QFont()
        font.setPointSize(10)
        self.label.setFont(font)

        self.horizontalLayout_7.addWidget(self.label)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer)

        self.minimize = QPushButton(self.header_menu)
        self.minimize.setObjectName(u"minimize")
        self.minimize.setMinimumSize(QSize(50, 40))
        self.minimize.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_7.addWidget(self.minimize)

        self.maximize = QPushButton(self.header_menu)
        self.maximize.setObjectName(u"maximize")
        self.maximize.setMinimumSize(QSize(50, 40))
        self.maximize.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_7.addWidget(self.maximize)

        self.close = QPushButton(self.header_menu)
        self.close.setObjectName(u"close")
        self.close.setMinimumSize(QSize(50, 40))
        self.close.setMaximumSize(QSize(40, 16777215))

        self.horizontalLayout_7.addWidget(self.close)


        self.verticalLayout.addWidget(self.header_menu)

        self.header = QFrame(self.centralwidget)
        self.header.setObjectName(u"header")
        self.header.setMinimumSize(QSize(0, 70))
        self.header.setMaximumSize(QSize(16777215, 50))
        self.header.setFrameShape(QFrame.StyledPanel)
        self.header.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.header)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.frame = QFrame(self.header)
        self.frame.setObjectName(u"frame")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.frame)
        self.horizontalLayout_4.setSpacing(0)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.menu = QPushButton(self.frame)
        self.menu.setObjectName(u"menu")
        self.menu.setMinimumSize(QSize(70, 40))
        self.menu.setMaximumSize(QSize(16777215, 30))

        self.horizontalLayout_4.addWidget(self.menu, 0, Qt.AlignHCenter|Qt.AlignVCenter)


        self.horizontalLayout_2.addWidget(self.frame, 0, Qt.AlignLeft)

        self.frame_3 = QFrame(self.header)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_3 = QHBoxLayout(self.frame_3)
        self.horizontalLayout_3.setSpacing(25)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")

        self.horizontalLayout_2.addWidget(self.frame_3)


        self.verticalLayout.addWidget(self.header)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy)
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame_2)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.side_menu = QCustomSlideMenu(self.frame_2)
        self.side_menu.setObjectName(u"side_menu")
        self.side_menu.setStyleSheet(u"QPushButton:hover{\n"
"border-left:5px solid red;\n"
"}")
        self.verticalLayout_2 = QVBoxLayout(self.side_menu)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame_4 = QFrame(self.side_menu)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setMinimumSize(QSize(150, 0))
        self.frame_4.setMaximumSize(QSize(150, 16777215))
        self.frame_4.setStyleSheet(u"")
        self.frame_4.setFrameShape(QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame_4)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.btn_home = QPushButton(self.frame_4)
        self.btn_home.setObjectName(u"btn_home")

        self.verticalLayout_3.addWidget(self.btn_home)

        self.btn_cliente = QPushButton(self.frame_4)
        self.btn_cliente.setObjectName(u"btn_cliente")
        self.btn_cliente.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.btn_cliente)

        self.btn_fornecedor = QPushButton(self.frame_4)
        self.btn_fornecedor.setObjectName(u"btn_fornecedor")
        self.btn_fornecedor.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.btn_fornecedor)

        self.btn_agenda = QPushButton(self.frame_4)
        self.btn_agenda.setObjectName(u"btn_agenda")
        self.btn_agenda.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.btn_agenda)

        self.btn_caixa = QPushButton(self.frame_4)
        self.btn_caixa.setObjectName(u"btn_caixa")
        self.btn_caixa.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.btn_caixa)

        self.btn_produtos = QPushButton(self.frame_4)
        self.btn_produtos.setObjectName(u"btn_produtos")
        self.btn_produtos.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.btn_produtos)

        self.btn_os = QPushButton(self.frame_4)
        self.btn_os.setObjectName(u"btn_os")
        self.btn_os.setMinimumSize(QSize(0, 40))

        self.verticalLayout_3.addWidget(self.btn_os)


        self.verticalLayout_2.addWidget(self.frame_4, 0, Qt.AlignTop)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.settings = QPushButton(self.side_menu)
        self.settings.setObjectName(u"settings")
        self.settings.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.settings)

        self.help = QPushButton(self.side_menu)
        self.help.setObjectName(u"help")
        self.help.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.help)

        self.about = QPushButton(self.side_menu)
        self.about.setObjectName(u"about")
        self.about.setMinimumSize(QSize(0, 40))

        self.verticalLayout_2.addWidget(self.about)


        self.horizontalLayout.addWidget(self.side_menu, 0, Qt.AlignLeft)

        self.body = QFrame(self.frame_2)
        self.body.setObjectName(u"body")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.body.sizePolicy().hasHeightForWidth())
        self.body.setSizePolicy(sizePolicy1)
        self.body.setFrameShape(QFrame.StyledPanel)
        self.body.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.body)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.frame_5 = QFrame(self.body)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_5)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.pages = QStackedWidget(self.frame_5)
        self.pages.setObjectName(u"pages")
        self.central = QWidget()
        self.central.setObjectName(u"central")
        self.pages.addWidget(self.central)
        self.cliente = QWidget()
        self.cliente.setObjectName(u"cliente")
        self.verticalLayout_7 = QVBoxLayout(self.cliente)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.frame_6 = QFrame(self.cliente)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.frame_6)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_8)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_2 = QLabel(self.frame_8)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout_6.addWidget(self.label_2)

        self.lineEdit = QLineEdit(self.frame_8)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(300, 0))
        self.lineEdit.setStyleSheet(u"")

        self.verticalLayout_6.addWidget(self.lineEdit)


        self.verticalLayout_8.addLayout(self.verticalLayout_6)


        self.horizontalLayout_5.addWidget(self.frame_8, 0, Qt.AlignLeft|Qt.AlignVCenter)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.frame_9)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.pushButton_14 = QPushButton(self.frame_9)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(50, 0))
        self.pushButton_14.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.pushButton_14)

        self.pushButton_12 = QPushButton(self.frame_9)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(50, 0))
        self.pushButton_12.setMaximumSize(QSize(16777215, 16777215))

        self.horizontalLayout_6.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.frame_9)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_6.addWidget(self.pushButton_13)

        self.pushButton_8 = QPushButton(self.frame_9)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(50, 0))

        self.horizontalLayout_6.addWidget(self.pushButton_8)


        self.horizontalLayout_5.addWidget(self.frame_9)


        self.verticalLayout_7.addWidget(self.frame_6)

        self.frame_7 = QFrame(self.cliente)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy)
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_7)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.tableWidget = QTableWidget(self.frame_7)
        if (self.tableWidget.columnCount() < 11):
            self.tableWidget.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(210)

        self.verticalLayout_9.addWidget(self.tableWidget)


        self.verticalLayout_7.addWidget(self.frame_7)

        self.pages.addWidget(self.cliente)
        self.fornecedor = QWidget()
        self.fornecedor.setObjectName(u"fornecedor")
        self.label_3 = QLabel(self.fornecedor)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(414, 190, 91, 41))
        self.pages.addWidget(self.fornecedor)

        self.verticalLayout_5.addWidget(self.pages)


        self.verticalLayout_4.addWidget(self.frame_5)


        self.horizontalLayout.addWidget(self.body)


        self.verticalLayout.addWidget(self.frame_2)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"JC Vidros", None))
        self.minimize.setText(QCoreApplication.translate("MainWindow", u"-", None))
        self.maximize.setText(QCoreApplication.translate("MainWindow", u"+", None))
        self.close.setText(QCoreApplication.translate("MainWindow", u"X", None))
        self.menu.setText(QCoreApplication.translate("MainWindow", u"Menu", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_cliente.setText(QCoreApplication.translate("MainWindow", u"Cliente", None))
        self.btn_fornecedor.setText(QCoreApplication.translate("MainWindow", u"Fornecedor", None))
        self.btn_agenda.setText(QCoreApplication.translate("MainWindow", u"Agenda", None))
        self.btn_caixa.setText(QCoreApplication.translate("MainWindow", u"Caixa", None))
        self.btn_produtos.setText(QCoreApplication.translate("MainWindow", u"Produtos", None))
        self.btn_os.setText(QCoreApplication.translate("MainWindow", u"OS", None))
        self.settings.setText(QCoreApplication.translate("MainWindow", u"Configura\u00e7oes", None))
        self.help.setText(QCoreApplication.translate("MainWindow", u"Ajuda", None))
        self.about.setText(QCoreApplication.translate("MainWindow", u"Sobre", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pesquisar Cliente", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Novo", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Editar", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Apagar", None))
        self.pushButton_8.setText(QCoreApplication.translate("MainWindow", u"Voltar", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tel1", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tel2", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem5 = self.tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem6 = self.tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Cidade", None));
        ___qtablewidgetitem7 = self.tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem8 = self.tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem9 = self.tableWidget.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem10 = self.tableWidget.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7ao", None));
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Fornecedor", None))
    # retranslateUi

