# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'telaYsIFNM.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1672, 979)
        icon = QIcon()
        icon.addFile(u":/Icons/jc_icon.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.change_pdf = QAction(MainWindow)
        self.change_pdf.setObjectName(u"change_pdf")
        self.actionAlterar_Estilo = QAction(MainWindow)
        self.actionAlterar_Estilo.setObjectName(u"actionAlterar_Estilo")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setMinimumSize(QSize(1300, 700))
        self.centralwidget.setStyleSheet(u"QPushButton{\n"
"border:0\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy)
        self.frame.setMinimumSize(QSize(90, 70))
        self.frame.setSizeIncrement(QSize(0, 0))
        self.frame.setBaseSize(QSize(0, 0))
        font = QFont()
        font.setUnderline(False)
        font.setStyleStrategy(QFont.PreferDefault)
        self.frame.setFont(font)
        self.frame.setStyleSheet(u"QPushButton{\n"
"	text-align:center;\n"
"	color:#fff;\n"
"	border:0px;\n"
"	border-radius:1px;\n"
"	font-size:20px;\n"
"	cursor: pointer;\n"
"	background-color:#538fff;\n"
"padding:2px 5px;\n"
"}\n"
"QPushButton:hover{\n"
"background-color:#3668ff;\n"
"border-left:5px solid red;\n"
"color:white;\n"
"	font: 20pt \"Impact\";\n"
"}")
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.frame.setLineWidth(1)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.client = QPushButton(self.frame)
        self.client.setObjectName(u"client")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Minimum)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.client.sizePolicy().hasHeightForWidth())
        self.client.setSizePolicy(sizePolicy1)
        self.client.setStyleSheet(u"")
        icon1 = QIcon()
        icon1.addFile(u":/Icons/Clientes.png", QSize(), QIcon.Normal, QIcon.Off)
        self.client.setIcon(icon1)
        self.client.setIconSize(QSize(80, 80))

        self.horizontalLayout.addWidget(self.client)

        self.provider = QPushButton(self.frame)
        self.provider.setObjectName(u"provider")
        sizePolicy1.setHeightForWidth(self.provider.sizePolicy().hasHeightForWidth())
        self.provider.setSizePolicy(sizePolicy1)
        icon2 = QIcon()
        icon2.addFile(u":/Icons/Fornecedor.png", QSize(), QIcon.Normal, QIcon.Off)
        self.provider.setIcon(icon2)
        self.provider.setIconSize(QSize(80, 80))

        self.horizontalLayout.addWidget(self.provider)

        self.task = QPushButton(self.frame)
        self.task.setObjectName(u"task")
        sizePolicy1.setHeightForWidth(self.task.sizePolicy().hasHeightForWidth())
        self.task.setSizePolicy(sizePolicy1)
        icon3 = QIcon()
        icon3.addFile(u":/Icons/agenda.png", QSize(), QIcon.Normal, QIcon.Off)
        self.task.setIcon(icon3)
        self.task.setIconSize(QSize(80, 80))

        self.horizontalLayout.addWidget(self.task)

        self.cashier_2 = QPushButton(self.frame)
        self.cashier_2.setObjectName(u"cashier_2")
        sizePolicy1.setHeightForWidth(self.cashier_2.sizePolicy().hasHeightForWidth())
        self.cashier_2.setSizePolicy(sizePolicy1)
        icon4 = QIcon()
        icon4.addFile(u":/Icons/Caixa.png", QSize(), QIcon.Normal, QIcon.Off)
        self.cashier_2.setIcon(icon4)
        self.cashier_2.setIconSize(QSize(80, 80))

        self.horizontalLayout.addWidget(self.cashier_2)

        self.product = QPushButton(self.frame)
        self.product.setObjectName(u"product")
        sizePolicy1.setHeightForWidth(self.product.sizePolicy().hasHeightForWidth())
        self.product.setSizePolicy(sizePolicy1)
        icon5 = QIcon()
        icon5.addFile(u":/Icons/Produtos.png", QSize(), QIcon.Normal, QIcon.Off)
        self.product.setIcon(icon5)
        self.product.setIconSize(QSize(80, 80))

        self.horizontalLayout.addWidget(self.product)

        self.os_2 = QPushButton(self.frame)
        self.os_2.setObjectName(u"os_2")
        sizePolicy1.setHeightForWidth(self.os_2.sizePolicy().hasHeightForWidth())
        self.os_2.setSizePolicy(sizePolicy1)
        icon6 = QIcon()
        icon6.addFile(u":/Icons/Menu_os.png.png", QSize(), QIcon.Normal, QIcon.Off)
        self.os_2.setIcon(icon6)
        self.os_2.setIconSize(QSize(80, 80))

        self.horizontalLayout.addWidget(self.os_2)


        self.verticalLayout.addWidget(self.frame)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(90, 0, 70, 20)
        self.pages = QStackedWidget(self.centralwidget)
        self.pages.setObjectName(u"pages")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.MinimumExpanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.pages.sizePolicy().hasHeightForWidth())
        self.pages.setSizePolicy(sizePolicy2)
        self.central = QWidget()
        self.central.setObjectName(u"central")
        self.pages.addWidget(self.central)
        self.Cliente = QWidget()
        self.Cliente.setObjectName(u"Cliente")
        sizePolicy.setHeightForWidth(self.Cliente.sizePolicy().hasHeightForWidth())
        self.Cliente.setSizePolicy(sizePolicy)
        self.Cliente.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_8 = QHBoxLayout(self.Cliente)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.frame_2 = QFrame(self.Cliente)
        self.frame_2.setObjectName(u"frame_2")
        sizePolicy2.setHeightForWidth(self.frame_2.sizePolicy().hasHeightForWidth())
        self.frame_2.setSizePolicy(sizePolicy2)
        self.frame_2.setMinimumSize(QSize(400, 0))
        self.frame_2.setMaximumSize(QSize(1920, 1080))
        self.frame_2.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(11, 5, -1, -1)
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_7.addItem(self.horizontalSpacer_3)

        self.label = QLabel(self.frame_2)
        self.label.setObjectName(u"label")
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        font1 = QFont()
        font1.setPointSize(9)
        self.label.setFont(font1)

        self.horizontalLayout_7.addWidget(self.label)


        self.verticalLayout_4.addLayout(self.horizontalLayout_7)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setSpacing(10)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(-1, 0, -1, 0)
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_2)

        self.search_client = QLineEdit(self.frame_2)
        self.search_client.setObjectName(u"search_client")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.search_client.sizePolicy().hasHeightForWidth())
        self.search_client.setSizePolicy(sizePolicy3)
        self.search_client.setMinimumSize(QSize(300, 0))
        font2 = QFont()
        font2.setPointSize(10)
        self.search_client.setFont(font2)

        self.horizontalLayout_3.addWidget(self.search_client)

        self.horizontalSpacer = QSpacerItem(400, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setSpacing(50)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.new_client = QPushButton(self.frame_2)
        self.new_client.setObjectName(u"new_client")
        sizePolicy.setHeightForWidth(self.new_client.sizePolicy().hasHeightForWidth())
        self.new_client.setSizePolicy(sizePolicy)
        self.new_client.setMinimumSize(QSize(0, 0))
        icon7 = QIcon()
        icon7.addFile(u":/Icons/add_cliente.png", QSize(), QIcon.Normal, QIcon.Off)
        self.new_client.setIcon(icon7)
        self.new_client.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.new_client)

        self.edit_client = QPushButton(self.frame_2)
        self.edit_client.setObjectName(u"edit_client")
        sizePolicy.setHeightForWidth(self.edit_client.sizePolicy().hasHeightForWidth())
        self.edit_client.setSizePolicy(sizePolicy)
        icon8 = QIcon()
        icon8.addFile(u":/Icons/editar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.edit_client.setIcon(icon8)
        self.edit_client.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.edit_client)

        self.delete_client = QPushButton(self.frame_2)
        self.delete_client.setObjectName(u"delete_client")
        sizePolicy4 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.delete_client.sizePolicy().hasHeightForWidth())
        self.delete_client.setSizePolicy(sizePolicy4)
        icon9 = QIcon()
        icon9.addFile(u":/Icons/Limpar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_client.setIcon(icon9)
        self.delete_client.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.delete_client)

        self.back_1 = QPushButton(self.frame_2)
        self.back_1.setObjectName(u"back_1")
        icon10 = QIcon()
        icon10.addFile(u":/Icons/back.png", QSize(), QIcon.Normal, QIcon.Off)
        self.back_1.setIcon(icon10)
        self.back_1.setIconSize(QSize(32, 32))

        self.horizontalLayout_4.addWidget(self.back_1)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(70, 10, 50, 30)
        self.table_Cliente = QTableWidget(self.frame_2)
        if (self.table_Cliente.columnCount() < 11):
            self.table_Cliente.setColumnCount(11)
        __qtablewidgetitem = QTableWidgetItem()
        self.table_Cliente.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.table_Cliente.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.table_Cliente.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.table_Cliente.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.table_Cliente.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.table_Cliente.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.table_Cliente.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.table_Cliente.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.table_Cliente.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.table_Cliente.setHorizontalHeaderItem(9, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.table_Cliente.setHorizontalHeaderItem(10, __qtablewidgetitem10)
        self.table_Cliente.setObjectName(u"table_Cliente")
        sizePolicy2.setHeightForWidth(self.table_Cliente.sizePolicy().hasHeightForWidth())
        self.table_Cliente.setSizePolicy(sizePolicy2)
        font3 = QFont()
        font3.setPointSize(8)
        self.table_Cliente.setFont(font3)
        self.table_Cliente.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_Cliente.setColumnCount(11)
        self.table_Cliente.horizontalHeader().setCascadingSectionResizes(False)
        self.table_Cliente.horizontalHeader().setMinimumSectionSize(195)
        self.table_Cliente.horizontalHeader().setDefaultSectionSize(230)
        self.table_Cliente.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_Cliente.horizontalHeader().setStretchLastSection(True)
        self.table_Cliente.verticalHeader().setVisible(False)

        self.verticalLayout_3.addWidget(self.table_Cliente)


        self.verticalLayout_4.addLayout(self.verticalLayout_3)


        self.horizontalLayout_8.addWidget(self.frame_2)

        self.pages.addWidget(self.Cliente)
        self.fornecedor = QWidget()
        self.fornecedor.setObjectName(u"fornecedor")
        self.horizontalLayout_12 = QHBoxLayout(self.fornecedor)
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.horizontalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.frame_3 = QFrame(self.fornecedor)
        self.frame_3.setObjectName(u"frame_3")
        sizePolicy2.setHeightForWidth(self.frame_3.sizePolicy().hasHeightForWidth())
        self.frame_3.setSizePolicy(sizePolicy2)
        self.frame_3.setMaximumSize(QSize(1920, 1080))
        self.frame_3.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_3)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_5.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_4)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        sizePolicy.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy)
        self.label_2.setFont(font1)

        self.horizontalLayout_9.addWidget(self.label_2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(10)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, 22)
        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)

        self.search_provider = QLineEdit(self.frame_3)
        self.search_provider.setObjectName(u"search_provider")
        sizePolicy3.setHeightForWidth(self.search_provider.sizePolicy().hasHeightForWidth())
        self.search_provider.setSizePolicy(sizePolicy3)
        self.search_provider.setMinimumSize(QSize(300, 0))
        self.search_provider.setFont(font2)

        self.horizontalLayout_10.addWidget(self.search_provider)

        self.horizontalSpacer_6 = QSpacerItem(400, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_6)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(50)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.new_provider = QPushButton(self.frame_3)
        self.new_provider.setObjectName(u"new_provider")
        sizePolicy5 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.new_provider.sizePolicy().hasHeightForWidth())
        self.new_provider.setSizePolicy(sizePolicy5)
        self.new_provider.setIcon(icon7)
        self.new_provider.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.new_provider)

        self.edit_provider = QPushButton(self.frame_3)
        self.edit_provider.setObjectName(u"edit_provider")
        sizePolicy5.setHeightForWidth(self.edit_provider.sizePolicy().hasHeightForWidth())
        self.edit_provider.setSizePolicy(sizePolicy5)
        self.edit_provider.setIcon(icon8)
        self.edit_provider.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.edit_provider)

        self.delete_provider = QPushButton(self.frame_3)
        self.delete_provider.setObjectName(u"delete_provider")
        self.delete_provider.setIcon(icon9)
        self.delete_provider.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.delete_provider)

        self.back_3 = QPushButton(self.frame_3)
        self.back_3.setObjectName(u"back_3")
        self.back_3.setIcon(icon10)
        self.back_3.setIconSize(QSize(32, 32))

        self.horizontalLayout_11.addWidget(self.back_3)


        self.horizontalLayout_10.addLayout(self.horizontalLayout_11)


        self.verticalLayout_5.addLayout(self.horizontalLayout_10)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(70, 0, 70, 50)
        self.table_fornecedor = QTableWidget(self.frame_3)
        if (self.table_fornecedor.columnCount() < 8):
            self.table_fornecedor.setColumnCount(8)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.table_fornecedor.setHorizontalHeaderItem(0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.table_fornecedor.setHorizontalHeaderItem(1, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.table_fornecedor.setHorizontalHeaderItem(2, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.table_fornecedor.setHorizontalHeaderItem(3, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.table_fornecedor.setHorizontalHeaderItem(4, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.table_fornecedor.setHorizontalHeaderItem(5, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.table_fornecedor.setHorizontalHeaderItem(6, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.table_fornecedor.setHorizontalHeaderItem(7, __qtablewidgetitem18)
        self.table_fornecedor.setObjectName(u"table_fornecedor")
        sizePolicy2.setHeightForWidth(self.table_fornecedor.sizePolicy().hasHeightForWidth())
        self.table_fornecedor.setSizePolicy(sizePolicy2)
        font4 = QFont()
        font4.setPointSize(12)
        self.table_fornecedor.setFont(font4)
        self.table_fornecedor.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_fornecedor.setColumnCount(8)
        self.table_fornecedor.horizontalHeader().setMinimumSectionSize(210)
        self.table_fornecedor.horizontalHeader().setDefaultSectionSize(210)
        self.table_fornecedor.verticalHeader().setVisible(False)
        self.table_fornecedor.verticalHeader().setDefaultSectionSize(31)

        self.verticalLayout_6.addWidget(self.table_fornecedor)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)


        self.horizontalLayout_12.addWidget(self.frame_3)

        self.pages.addWidget(self.fornecedor)
        self.agenda = QWidget()
        self.agenda.setObjectName(u"agenda")
        self.horizontalLayout_20 = QHBoxLayout(self.agenda)
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.horizontalLayout_20.setContentsMargins(0, 0, 0, 0)
        self.frame_5 = QFrame(self.agenda)
        self.frame_5.setObjectName(u"frame_5")
        sizePolicy2.setHeightForWidth(self.frame_5.sizePolicy().hasHeightForWidth())
        self.frame_5.setSizePolicy(sizePolicy2)
        self.frame_5.setMaximumSize(QSize(1920, 1080))
        self.frame_5.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.frame_5.setFrameShape(QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_5)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_9.setContentsMargins(11, 5, 11, 11)
        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalSpacer_10 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_17.addItem(self.horizontalSpacer_10)

        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setFont(font1)

        self.horizontalLayout_17.addWidget(self.label_4)


        self.verticalLayout_9.addLayout(self.horizontalLayout_17)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setSpacing(10)
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.horizontalLayout_18.setContentsMargins(-1, 0, -1, 22)
        self.horizontalSpacer_11 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_11)

        self.search_task = QLineEdit(self.frame_5)
        self.search_task.setObjectName(u"search_task")
        sizePolicy3.setHeightForWidth(self.search_task.sizePolicy().hasHeightForWidth())
        self.search_task.setSizePolicy(sizePolicy3)
        self.search_task.setMinimumSize(QSize(300, 0))
        self.search_task.setFont(font2)

        self.horizontalLayout_18.addWidget(self.search_task)

        self.horizontalSpacer_12 = QSpacerItem(400, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_18.addItem(self.horizontalSpacer_12)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setSpacing(50)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.new_task = QPushButton(self.frame_5)
        self.new_task.setObjectName(u"new_task")
        sizePolicy5.setHeightForWidth(self.new_task.sizePolicy().hasHeightForWidth())
        self.new_task.setSizePolicy(sizePolicy5)
        self.new_task.setIcon(icon7)
        self.new_task.setIconSize(QSize(32, 32))

        self.horizontalLayout_19.addWidget(self.new_task)

        self.edit_task = QPushButton(self.frame_5)
        self.edit_task.setObjectName(u"edit_task")
        sizePolicy5.setHeightForWidth(self.edit_task.sizePolicy().hasHeightForWidth())
        self.edit_task.setSizePolicy(sizePolicy5)
        self.edit_task.setIcon(icon8)
        self.edit_task.setIconSize(QSize(32, 32))

        self.horizontalLayout_19.addWidget(self.edit_task)

        self.delete_task = QPushButton(self.frame_5)
        self.delete_task.setObjectName(u"delete_task")
        self.delete_task.setIcon(icon9)
        self.delete_task.setIconSize(QSize(32, 32))

        self.horizontalLayout_19.addWidget(self.delete_task)

        self.back_6 = QPushButton(self.frame_5)
        self.back_6.setObjectName(u"back_6")
        self.back_6.setIcon(icon10)
        self.back_6.setIconSize(QSize(32, 32))

        self.horizontalLayout_19.addWidget(self.back_6)


        self.horizontalLayout_18.addLayout(self.horizontalLayout_19)


        self.verticalLayout_9.addLayout(self.horizontalLayout_18)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.verticalLayout_10.setContentsMargins(70, 0, 70, 50)
        self.table_agenda = QTableWidget(self.frame_5)
        if (self.table_agenda.columnCount() < 10):
            self.table_agenda.setColumnCount(10)
        __qtablewidgetitem19 = QTableWidgetItem()
        self.table_agenda.setHorizontalHeaderItem(0, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        self.table_agenda.setHorizontalHeaderItem(1, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.table_agenda.setHorizontalHeaderItem(2, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.table_agenda.setHorizontalHeaderItem(3, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.table_agenda.setHorizontalHeaderItem(4, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.table_agenda.setHorizontalHeaderItem(5, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.table_agenda.setHorizontalHeaderItem(6, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        self.table_agenda.setHorizontalHeaderItem(7, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        self.table_agenda.setHorizontalHeaderItem(8, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.table_agenda.setHorizontalHeaderItem(9, __qtablewidgetitem28)
        self.table_agenda.setObjectName(u"table_agenda")
        sizePolicy2.setHeightForWidth(self.table_agenda.sizePolicy().hasHeightForWidth())
        self.table_agenda.setSizePolicy(sizePolicy2)
        self.table_agenda.setFont(font4)
        self.table_agenda.setAutoScrollMargin(16)
        self.table_agenda.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_agenda.setColumnCount(10)
        self.table_agenda.horizontalHeader().setMinimumSectionSize(190)
        self.table_agenda.horizontalHeader().setDefaultSectionSize(190)
        self.table_agenda.horizontalHeader().setStretchLastSection(True)
        self.table_agenda.verticalHeader().setVisible(False)
        self.table_agenda.verticalHeader().setDefaultSectionSize(31)

        self.verticalLayout_10.addWidget(self.table_agenda)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)


        self.horizontalLayout_20.addWidget(self.frame_5)

        self.pages.addWidget(self.agenda)
        self.caixa = QWidget()
        self.caixa.setObjectName(u"caixa")
        self.horizontalLayout_23 = QHBoxLayout(self.caixa)
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.horizontalLayout_23.setContentsMargins(0, 0, 0, 0)
        self.frame_11 = QFrame(self.caixa)
        self.frame_11.setObjectName(u"frame_11")
        sizePolicy2.setHeightForWidth(self.frame_11.sizePolicy().hasHeightForWidth())
        self.frame_11.setSizePolicy(sizePolicy2)
        self.frame_11.setMaximumSize(QSize(1920, 1080))
        self.frame_11.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.frame_11.setFrameShape(QFrame.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_11)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(-1, 5, -1, -1)
        self.tabWidget = QTabWidget(self.frame_11)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(1357, 0))
        self.tabWidget.setFont(font1)
        self.tabWidget.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.gridLayout = QGridLayout(self.tab)
        self.gridLayout.setObjectName(u"gridLayout")
        self.saldo = QLineEdit(self.tab)
        self.saldo.setObjectName(u"saldo")
        sizePolicy6 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Preferred)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.saldo.sizePolicy().hasHeightForWidth())
        self.saldo.setSizePolicy(sizePolicy6)
        self.saldo.setMinimumSize(QSize(0, 50))
        self.saldo.setFont(font2)
        self.saldo.setReadOnly(True)

        self.gridLayout.addWidget(self.saldo, 4, 3, 1, 1)

        self.search_cashier = QLineEdit(self.tab)
        self.search_cashier.setObjectName(u"search_cashier")
        sizePolicy6.setHeightForWidth(self.search_cashier.sizePolicy().hasHeightForWidth())
        self.search_cashier.setSizePolicy(sizePolicy6)
        self.search_cashier.setFont(font2)
        self.search_cashier.setStyleSheet(u"")

        self.gridLayout.addWidget(self.search_cashier, 1, 0, 1, 2)

        self.horizontalSpacer_13 = QSpacerItem(700, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_13, 0, 1, 1, 1)

        self.horizontalSpacer_14 = QSpacerItem(600, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout.addItem(self.horizontalSpacer_14, 4, 2, 1, 1)

        self.label_49 = QLabel(self.tab)
        self.label_49.setObjectName(u"label_49")

        self.gridLayout.addWidget(self.label_49, 0, 0, 1, 1)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setSpacing(0)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.new_cashier = QPushButton(self.tab)
        self.new_cashier.setObjectName(u"new_cashier")
        sizePolicy7 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Maximum)
        sizePolicy7.setHorizontalStretch(0)
        sizePolicy7.setVerticalStretch(0)
        sizePolicy7.setHeightForWidth(self.new_cashier.sizePolicy().hasHeightForWidth())
        self.new_cashier.setSizePolicy(sizePolicy7)
        self.new_cashier.setIcon(icon7)
        self.new_cashier.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.new_cashier)

        self.edit_cashier = QPushButton(self.tab)
        self.edit_cashier.setObjectName(u"edit_cashier")
        sizePolicy7.setHeightForWidth(self.edit_cashier.sizePolicy().hasHeightForWidth())
        self.edit_cashier.setSizePolicy(sizePolicy7)
        self.edit_cashier.setIcon(icon8)
        self.edit_cashier.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.edit_cashier)

        self.delete_cashier = QPushButton(self.tab)
        self.delete_cashier.setObjectName(u"delete_cashier")
        sizePolicy7.setHeightForWidth(self.delete_cashier.sizePolicy().hasHeightForWidth())
        self.delete_cashier.setSizePolicy(sizePolicy7)
        icon11 = QIcon()
        icon11.addFile(u":/Icons/apagar.png", QSize(), QIcon.Normal, QIcon.Off)
        self.delete_cashier.setIcon(icon11)
        self.delete_cashier.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.delete_cashier)

        self.print_cashier = QPushButton(self.tab)
        self.print_cashier.setObjectName(u"print_cashier")
        sizePolicy7.setHeightForWidth(self.print_cashier.sizePolicy().hasHeightForWidth())
        self.print_cashier.setSizePolicy(sizePolicy7)
        icon12 = QIcon()
        icon12.addFile(u":/Icons/imprimir.png", QSize(), QIcon.Normal, QIcon.Off)
        self.print_cashier.setIcon(icon12)
        self.print_cashier.setIconSize(QSize(32, 32))

        self.horizontalLayout_21.addWidget(self.print_cashier)


        self.gridLayout.addLayout(self.horizontalLayout_21, 3, 0, 2, 2)

        self.table_caixa = QTableWidget(self.tab)
        if (self.table_caixa.columnCount() < 6):
            self.table_caixa.setColumnCount(6)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.table_caixa.setHorizontalHeaderItem(0, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.table_caixa.setHorizontalHeaderItem(1, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.table_caixa.setHorizontalHeaderItem(2, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.table_caixa.setHorizontalHeaderItem(3, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        self.table_caixa.setHorizontalHeaderItem(4, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        self.table_caixa.setHorizontalHeaderItem(5, __qtablewidgetitem34)
        self.table_caixa.setObjectName(u"table_caixa")
        sizePolicy8 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.MinimumExpanding)
        sizePolicy8.setHorizontalStretch(0)
        sizePolicy8.setVerticalStretch(0)
        sizePolicy8.setHeightForWidth(self.table_caixa.sizePolicy().hasHeightForWidth())
        self.table_caixa.setSizePolicy(sizePolicy8)
        self.table_caixa.setSizeIncrement(QSize(700, 0))
        self.table_caixa.setFont(font4)
        self.table_caixa.setStyleSheet(u"")
        self.table_caixa.setFrameShape(QFrame.StyledPanel)
        self.table_caixa.setLineWidth(0)
        self.table_caixa.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_caixa.setTabKeyNavigation(False)
        self.table_caixa.setShowGrid(True)
        self.table_caixa.setGridStyle(Qt.SolidLine)
        self.table_caixa.setSortingEnabled(False)
        self.table_caixa.setWordWrap(True)
        self.table_caixa.horizontalHeader().setVisible(False)
        self.table_caixa.horizontalHeader().setCascadingSectionResizes(False)
        self.table_caixa.horizontalHeader().setMinimumSectionSize(280)
        self.table_caixa.horizontalHeader().setDefaultSectionSize(280)
        self.table_caixa.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_caixa.horizontalHeader().setStretchLastSection(True)
        self.table_caixa.verticalHeader().setVisible(False)
        self.table_caixa.verticalHeader().setCascadingSectionResizes(False)
        self.table_caixa.verticalHeader().setMinimumSectionSize(18)
        self.table_caixa.verticalHeader().setDefaultSectionSize(23)
        self.table_caixa.verticalHeader().setHighlightSections(False)
        self.table_caixa.verticalHeader().setProperty("showSortIndicator", False)
        self.table_caixa.verticalHeader().setStretchLastSection(False)

        self.gridLayout.addWidget(self.table_caixa, 2, 0, 1, 4)

        self.label_52 = QLabel(self.tab)
        self.label_52.setObjectName(u"label_52")
        self.label_52.setFont(font2)

        self.gridLayout.addWidget(self.label_52, 3, 3, 1, 1)

        self.back_8 = QPushButton(self.tab)
        self.back_8.setObjectName(u"back_8")
        sizePolicy9 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Maximum)
        sizePolicy9.setHorizontalStretch(0)
        sizePolicy9.setVerticalStretch(0)
        sizePolicy9.setHeightForWidth(self.back_8.sizePolicy().hasHeightForWidth())
        self.back_8.setSizePolicy(sizePolicy9)
        self.back_8.setIcon(icon10)
        self.back_8.setIconSize(QSize(32, 32))

        self.gridLayout.addWidget(self.back_8, 0, 3, 1, 1)

        self.tabWidget.addTab(self.tab, "")

        self.verticalLayout_11.addWidget(self.tabWidget)


        self.horizontalLayout_23.addWidget(self.frame_11)

        self.pages.addWidget(self.caixa)
        self.produto = QWidget()
        self.produto.setObjectName(u"produto")
        self.horizontalLayout_28 = QHBoxLayout(self.produto)
        self.horizontalLayout_28.setObjectName(u"horizontalLayout_28")
        self.horizontalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.frame_6 = QFrame(self.produto)
        self.frame_6.setObjectName(u"frame_6")
        sizePolicy2.setHeightForWidth(self.frame_6.sizePolicy().hasHeightForWidth())
        self.frame_6.setSizePolicy(sizePolicy2)
        self.frame_6.setMaximumSize(QSize(1920, 1080))
        self.frame_6.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.frame_6.setFrameShape(QFrame.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Raised)
        self.verticalLayout_12 = QVBoxLayout(self.frame_6)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalSpacer_15 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_25.addItem(self.horizontalSpacer_15)

        self.label_5 = QLabel(self.frame_6)
        self.label_5.setObjectName(u"label_5")
        sizePolicy.setHeightForWidth(self.label_5.sizePolicy().hasHeightForWidth())
        self.label_5.setSizePolicy(sizePolicy)
        self.label_5.setFont(font1)

        self.horizontalLayout_25.addWidget(self.label_5)


        self.verticalLayout_12.addLayout(self.horizontalLayout_25)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setSpacing(10)
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalLayout_26.setContentsMargins(-1, 0, -1, 22)
        self.horizontalSpacer_16 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_16)

        self.search_product = QLineEdit(self.frame_6)
        self.search_product.setObjectName(u"search_product")
        sizePolicy3.setHeightForWidth(self.search_product.sizePolicy().hasHeightForWidth())
        self.search_product.setSizePolicy(sizePolicy3)
        self.search_product.setMinimumSize(QSize(300, 0))
        self.search_product.setFont(font2)

        self.horizontalLayout_26.addWidget(self.search_product)

        self.horizontalSpacer_17 = QSpacerItem(400, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_17)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setSpacing(50)
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.new_product = QPushButton(self.frame_6)
        self.new_product.setObjectName(u"new_product")
        sizePolicy.setHeightForWidth(self.new_product.sizePolicy().hasHeightForWidth())
        self.new_product.setSizePolicy(sizePolicy)
        self.new_product.setMinimumSize(QSize(0, 0))
        self.new_product.setIcon(icon7)
        self.new_product.setIconSize(QSize(32, 32))

        self.horizontalLayout_27.addWidget(self.new_product)

        self.edit_product = QPushButton(self.frame_6)
        self.edit_product.setObjectName(u"edit_product")
        sizePolicy.setHeightForWidth(self.edit_product.sizePolicy().hasHeightForWidth())
        self.edit_product.setSizePolicy(sizePolicy)
        self.edit_product.setIcon(icon8)
        self.edit_product.setIconSize(QSize(32, 32))

        self.horizontalLayout_27.addWidget(self.edit_product)

        self.delete_product = QPushButton(self.frame_6)
        self.delete_product.setObjectName(u"delete_product")
        sizePolicy4.setHeightForWidth(self.delete_product.sizePolicy().hasHeightForWidth())
        self.delete_product.setSizePolicy(sizePolicy4)
        self.delete_product.setIcon(icon9)
        self.delete_product.setIconSize(QSize(32, 32))

        self.horizontalLayout_27.addWidget(self.delete_product)

        self.back_10 = QPushButton(self.frame_6)
        self.back_10.setObjectName(u"back_10")
        self.back_10.setIcon(icon10)
        self.back_10.setIconSize(QSize(32, 32))

        self.horizontalLayout_27.addWidget(self.back_10)


        self.horizontalLayout_26.addLayout(self.horizontalLayout_27)


        self.verticalLayout_12.addLayout(self.horizontalLayout_26)

        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(60, 0, 60, 30)
        self.table_produto = QTableWidget(self.frame_6)
        if (self.table_produto.columnCount() < 8):
            self.table_produto.setColumnCount(8)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.table_produto.setHorizontalHeaderItem(0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.table_produto.setHorizontalHeaderItem(1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.table_produto.setHorizontalHeaderItem(2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.table_produto.setHorizontalHeaderItem(3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.table_produto.setHorizontalHeaderItem(4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        self.table_produto.setHorizontalHeaderItem(5, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        self.table_produto.setHorizontalHeaderItem(6, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.table_produto.setHorizontalHeaderItem(7, __qtablewidgetitem42)
        self.table_produto.setObjectName(u"table_produto")
        sizePolicy2.setHeightForWidth(self.table_produto.sizePolicy().hasHeightForWidth())
        self.table_produto.setSizePolicy(sizePolicy2)
        self.table_produto.setFont(font4)
        self.table_produto.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_produto.setColumnCount(8)
        self.table_produto.horizontalHeader().setCascadingSectionResizes(False)
        self.table_produto.horizontalHeader().setMinimumSectionSize(290)
        self.table_produto.horizontalHeader().setDefaultSectionSize(290)
        self.table_produto.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_produto.horizontalHeader().setStretchLastSection(True)
        self.table_produto.verticalHeader().setVisible(False)

        self.verticalLayout_13.addWidget(self.table_produto)


        self.verticalLayout_12.addLayout(self.verticalLayout_13)


        self.horizontalLayout_28.addWidget(self.frame_6)

        self.pages.addWidget(self.produto)
        self.os = QWidget()
        self.os.setObjectName(u"os")
        self.horizontalLayout_32 = QHBoxLayout(self.os)
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.horizontalLayout_32.setContentsMargins(0, 0, 0, 0)
        self.frame_7 = QFrame(self.os)
        self.frame_7.setObjectName(u"frame_7")
        sizePolicy2.setHeightForWidth(self.frame_7.sizePolicy().hasHeightForWidth())
        self.frame_7.setSizePolicy(sizePolicy2)
        self.frame_7.setMaximumSize(QSize(1920, 1080))
        self.frame_7.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.frame_7.setFrameShape(QFrame.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Raised)
        self.verticalLayout_14 = QVBoxLayout(self.frame_7)
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.verticalLayout_14.setContentsMargins(-1, 5, -1, -1)
        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.horizontalSpacer_18 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_29.addItem(self.horizontalSpacer_18)

        self.label_6 = QLabel(self.frame_7)
        self.label_6.setObjectName(u"label_6")
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setFont(font1)

        self.horizontalLayout_29.addWidget(self.label_6)


        self.verticalLayout_14.addLayout(self.horizontalLayout_29)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setSpacing(10)
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.horizontalLayout_30.setContentsMargins(-1, 0, -1, 22)
        self.horizontalSpacer_19 = QSpacerItem(40, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_19)

        self.search_os = QLineEdit(self.frame_7)
        self.search_os.setObjectName(u"search_os")
        sizePolicy3.setHeightForWidth(self.search_os.sizePolicy().hasHeightForWidth())
        self.search_os.setSizePolicy(sizePolicy3)
        self.search_os.setMinimumSize(QSize(300, 0))
        self.search_os.setFont(font2)

        self.horizontalLayout_30.addWidget(self.search_os)

        self.horizontalSpacer_20 = QSpacerItem(400, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_30.addItem(self.horizontalSpacer_20)

        self.horizontalLayout_31 = QHBoxLayout()
        self.horizontalLayout_31.setSpacing(50)
        self.horizontalLayout_31.setObjectName(u"horizontalLayout_31")
        self.new_os = QPushButton(self.frame_7)
        self.new_os.setObjectName(u"new_os")
        sizePolicy.setHeightForWidth(self.new_os.sizePolicy().hasHeightForWidth())
        self.new_os.setSizePolicy(sizePolicy)
        self.new_os.setMinimumSize(QSize(0, 0))
        self.new_os.setIcon(icon7)
        self.new_os.setIconSize(QSize(32, 32))

        self.horizontalLayout_31.addWidget(self.new_os)

        self.edit_os = QPushButton(self.frame_7)
        self.edit_os.setObjectName(u"edit_os")
        sizePolicy.setHeightForWidth(self.edit_os.sizePolicy().hasHeightForWidth())
        self.edit_os.setSizePolicy(sizePolicy)
        self.edit_os.setIcon(icon8)
        self.edit_os.setIconSize(QSize(32, 32))

        self.horizontalLayout_31.addWidget(self.edit_os)

        self.delete_os = QPushButton(self.frame_7)
        self.delete_os.setObjectName(u"delete_os")
        sizePolicy4.setHeightForWidth(self.delete_os.sizePolicy().hasHeightForWidth())
        self.delete_os.setSizePolicy(sizePolicy4)
        self.delete_os.setIcon(icon9)
        self.delete_os.setIconSize(QSize(32, 32))

        self.horizontalLayout_31.addWidget(self.delete_os)

        self.print_os = QPushButton(self.frame_7)
        self.print_os.setObjectName(u"print_os")
        self.print_os.setIcon(icon12)
        self.print_os.setIconSize(QSize(32, 32))

        self.horizontalLayout_31.addWidget(self.print_os)

        self.back_12 = QPushButton(self.frame_7)
        self.back_12.setObjectName(u"back_12")
        self.back_12.setIcon(icon10)
        self.back_12.setIconSize(QSize(32, 32))

        self.horizontalLayout_31.addWidget(self.back_12)


        self.horizontalLayout_30.addLayout(self.horizontalLayout_31)


        self.verticalLayout_14.addLayout(self.horizontalLayout_30)

        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_15.setContentsMargins(70, 0, 70, 30)
        self.table_os = QTableWidget(self.frame_7)
        self.table_os.setObjectName(u"table_os")
        sizePolicy2.setHeightForWidth(self.table_os.sizePolicy().hasHeightForWidth())
        self.table_os.setSizePolicy(sizePolicy2)
        self.table_os.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table_os.setColumnCount(0)
        self.table_os.horizontalHeader().setCascadingSectionResizes(False)
        self.table_os.horizontalHeader().setMinimumSectionSize(195)
        self.table_os.horizontalHeader().setDefaultSectionSize(195)
        self.table_os.horizontalHeader().setProperty("showSortIndicator", False)
        self.table_os.horizontalHeader().setStretchLastSection(False)

        self.verticalLayout_15.addWidget(self.table_os)


        self.verticalLayout_14.addLayout(self.verticalLayout_15)


        self.horizontalLayout_32.addWidget(self.frame_7)

        self.pages.addWidget(self.os)
        self.add_client = QWidget()
        self.add_client.setObjectName(u"add_client")
        self.add_client.setMinimumSize(QSize(0, 0))
        self.horizontalLayout_33 = QHBoxLayout(self.add_client)
        self.horizontalLayout_33.setSpacing(0)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_33.setContentsMargins(0, 0, 0, 0)
        self.frame_8 = QFrame(self.add_client)
        self.frame_8.setObjectName(u"frame_8")
        sizePolicy7.setHeightForWidth(self.frame_8.sizePolicy().hasHeightForWidth())
        self.frame_8.setSizePolicy(sizePolicy7)
        self.frame_8.setMinimumSize(QSize(800, 600))
        self.frame_8.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.frame_8.setFrameShape(QFrame.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Raised)
        self.layoutWidget_4 = QWidget(self.frame_8)
        self.layoutWidget_4.setObjectName(u"layoutWidget_4")
        self.layoutWidget_4.setGeometry(QRect(10, 10, 613, 477))
        self.verticalLayout_16 = QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.verticalLayout_16.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.label_54 = QLabel(self.layoutWidget_4)
        self.label_54.setObjectName(u"label_54")
        sizePolicy9.setHeightForWidth(self.label_54.sizePolicy().hasHeightForWidth())
        self.label_54.setSizePolicy(sizePolicy9)
        self.label_54.setFont(font2)

        self.verticalLayout_17.addWidget(self.label_54)

        self.nm_cliente = QLineEdit(self.layoutWidget_4)
        self.nm_cliente.setObjectName(u"nm_cliente")
        sizePolicy10 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy10.setHorizontalStretch(0)
        sizePolicy10.setVerticalStretch(0)
        sizePolicy10.setHeightForWidth(self.nm_cliente.sizePolicy().hasHeightForWidth())
        self.nm_cliente.setSizePolicy(sizePolicy10)
        self.nm_cliente.setMinimumSize(QSize(400, 30))
        self.nm_cliente.setFont(font2)

        self.verticalLayout_17.addWidget(self.nm_cliente)


        self.verticalLayout_16.addLayout(self.verticalLayout_17)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.label_57 = QLabel(self.layoutWidget_4)
        self.label_57.setObjectName(u"label_57")
        self.label_57.setFont(font2)

        self.horizontalLayout_34.addWidget(self.label_57)

        self.label_56 = QLabel(self.layoutWidget_4)
        self.label_56.setObjectName(u"label_56")
        sizePolicy.setHeightForWidth(self.label_56.sizePolicy().hasHeightForWidth())
        self.label_56.setSizePolicy(sizePolicy)
        self.label_56.setFont(font2)

        self.horizontalLayout_34.addWidget(self.label_56)


        self.verticalLayout_19.addLayout(self.horizontalLayout_34)

        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.tel1 = QLineEdit(self.layoutWidget_4)
        self.tel1.setObjectName(u"tel1")
        sizePolicy5.setHeightForWidth(self.tel1.sizePolicy().hasHeightForWidth())
        self.tel1.setSizePolicy(sizePolicy5)
        self.tel1.setMinimumSize(QSize(200, 30))
        self.tel1.setFont(font2)

        self.horizontalLayout_36.addWidget(self.tel1)

        self.tel2 = QLineEdit(self.layoutWidget_4)
        self.tel2.setObjectName(u"tel2")
        sizePolicy5.setHeightForWidth(self.tel2.sizePolicy().hasHeightForWidth())
        self.tel2.setSizePolicy(sizePolicy5)
        self.tel2.setMinimumSize(QSize(200, 30))
        self.tel2.setFont(font2)

        self.horizontalLayout_36.addWidget(self.tel2)


        self.verticalLayout_19.addLayout(self.horizontalLayout_36)


        self.verticalLayout_16.addLayout(self.verticalLayout_19)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.label_55 = QLabel(self.layoutWidget_4)
        self.label_55.setObjectName(u"label_55")
        sizePolicy9.setHeightForWidth(self.label_55.sizePolicy().hasHeightForWidth())
        self.label_55.setSizePolicy(sizePolicy9)
        self.label_55.setFont(font2)

        self.verticalLayout_18.addWidget(self.label_55)

        self.end = QLineEdit(self.layoutWidget_4)
        self.end.setObjectName(u"end")
        sizePolicy10.setHeightForWidth(self.end.sizePolicy().hasHeightForWidth())
        self.end.setSizePolicy(sizePolicy10)
        self.end.setMinimumSize(QSize(400, 30))
        self.end.setFont(font2)

        self.verticalLayout_18.addWidget(self.end)


        self.verticalLayout_16.addLayout(self.verticalLayout_18)

        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.horizontalLayout_54 = QHBoxLayout()
        self.horizontalLayout_54.setObjectName(u"horizontalLayout_54")
        self.label_65 = QLabel(self.layoutWidget_4)
        self.label_65.setObjectName(u"label_65")
        sizePolicy.setHeightForWidth(self.label_65.sizePolicy().hasHeightForWidth())
        self.label_65.setSizePolicy(sizePolicy)
        self.label_65.setFont(font2)

        self.horizontalLayout_54.addWidget(self.label_65)

        self.label_63 = QLabel(self.layoutWidget_4)
        self.label_63.setObjectName(u"label_63")
        sizePolicy.setHeightForWidth(self.label_63.sizePolicy().hasHeightForWidth())
        self.label_63.setSizePolicy(sizePolicy)
        self.label_63.setFont(font2)

        self.horizontalLayout_54.addWidget(self.label_63)


        self.verticalLayout_55.addLayout(self.horizontalLayout_54)

        self.horizontalLayout_55 = QHBoxLayout()
        self.horizontalLayout_55.setObjectName(u"horizontalLayout_55")
        self.cdd = QLineEdit(self.layoutWidget_4)
        self.cdd.setObjectName(u"cdd")
        sizePolicy11 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy11.setHorizontalStretch(0)
        sizePolicy11.setVerticalStretch(0)
        sizePolicy11.setHeightForWidth(self.cdd.sizePolicy().hasHeightForWidth())
        self.cdd.setSizePolicy(sizePolicy11)
        self.cdd.setMinimumSize(QSize(300, 30))
        self.cdd.setFont(font2)

        self.horizontalLayout_55.addWidget(self.cdd)

        self.brr = QLineEdit(self.layoutWidget_4)
        self.brr.setObjectName(u"brr")
        sizePolicy11.setHeightForWidth(self.brr.sizePolicy().hasHeightForWidth())
        self.brr.setSizePolicy(sizePolicy11)
        self.brr.setMinimumSize(QSize(300, 30))
        self.brr.setFont(font2)

        self.horizontalLayout_55.addWidget(self.brr)


        self.verticalLayout_55.addLayout(self.horizontalLayout_55)


        self.verticalLayout_16.addLayout(self.verticalLayout_55)

        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.horizontalLayout_52 = QHBoxLayout()
        self.horizontalLayout_52.setObjectName(u"horizontalLayout_52")
        self.label_58 = QLabel(self.layoutWidget_4)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font2)

        self.horizontalLayout_52.addWidget(self.label_58)

        self.label_62 = QLabel(self.layoutWidget_4)
        self.label_62.setObjectName(u"label_62")
        self.label_62.setFont(font2)

        self.horizontalLayout_52.addWidget(self.label_62)


        self.verticalLayout_20.addLayout(self.horizontalLayout_52)

        self.horizontalLayout_53 = QHBoxLayout()
        self.horizontalLayout_53.setObjectName(u"horizontalLayout_53")
        self.email = QLineEdit(self.layoutWidget_4)
        self.email.setObjectName(u"email")
        sizePolicy11.setHeightForWidth(self.email.sizePolicy().hasHeightForWidth())
        self.email.setSizePolicy(sizePolicy11)
        self.email.setMinimumSize(QSize(300, 30))
        self.email.setFont(font2)

        self.horizontalLayout_53.addWidget(self.email)

        self.cpf = QLineEdit(self.layoutWidget_4)
        self.cpf.setObjectName(u"cpf")
        sizePolicy11.setHeightForWidth(self.cpf.sizePolicy().hasHeightForWidth())
        self.cpf.setSizePolicy(sizePolicy11)
        self.cpf.setMinimumSize(QSize(300, 30))
        self.cpf.setFont(font2)

        self.horizontalLayout_53.addWidget(self.cpf)


        self.verticalLayout_20.addLayout(self.horizontalLayout_53)


        self.verticalLayout_16.addLayout(self.verticalLayout_20)

        self.label_10 = QLabel(self.layoutWidget_4)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font2)

        self.verticalLayout_16.addWidget(self.label_10)

        self.desc = QTextEdit(self.layoutWidget_4)
        self.desc.setObjectName(u"desc")
        self.desc.setMinimumSize(QSize(0, 100))
        self.desc.setFont(font4)

        self.verticalLayout_16.addWidget(self.desc)

        self.layoutWidget_6 = QWidget(self.frame_8)
        self.layoutWidget_6.setObjectName(u"layoutWidget_6")
        self.layoutWidget_6.setGeometry(QRect(20, 510, 758, 72))
        self.horizontalLayout_57 = QHBoxLayout(self.layoutWidget_6)
        self.horizontalLayout_57.setObjectName(u"horizontalLayout_57")
        self.horizontalLayout_57.setContentsMargins(0, 0, 0, 0)
        self.cancel_client = QPushButton(self.layoutWidget_6)
        self.cancel_client.setObjectName(u"cancel_client")
        sizePolicy12 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy12.setHorizontalStretch(0)
        sizePolicy12.setVerticalStretch(0)
        sizePolicy12.setHeightForWidth(self.cancel_client.sizePolicy().hasHeightForWidth())
        self.cancel_client.setSizePolicy(sizePolicy12)
        self.cancel_client.setMinimumSize(QSize(150, 70))
        self.cancel_client.setFont(font2)
        self.cancel_client.setIcon(icon11)
        self.cancel_client.setIconSize(QSize(32, 32))

        self.horizontalLayout_57.addWidget(self.cancel_client)

        self.save_client = QPushButton(self.layoutWidget_6)
        self.save_client.setObjectName(u"save_client")
        sizePolicy12.setHeightForWidth(self.save_client.sizePolicy().hasHeightForWidth())
        self.save_client.setSizePolicy(sizePolicy12)
        self.save_client.setMinimumSize(QSize(150, 70))
        self.save_client.setFont(font2)
        self.save_client.setIcon(icon7)
        self.save_client.setIconSize(QSize(32, 32))

        self.horizontalLayout_57.addWidget(self.save_client)

        self.back_client = QPushButton(self.layoutWidget_6)
        self.back_client.setObjectName(u"back_client")
        sizePolicy12.setHeightForWidth(self.back_client.sizePolicy().hasHeightForWidth())
        self.back_client.setSizePolicy(sizePolicy12)
        self.back_client.setMinimumSize(QSize(150, 70))
        self.back_client.setFont(font2)
        self.back_client.setIcon(icon10)
        self.back_client.setIconSize(QSize(32, 32))

        self.horizontalLayout_57.addWidget(self.back_client)


        self.horizontalLayout_33.addWidget(self.frame_8)

        self.pages.addWidget(self.add_client)
        self.add_provider = QWidget()
        self.add_provider.setObjectName(u"add_provider")
        self.horizontalLayout_48 = QHBoxLayout(self.add_provider)
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.frame_15 = QFrame(self.add_provider)
        self.frame_15.setObjectName(u"frame_15")
        sizePolicy7.setHeightForWidth(self.frame_15.sizePolicy().hasHeightForWidth())
        self.frame_15.setSizePolicy(sizePolicy7)
        self.frame_15.setMinimumSize(QSize(800, 600))
        self.frame_15.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.frame_15.setFrameShape(QFrame.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Raised)
        self.gridLayout_9 = QGridLayout(self.frame_15)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(10, 19, 19, 0)
        self.verticalLayout_59 = QVBoxLayout()
        self.verticalLayout_59.setSpacing(0)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_59.setContentsMargins(-1, 0, 0, -1)
        self.verticalLayout_79 = QVBoxLayout()
        self.verticalLayout_79.setObjectName(u"verticalLayout_79")
        self.horizontalLayout_68 = QHBoxLayout()
        self.horizontalLayout_68.setObjectName(u"horizontalLayout_68")
        self.label_80 = QLabel(self.frame_15)
        self.label_80.setObjectName(u"label_80")
        self.label_80.setFont(font2)

        self.horizontalLayout_68.addWidget(self.label_80)

        self.label_81 = QLabel(self.frame_15)
        self.label_81.setObjectName(u"label_81")
        self.label_81.setFont(font2)

        self.horizontalLayout_68.addWidget(self.label_81)


        self.verticalLayout_79.addLayout(self.horizontalLayout_68)

        self.horizontalLayout_69 = QHBoxLayout()
        self.horizontalLayout_69.setObjectName(u"horizontalLayout_69")
        self.email_2 = QLineEdit(self.frame_15)
        self.email_2.setObjectName(u"email_2")
        sizePolicy11.setHeightForWidth(self.email_2.sizePolicy().hasHeightForWidth())
        self.email_2.setSizePolicy(sizePolicy11)
        self.email_2.setMinimumSize(QSize(300, 30))
        self.email_2.setFont(font2)

        self.horizontalLayout_69.addWidget(self.email_2, 0, Qt.AlignLeft)

        self.cpf_2 = QLineEdit(self.frame_15)
        self.cpf_2.setObjectName(u"cpf_2")
        sizePolicy11.setHeightForWidth(self.cpf_2.sizePolicy().hasHeightForWidth())
        self.cpf_2.setSizePolicy(sizePolicy11)
        self.cpf_2.setMinimumSize(QSize(300, 30))
        self.cpf_2.setFont(font2)

        self.horizontalLayout_69.addWidget(self.cpf_2, 0, Qt.AlignLeft)


        self.verticalLayout_79.addLayout(self.horizontalLayout_69)


        self.verticalLayout_59.addLayout(self.verticalLayout_79)

        self.label_26 = QLabel(self.frame_15)
        self.label_26.setObjectName(u"label_26")
        sizePolicy5.setHeightForWidth(self.label_26.sizePolicy().hasHeightForWidth())
        self.label_26.setSizePolicy(sizePolicy5)
        self.label_26.setFont(font2)
        self.label_26.setTextFormat(Qt.AutoText)
        self.label_26.setScaledContents(False)
        self.label_26.setIndent(-1)

        self.verticalLayout_59.addWidget(self.label_26)

        self.obs_provider = QTextEdit(self.frame_15)
        self.obs_provider.setObjectName(u"obs_provider")
        sizePolicy5.setHeightForWidth(self.obs_provider.sizePolicy().hasHeightForWidth())
        self.obs_provider.setSizePolicy(sizePolicy5)
        self.obs_provider.setMinimumSize(QSize(0, 100))
        self.obs_provider.setMaximumSize(QSize(16777215, 100))
        self.obs_provider.setFont(font4)

        self.verticalLayout_59.addWidget(self.obs_provider)

        self.verticalSpacer_4 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_59.addItem(self.verticalSpacer_4)

        self.horizontalLayout_56 = QHBoxLayout()
        self.horizontalLayout_56.setObjectName(u"horizontalLayout_56")
        self.cancel_provider = QPushButton(self.frame_15)
        self.cancel_provider.setObjectName(u"cancel_provider")
        sizePolicy12.setHeightForWidth(self.cancel_provider.sizePolicy().hasHeightForWidth())
        self.cancel_provider.setSizePolicy(sizePolicy12)
        self.cancel_provider.setMinimumSize(QSize(150, 70))
        self.cancel_provider.setFont(font2)
        self.cancel_provider.setIcon(icon11)
        self.cancel_provider.setIconSize(QSize(32, 32))

        self.horizontalLayout_56.addWidget(self.cancel_provider)

        self.save_provider = QPushButton(self.frame_15)
        self.save_provider.setObjectName(u"save_provider")
        sizePolicy12.setHeightForWidth(self.save_provider.sizePolicy().hasHeightForWidth())
        self.save_provider.setSizePolicy(sizePolicy12)
        self.save_provider.setMinimumSize(QSize(150, 70))
        self.save_provider.setFont(font2)
        self.save_provider.setIcon(icon7)
        self.save_provider.setIconSize(QSize(32, 32))

        self.horizontalLayout_56.addWidget(self.save_provider)

        self.back_provider = QPushButton(self.frame_15)
        self.back_provider.setObjectName(u"back_provider")
        sizePolicy12.setHeightForWidth(self.back_provider.sizePolicy().hasHeightForWidth())
        self.back_provider.setSizePolicy(sizePolicy12)
        self.back_provider.setMinimumSize(QSize(150, 70))
        self.back_provider.setFont(font2)
        self.back_provider.setIcon(icon10)
        self.back_provider.setIconSize(QSize(32, 32))

        self.horizontalLayout_56.addWidget(self.back_provider)


        self.verticalLayout_59.addLayout(self.horizontalLayout_56)


        self.gridLayout_9.addLayout(self.verticalLayout_59, 6, 0, 1, 1)

        self.verticalLayout_78 = QVBoxLayout()
        self.verticalLayout_78.setObjectName(u"verticalLayout_78")
        self.horizontalLayout_66 = QHBoxLayout()
        self.horizontalLayout_66.setObjectName(u"horizontalLayout_66")
        self.label_77 = QLabel(self.frame_15)
        self.label_77.setObjectName(u"label_77")
        sizePolicy.setHeightForWidth(self.label_77.sizePolicy().hasHeightForWidth())
        self.label_77.setSizePolicy(sizePolicy)
        self.label_77.setFont(font2)

        self.horizontalLayout_66.addWidget(self.label_77)

        self.label_79 = QLabel(self.frame_15)
        self.label_79.setObjectName(u"label_79")
        sizePolicy.setHeightForWidth(self.label_79.sizePolicy().hasHeightForWidth())
        self.label_79.setSizePolicy(sizePolicy)
        self.label_79.setFont(font2)

        self.horizontalLayout_66.addWidget(self.label_79)


        self.verticalLayout_78.addLayout(self.horizontalLayout_66)

        self.horizontalLayout_67 = QHBoxLayout()
        self.horizontalLayout_67.setObjectName(u"horizontalLayout_67")
        self.cdd_2 = QLineEdit(self.frame_15)
        self.cdd_2.setObjectName(u"cdd_2")
        sizePolicy11.setHeightForWidth(self.cdd_2.sizePolicy().hasHeightForWidth())
        self.cdd_2.setSizePolicy(sizePolicy11)
        self.cdd_2.setMinimumSize(QSize(300, 30))
        self.cdd_2.setFont(font2)

        self.horizontalLayout_67.addWidget(self.cdd_2, 0, Qt.AlignLeft)

        self.brr_2 = QLineEdit(self.frame_15)
        self.brr_2.setObjectName(u"brr_2")
        sizePolicy11.setHeightForWidth(self.brr_2.sizePolicy().hasHeightForWidth())
        self.brr_2.setSizePolicy(sizePolicy11)
        self.brr_2.setMinimumSize(QSize(300, 30))
        self.brr_2.setFont(font2)

        self.horizontalLayout_67.addWidget(self.brr_2, 0, Qt.AlignLeft)


        self.verticalLayout_78.addLayout(self.horizontalLayout_67)


        self.gridLayout_9.addLayout(self.verticalLayout_78, 3, 0, 1, 1)

        self.horizontalLayout_45 = QHBoxLayout()
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.verticalLayout_60 = QVBoxLayout()
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.label_19 = QLabel(self.frame_15)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setFont(font2)

        self.verticalLayout_60.addWidget(self.label_19)

        self.tel1_provider = QLineEdit(self.frame_15)
        self.tel1_provider.setObjectName(u"tel1_provider")
        sizePolicy13 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy13.setHorizontalStretch(0)
        sizePolicy13.setVerticalStretch(0)
        sizePolicy13.setHeightForWidth(self.tel1_provider.sizePolicy().hasHeightForWidth())
        self.tel1_provider.setSizePolicy(sizePolicy13)
        self.tel1_provider.setMinimumSize(QSize(0, 30))
        self.tel1_provider.setFont(font2)

        self.verticalLayout_60.addWidget(self.tel1_provider)


        self.horizontalLayout_45.addLayout(self.verticalLayout_60)

        self.verticalLayout_63 = QVBoxLayout()
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.label_20 = QLabel(self.frame_15)
        self.label_20.setObjectName(u"label_20")
        self.label_20.setFont(font2)

        self.verticalLayout_63.addWidget(self.label_20)

        self.tel2_provider = QLineEdit(self.frame_15)
        self.tel2_provider.setObjectName(u"tel2_provider")
        sizePolicy13.setHeightForWidth(self.tel2_provider.sizePolicy().hasHeightForWidth())
        self.tel2_provider.setSizePolicy(sizePolicy13)
        self.tel2_provider.setMinimumSize(QSize(0, 30))
        self.tel2_provider.setFont(font2)

        self.verticalLayout_63.addWidget(self.tel2_provider)


        self.horizontalLayout_45.addLayout(self.verticalLayout_63)


        self.gridLayout_9.addLayout(self.horizontalLayout_45, 1, 0, 1, 1)

        self.horizontalLayout_47 = QHBoxLayout()
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.verticalLayout_57 = QVBoxLayout()
        self.verticalLayout_57.setSpacing(7)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_57.setContentsMargins(-1, 0, -1, -1)
        self.label_18 = QLabel(self.frame_15)
        self.label_18.setObjectName(u"label_18")
        sizePolicy.setHeightForWidth(self.label_18.sizePolicy().hasHeightForWidth())
        self.label_18.setSizePolicy(sizePolicy)
        self.label_18.setFont(font2)

        self.verticalLayout_57.addWidget(self.label_18, 0, Qt.AlignLeft)

        self.end_provider = QLineEdit(self.frame_15)
        self.end_provider.setObjectName(u"end_provider")
        sizePolicy11.setHeightForWidth(self.end_provider.sizePolicy().hasHeightForWidth())
        self.end_provider.setSizePolicy(sizePolicy11)
        self.end_provider.setMinimumSize(QSize(400, 30))
        self.end_provider.setMaximumSize(QSize(16777215, 40))
        self.end_provider.setFont(font2)

        self.verticalLayout_57.addWidget(self.end_provider, 0, Qt.AlignLeft|Qt.AlignBottom)


        self.horizontalLayout_47.addLayout(self.verticalLayout_57)


        self.gridLayout_9.addLayout(self.horizontalLayout_47, 2, 0, 1, 1)

        self.verticalLayout_37 = QVBoxLayout()
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_37.setContentsMargins(-1, 0, -1, -1)
        self.label_17 = QLabel(self.frame_15)
        self.label_17.setObjectName(u"label_17")
        sizePolicy9.setHeightForWidth(self.label_17.sizePolicy().hasHeightForWidth())
        self.label_17.setSizePolicy(sizePolicy9)
        self.label_17.setFont(font2)

        self.verticalLayout_37.addWidget(self.label_17)

        self.nome_provider = QLineEdit(self.frame_15)
        self.nome_provider.setObjectName(u"nome_provider")
        sizePolicy14 = QSizePolicy(QSizePolicy.Maximum, QSizePolicy.Fixed)
        sizePolicy14.setHorizontalStretch(0)
        sizePolicy14.setVerticalStretch(44)
        sizePolicy14.setHeightForWidth(self.nome_provider.sizePolicy().hasHeightForWidth())
        self.nome_provider.setSizePolicy(sizePolicy14)
        self.nome_provider.setMinimumSize(QSize(400, 30))
        self.nome_provider.setSizeIncrement(QSize(0, 0))
        font5 = QFont()
        font5.setPointSize(10)
        font5.setKerning(True)
        self.nome_provider.setFont(font5)
        self.nome_provider.setStyleSheet(u"")
        self.nome_provider.setFrame(True)
        self.nome_provider.setClearButtonEnabled(False)

        self.verticalLayout_37.addWidget(self.nome_provider)


        self.gridLayout_9.addLayout(self.verticalLayout_37, 0, 0, 1, 1)

        self.verticalLayout_61 = QVBoxLayout()
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")

        self.gridLayout_9.addLayout(self.verticalLayout_61, 6, 1, 1, 1)


        self.horizontalLayout_48.addWidget(self.frame_15)

        self.pages.addWidget(self.add_provider)
        self.add_task = QWidget()
        self.add_task.setObjectName(u"add_task")
        self.verticalLayout_32 = QVBoxLayout(self.add_task)
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.frame_10 = QFrame(self.add_task)
        self.frame_10.setObjectName(u"frame_10")
        sizePolicy7.setHeightForWidth(self.frame_10.sizePolicy().hasHeightForWidth())
        self.frame_10.setSizePolicy(sizePolicy7)
        self.frame_10.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.frame_10.setFrameShape(QFrame.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Raised)
        self.gridLayout_5 = QGridLayout(self.frame_10)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(30, 44, 140, 45)
        self.verticalLayout_23 = QVBoxLayout()
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.label_31 = QLabel(self.frame_10)
        self.label_31.setObjectName(u"label_31")
        self.label_31.setFont(font2)

        self.verticalLayout_23.addWidget(self.label_31)

        self.com = QLineEdit(self.frame_10)
        self.com.setObjectName(u"com")
        sizePolicy15 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Minimum)
        sizePolicy15.setHorizontalStretch(0)
        sizePolicy15.setVerticalStretch(0)
        sizePolicy15.setHeightForWidth(self.com.sizePolicy().hasHeightForWidth())
        self.com.setSizePolicy(sizePolicy15)
        self.com.setMinimumSize(QSize(0, 30))
        self.com.setMaximumSize(QSize(400, 16777215))
        self.com.setFont(font2)

        self.verticalLayout_23.addWidget(self.com)

        self.label_32 = QLabel(self.frame_10)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setFont(font2)

        self.verticalLayout_23.addWidget(self.label_32)

        self.cliente = QLineEdit(self.frame_10)
        self.cliente.setObjectName(u"cliente")
        sizePolicy15.setHeightForWidth(self.cliente.sizePolicy().hasHeightForWidth())
        self.cliente.setSizePolicy(sizePolicy15)
        self.cliente.setMinimumSize(QSize(0, 30))
        self.cliente.setMaximumSize(QSize(400, 16777215))
        self.cliente.setFont(font2)

        self.verticalLayout_23.addWidget(self.cliente)

        self.verticalLayout_25 = QVBoxLayout()
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.horizontalLayout_72 = QHBoxLayout()
        self.horizontalLayout_72.setSpacing(100)
        self.horizontalLayout_72.setObjectName(u"horizontalLayout_72")
        self.label_36 = QLabel(self.frame_10)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font2)

        self.horizontalLayout_72.addWidget(self.label_36)

        self.label_43 = QLabel(self.frame_10)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font2)

        self.horizontalLayout_72.addWidget(self.label_43)

        self.horizontalSpacer_31 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_72.addItem(self.horizontalSpacer_31)


        self.verticalLayout_25.addLayout(self.horizontalLayout_72)

        self.horizontalLayout_73 = QHBoxLayout()
        self.horizontalLayout_73.setObjectName(u"horizontalLayout_73")
        self.tel1_3 = QLineEdit(self.frame_10)
        self.tel1_3.setObjectName(u"tel1_3")
        sizePolicy3.setHeightForWidth(self.tel1_3.sizePolicy().hasHeightForWidth())
        self.tel1_3.setSizePolicy(sizePolicy3)
        self.tel1_3.setMinimumSize(QSize(0, 30))
        self.tel1_3.setMaximumSize(QSize(200, 16777215))
        self.tel1_3.setFont(font2)

        self.horizontalLayout_73.addWidget(self.tel1_3)

        self.tel2_3 = QLineEdit(self.frame_10)
        self.tel2_3.setObjectName(u"tel2_3")
        sizePolicy3.setHeightForWidth(self.tel2_3.sizePolicy().hasHeightForWidth())
        self.tel2_3.setSizePolicy(sizePolicy3)
        self.tel2_3.setMinimumSize(QSize(180, 30))
        self.tel2_3.setMaximumSize(QSize(200, 16777215))
        self.tel2_3.setFont(font2)

        self.horizontalLayout_73.addWidget(self.tel2_3)

        self.horizontalSpacer_30 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_73.addItem(self.horizontalSpacer_30)


        self.verticalLayout_25.addLayout(self.horizontalLayout_73)


        self.verticalLayout_23.addLayout(self.verticalLayout_25)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setSpacing(30)
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.label_28 = QLabel(self.frame_10)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setFont(font2)

        self.horizontalLayout_22.addWidget(self.label_28)

        self.label_29 = QLabel(self.frame_10)
        self.label_29.setObjectName(u"label_29")
        self.label_29.setFont(font2)

        self.horizontalLayout_22.addWidget(self.label_29)

        self.horizontalSpacer_29 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_22.addItem(self.horizontalSpacer_29)


        self.verticalLayout_7.addLayout(self.horizontalLayout_22)

        self.horizontalLayout_70 = QHBoxLayout()
        self.horizontalLayout_70.setObjectName(u"horizontalLayout_70")
        self.data = QLineEdit(self.frame_10)
        self.data.setObjectName(u"data")
        sizePolicy16 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Minimum)
        sizePolicy16.setHorizontalStretch(0)
        sizePolicy16.setVerticalStretch(0)
        sizePolicy16.setHeightForWidth(self.data.sizePolicy().hasHeightForWidth())
        self.data.setSizePolicy(sizePolicy16)
        self.data.setMinimumSize(QSize(150, 30))
        self.data.setFont(font2)

        self.horizontalLayout_70.addWidget(self.data)

        self.hora = QLineEdit(self.frame_10)
        self.hora.setObjectName(u"hora")
        sizePolicy16.setHeightForWidth(self.hora.sizePolicy().hasHeightForWidth())
        self.hora.setSizePolicy(sizePolicy16)
        self.hora.setMinimumSize(QSize(150, 30))
        self.hora.setFont(font2)

        self.horizontalLayout_70.addWidget(self.hora)

        self.horizontalSpacer_28 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_70.addItem(self.horizontalSpacer_28)


        self.verticalLayout_7.addLayout(self.horizontalLayout_70)


        self.verticalLayout_23.addLayout(self.verticalLayout_7)

        self.label_33 = QLabel(self.frame_10)
        self.label_33.setObjectName(u"label_33")
        self.label_33.setFont(font2)

        self.verticalLayout_23.addWidget(self.label_33)

        self.end_2 = QLineEdit(self.frame_10)
        self.end_2.setObjectName(u"end_2")
        sizePolicy15.setHeightForWidth(self.end_2.sizePolicy().hasHeightForWidth())
        self.end_2.setSizePolicy(sizePolicy15)
        self.end_2.setMinimumSize(QSize(0, 30))
        self.end_2.setMaximumSize(QSize(400, 16777215))
        self.end_2.setFont(font2)

        self.verticalLayout_23.addWidget(self.end_2)


        self.gridLayout_5.addLayout(self.verticalLayout_23, 0, 0, 1, 4)

        self.splitter = QSplitter(self.frame_10)
        self.splitter.setObjectName(u"splitter")
        self.splitter.setOrientation(Qt.Horizontal)
        self.layoutWidget_8 = QWidget(self.splitter)
        self.layoutWidget_8.setObjectName(u"layoutWidget_8")
        self.verticalLayout_27 = QVBoxLayout(self.layoutWidget_8)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_27.setContentsMargins(0, 0, 0, 0)
        self.cancel_task = QPushButton(self.layoutWidget_8)
        self.cancel_task.setObjectName(u"cancel_task")
        sizePolicy1.setHeightForWidth(self.cancel_task.sizePolicy().hasHeightForWidth())
        self.cancel_task.setSizePolicy(sizePolicy1)
        self.cancel_task.setMinimumSize(QSize(100, 0))
        self.cancel_task.setFont(font2)
        self.cancel_task.setIcon(icon11)
        self.cancel_task.setIconSize(QSize(40, 40))

        self.verticalLayout_27.addWidget(self.cancel_task)

        self.print_task = QPushButton(self.layoutWidget_8)
        self.print_task.setObjectName(u"print_task")
        sizePolicy1.setHeightForWidth(self.print_task.sizePolicy().hasHeightForWidth())
        self.print_task.setSizePolicy(sizePolicy1)
        self.print_task.setFont(font2)
        self.print_task.setIcon(icon12)
        self.print_task.setIconSize(QSize(32, 32))

        self.verticalLayout_27.addWidget(self.print_task)

        self.splitter.addWidget(self.layoutWidget_8)
        self.layoutWidget_9 = QWidget(self.splitter)
        self.layoutWidget_9.setObjectName(u"layoutWidget_9")
        self.verticalLayout_28 = QVBoxLayout(self.layoutWidget_9)
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.verticalLayout_28.setContentsMargins(0, 0, 0, 0)
        self.save_task = QPushButton(self.layoutWidget_9)
        self.save_task.setObjectName(u"save_task")
        sizePolicy1.setHeightForWidth(self.save_task.sizePolicy().hasHeightForWidth())
        self.save_task.setSizePolicy(sizePolicy1)
        self.save_task.setFont(font2)
        icon13 = QIcon()
        icon13.addFile(u":/Icons/task.png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_task.setIcon(icon13)
        self.save_task.setIconSize(QSize(40, 40))

        self.verticalLayout_28.addWidget(self.save_task)

        self.back_task = QPushButton(self.layoutWidget_9)
        self.back_task.setObjectName(u"back_task")
        sizePolicy1.setHeightForWidth(self.back_task.sizePolicy().hasHeightForWidth())
        self.back_task.setSizePolicy(sizePolicy1)
        self.back_task.setMinimumSize(QSize(100, 0))
        self.back_task.setFont(font2)
        self.back_task.setIcon(icon10)
        self.back_task.setIconSize(QSize(32, 32))

        self.verticalLayout_28.addWidget(self.back_task)

        self.splitter.addWidget(self.layoutWidget_9)

        self.gridLayout_5.addWidget(self.splitter, 2, 3, 1, 1)

        self.horizontalSpacer_21 = QSpacerItem(100, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.gridLayout_5.addItem(self.horizontalSpacer_21, 2, 2, 1, 1)

        self.verticalLayout_29 = QVBoxLayout()
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.label_30 = QLabel(self.frame_10)
        self.label_30.setObjectName(u"label_30")
        self.label_30.setFont(font2)

        self.verticalLayout_29.addWidget(self.label_30)

        self.obs_agenda = QTextEdit(self.frame_10)
        self.obs_agenda.setObjectName(u"obs_agenda")
        self.obs_agenda.setMinimumSize(QSize(400, 0))
        self.obs_agenda.setFont(font2)

        self.verticalLayout_29.addWidget(self.obs_agenda)


        self.gridLayout_5.addLayout(self.verticalLayout_29, 2, 0, 1, 2)


        self.verticalLayout_32.addWidget(self.frame_10, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.add_task)
        self.add_cashier = QWidget()
        self.add_cashier.setObjectName(u"add_cashier")
        self.verticalLayout_39 = QVBoxLayout(self.add_cashier)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.frame_12 = QFrame(self.add_cashier)
        self.frame_12.setObjectName(u"frame_12")
        sizePolicy7.setHeightForWidth(self.frame_12.sizePolicy().hasHeightForWidth())
        self.frame_12.setSizePolicy(sizePolicy7)
        self.frame_12.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.frame_12.setFrameShape(QFrame.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_2 = QHBoxLayout(self.frame_12)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(30, 40, 140, 191)
        self.verticalLayout_21 = QVBoxLayout()
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_33 = QVBoxLayout()
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_60 = QLabel(self.frame_12)
        self.label_60.setObjectName(u"label_60")
        sizePolicy5.setHeightForWidth(self.label_60.sizePolicy().hasHeightForWidth())
        self.label_60.setSizePolicy(sizePolicy5)
        self.label_60.setFont(font2)

        self.verticalLayout_34.addWidget(self.label_60)

        self.horizontalLayout_58 = QHBoxLayout()
        self.horizontalLayout_58.setObjectName(u"horizontalLayout_58")
        self.valor = QDoubleSpinBox(self.frame_12)
        self.valor.setObjectName(u"valor")
        sizePolicy11.setHeightForWidth(self.valor.sizePolicy().hasHeightForWidth())
        self.valor.setSizePolicy(sizePolicy11)
        self.valor.setMinimumSize(QSize(150, 40))
        self.valor.setFont(font2)
        self.valor.setAlignment(Qt.AlignCenter)
        self.valor.setMaximum(99999.990000000005239)

        self.horizontalLayout_58.addWidget(self.valor, 0, Qt.AlignLeft)

        self.forma = QComboBox(self.frame_12)
        self.forma.addItem("")
        self.forma.addItem("")
        self.forma.addItem("")
        self.forma.addItem("")
        self.forma.addItem("")
        self.forma.addItem("")
        self.forma.addItem("")
        self.forma.addItem("")
        self.forma.addItem("")
        self.forma.addItem("")
        self.forma.addItem("")
        self.forma.setObjectName(u"forma")
        sizePolicy11.setHeightForWidth(self.forma.sizePolicy().hasHeightForWidth())
        self.forma.setSizePolicy(sizePolicy11)
        self.forma.setMinimumSize(QSize(250, 40))
        self.forma.setSizeIncrement(QSize(0, 0))
        self.forma.setFont(font2)

        self.horizontalLayout_58.addWidget(self.forma, 0, Qt.AlignLeft)


        self.verticalLayout_34.addLayout(self.horizontalLayout_58)


        self.verticalLayout_33.addLayout(self.verticalLayout_34)

        self.verticalLayout_35 = QVBoxLayout()
        self.verticalLayout_35.setSpacing(6)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.label_61 = QLabel(self.frame_12)
        self.label_61.setObjectName(u"label_61")
        sizePolicy5.setHeightForWidth(self.label_61.sizePolicy().hasHeightForWidth())
        self.label_61.setSizePolicy(sizePolicy5)
        self.label_61.setFont(font2)

        self.verticalLayout_35.addWidget(self.label_61)

        self.date_cashier = QDateEdit(self.frame_12)
        self.date_cashier.setObjectName(u"date_cashier")
        sizePolicy11.setHeightForWidth(self.date_cashier.sizePolicy().hasHeightForWidth())
        self.date_cashier.setSizePolicy(sizePolicy11)
        self.date_cashier.setMinimumSize(QSize(200, 40))
        self.date_cashier.setFont(font2)
        self.date_cashier.setAlignment(Qt.AlignCenter)
        self.date_cashier.setCalendarPopup(True)

        self.verticalLayout_35.addWidget(self.date_cashier)


        self.verticalLayout_33.addLayout(self.verticalLayout_35)


        self.verticalLayout_21.addLayout(self.verticalLayout_33)

        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setSpacing(0)
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.verticalLayout_38.setContentsMargins(-1, 0, -1, 0)
        self.label_59 = QLabel(self.frame_12)
        self.label_59.setObjectName(u"label_59")
        sizePolicy5.setHeightForWidth(self.label_59.sizePolicy().hasHeightForWidth())
        self.label_59.setSizePolicy(sizePolicy5)
        self.label_59.setFont(font2)

        self.verticalLayout_38.addWidget(self.label_59)

        self.desc_entrada = QTextEdit(self.frame_12)
        self.desc_entrada.setObjectName(u"desc_entrada")
        sizePolicy10.setHeightForWidth(self.desc_entrada.sizePolicy().hasHeightForWidth())
        self.desc_entrada.setSizePolicy(sizePolicy10)
        self.desc_entrada.setMinimumSize(QSize(500, 0))
        self.desc_entrada.setFont(font2)

        self.verticalLayout_38.addWidget(self.desc_entrada)

        self.verticalSpacer_6 = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_38.addItem(self.verticalSpacer_6)

        self.horizontalLayout_59 = QHBoxLayout()
        self.horizontalLayout_59.setSpacing(23)
        self.horizontalLayout_59.setObjectName(u"horizontalLayout_59")
        self.horizontalLayout_59.setContentsMargins(-1, 0, -1, -1)
        self.add_entry = QPushButton(self.frame_12)
        self.add_entry.setObjectName(u"add_entry")
        sizePolicy12.setHeightForWidth(self.add_entry.sizePolicy().hasHeightForWidth())
        self.add_entry.setSizePolicy(sizePolicy12)
        self.add_entry.setFont(font2)
        icon14 = QIcon()
        icon14.addFile(u":/Icons/add_money.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_entry.setIcon(icon14)
        self.add_entry.setIconSize(QSize(40, 40))

        self.horizontalLayout_59.addWidget(self.add_entry)

        self.add_out = QPushButton(self.frame_12)
        self.add_out.setObjectName(u"add_out")
        sizePolicy12.setHeightForWidth(self.add_out.sizePolicy().hasHeightForWidth())
        self.add_out.setSizePolicy(sizePolicy12)
        self.add_out.setFont(font2)
        icon15 = QIcon()
        icon15.addFile(u":/Icons/less_money.png", QSize(), QIcon.Normal, QIcon.Off)
        self.add_out.setIcon(icon15)
        self.add_out.setIconSize(QSize(40, 40))

        self.horizontalLayout_59.addWidget(self.add_out)

        self.back_cashier = QPushButton(self.frame_12)
        self.back_cashier.setObjectName(u"back_cashier")
        self.back_cashier.setIcon(icon10)
        self.back_cashier.setIconSize(QSize(32, 32))

        self.horizontalLayout_59.addWidget(self.back_cashier)


        self.verticalLayout_38.addLayout(self.horizontalLayout_59)


        self.verticalLayout_21.addLayout(self.verticalLayout_38)


        self.horizontalLayout_2.addLayout(self.verticalLayout_21)


        self.verticalLayout_39.addWidget(self.frame_12, 0, Qt.AlignHCenter|Qt.AlignVCenter)

        self.pages.addWidget(self.add_cashier)
        self.add_product = QWidget()
        self.add_product.setObjectName(u"add_product")
        self.verticalLayout_41 = QVBoxLayout(self.add_product)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.frame_13 = QFrame(self.add_product)
        self.frame_13.setObjectName(u"frame_13")
        sizePolicy17 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        sizePolicy17.setHorizontalStretch(0)
        sizePolicy17.setVerticalStretch(0)
        sizePolicy17.setHeightForWidth(self.frame_13.sizePolicy().hasHeightForWidth())
        self.frame_13.setSizePolicy(sizePolicy17)
        self.frame_13.setMinimumSize(QSize(700, 0))
        self.frame_13.setMaximumSize(QSize(900, 16777215))
        self.frame_13.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.frame_13.setFrameShape(QFrame.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Raised)
        self.verticalLayout_22 = QVBoxLayout(self.frame_13)
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.verticalLayout_22.setContentsMargins(30, 44, 140, 45)
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_44 = QLabel(self.frame_13)
        self.label_44.setObjectName(u"label_44")
        sizePolicy5.setHeightForWidth(self.label_44.sizePolicy().hasHeightForWidth())
        self.label_44.setSizePolicy(sizePolicy5)

        self.verticalLayout_56.addWidget(self.label_44)

        self.nm_prod = QLineEdit(self.frame_13)
        self.nm_prod.setObjectName(u"nm_prod")
        self.nm_prod.setMinimumSize(QSize(300, 30))
        self.nm_prod.setFont(font2)

        self.verticalLayout_56.addWidget(self.nm_prod)


        self.horizontalLayout_44.addLayout(self.verticalLayout_56)

        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_47 = QLabel(self.frame_13)
        self.label_47.setObjectName(u"label_47")
        sizePolicy5.setHeightForWidth(self.label_47.sizePolicy().hasHeightForWidth())
        self.label_47.setSizePolicy(sizePolicy5)
        self.label_47.setFont(font2)

        self.verticalLayout_43.addWidget(self.label_47)

        self.grup_prod = QLineEdit(self.frame_13)
        self.grup_prod.setObjectName(u"grup_prod")
        self.grup_prod.setMinimumSize(QSize(0, 30))
        self.grup_prod.setFont(font2)

        self.verticalLayout_43.addWidget(self.grup_prod)


        self.horizontalLayout_44.addLayout(self.verticalLayout_43)


        self.horizontalLayout_5.addLayout(self.horizontalLayout_44)

        self.verticalLayout_62 = QVBoxLayout()
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.label_66 = QLabel(self.frame_13)
        self.label_66.setObjectName(u"label_66")

        self.verticalLayout_62.addWidget(self.label_66)

        self.qt_prod = QLineEdit(self.frame_13)
        self.qt_prod.setObjectName(u"qt_prod")
        sizePolicy10.setHeightForWidth(self.qt_prod.sizePolicy().hasHeightForWidth())
        self.qt_prod.setSizePolicy(sizePolicy10)
        self.qt_prod.setMinimumSize(QSize(0, 30))
        self.qt_prod.setMaximumSize(QSize(80, 30))
        self.qt_prod.setFont(font2)

        self.verticalLayout_62.addWidget(self.qt_prod)


        self.horizontalLayout_5.addLayout(self.verticalLayout_62)


        self.verticalLayout_22.addLayout(self.horizontalLayout_5)

        self.verticalLayout_45 = QVBoxLayout()
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_45.setContentsMargins(-1, 28, -1, -1)
        self.label_46 = QLabel(self.frame_13)
        self.label_46.setObjectName(u"label_46")

        self.verticalLayout_45.addWidget(self.label_46)

        self.desc_prod = QTextEdit(self.frame_13)
        self.desc_prod.setObjectName(u"desc_prod")
        sizePolicy12.setHeightForWidth(self.desc_prod.sizePolicy().hasHeightForWidth())
        self.desc_prod.setSizePolicy(sizePolicy12)
        self.desc_prod.setFont(font2)

        self.verticalLayout_45.addWidget(self.desc_prod)


        self.verticalLayout_22.addLayout(self.verticalLayout_45)

        self.label_45 = QLabel(self.frame_13)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_22.addWidget(self.label_45)

        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.horizontalLayout_35 = QHBoxLayout()
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.uni = QRadioButton(self.frame_13)
        self.uni.setObjectName(u"uni")
        sizePolicy18 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy18.setHorizontalStretch(0)
        sizePolicy18.setVerticalStretch(0)
        sizePolicy18.setHeightForWidth(self.uni.sizePolicy().hasHeightForWidth())
        self.uni.setSizePolicy(sizePolicy18)
        font6 = QFont()
        font6.setPointSize(18)
        self.uni.setFont(font6)
        self.uni.setChecked(True)

        self.horizontalLayout_35.addWidget(self.uni)

        self.label_40 = QLabel(self.frame_13)
        self.label_40.setObjectName(u"label_40")
        sizePolicy.setHeightForWidth(self.label_40.sizePolicy().hasHeightForWidth())
        self.label_40.setSizePolicy(sizePolicy)

        self.horizontalLayout_35.addWidget(self.label_40)

        self.valor_uni = QDoubleSpinBox(self.frame_13)
        self.valor_uni.setObjectName(u"valor_uni")
        sizePolicy15.setHeightForWidth(self.valor_uni.sizePolicy().hasHeightForWidth())
        self.valor_uni.setSizePolicy(sizePolicy15)
        self.valor_uni.setFont(font1)
        self.valor_uni.setDecimals(2)
        self.valor_uni.setMaximum(99999.990000000005239)
        self.valor_uni.setStepType(QAbstractSpinBox.DefaultStepType)

        self.horizontalLayout_35.addWidget(self.valor_uni)


        self.verticalLayout_40.addLayout(self.horizontalLayout_35)

        self.horizontalLayout_37 = QHBoxLayout()
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.m2 = QRadioButton(self.frame_13)
        self.m2.setObjectName(u"m2")
        sizePolicy18.setHeightForWidth(self.m2.sizePolicy().hasHeightForWidth())
        self.m2.setSizePolicy(sizePolicy18)
        self.m2.setFont(font6)

        self.horizontalLayout_37.addWidget(self.m2)

        self.label_41 = QLabel(self.frame_13)
        self.label_41.setObjectName(u"label_41")
        sizePolicy.setHeightForWidth(self.label_41.sizePolicy().hasHeightForWidth())
        self.label_41.setSizePolicy(sizePolicy)

        self.horizontalLayout_37.addWidget(self.label_41)

        self.valor_m2 = QDoubleSpinBox(self.frame_13)
        self.valor_m2.setObjectName(u"valor_m2")
        sizePolicy15.setHeightForWidth(self.valor_m2.sizePolicy().hasHeightForWidth())
        self.valor_m2.setSizePolicy(sizePolicy15)
        self.valor_m2.setFont(font2)
        self.valor_m2.setMaximum(99999.990000000005239)

        self.horizontalLayout_37.addWidget(self.valor_m2)


        self.verticalLayout_40.addLayout(self.horizontalLayout_37)

        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.kg = QRadioButton(self.frame_13)
        self.kg.setObjectName(u"kg")
        sizePolicy18.setHeightForWidth(self.kg.sizePolicy().hasHeightForWidth())
        self.kg.setSizePolicy(sizePolicy18)
        font7 = QFont()
        font7.setPointSize(14)
        self.kg.setFont(font7)

        self.horizontalLayout_38.addWidget(self.kg)

        self.label_42 = QLabel(self.frame_13)
        self.label_42.setObjectName(u"label_42")
        sizePolicy.setHeightForWidth(self.label_42.sizePolicy().hasHeightForWidth())
        self.label_42.setSizePolicy(sizePolicy)

        self.horizontalLayout_38.addWidget(self.label_42)

        self.valor_kg = QDoubleSpinBox(self.frame_13)
        self.valor_kg.setObjectName(u"valor_kg")
        sizePolicy15.setHeightForWidth(self.valor_kg.sizePolicy().hasHeightForWidth())
        self.valor_kg.setSizePolicy(sizePolicy15)
        self.valor_kg.setFont(font2)
        self.valor_kg.setMaximum(99999.990000000005239)

        self.horizontalLayout_38.addWidget(self.valor_kg)


        self.verticalLayout_40.addLayout(self.horizontalLayout_38)


        self.verticalLayout_22.addLayout(self.verticalLayout_40)

        self.verticalSpacer = QSpacerItem(20, 100, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout_22.addItem(self.verticalSpacer)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setSpacing(45)
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.horizontalSpacer_8 = QSpacerItem(63, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_24.addItem(self.horizontalSpacer_8)

        self.back_product = QPushButton(self.frame_13)
        self.back_product.setObjectName(u"back_product")
        self.back_product.setIcon(icon10)
        self.back_product.setIconSize(QSize(40, 40))

        self.horizontalLayout_24.addWidget(self.back_product)

        self.cancel_product = QPushButton(self.frame_13)
        self.cancel_product.setObjectName(u"cancel_product")
        self.cancel_product.setFont(font2)
        self.cancel_product.setIcon(icon11)
        self.cancel_product.setIconSize(QSize(40, 40))

        self.horizontalLayout_24.addWidget(self.cancel_product, 0, Qt.AlignHCenter)

        self.save_product = QPushButton(self.frame_13)
        self.save_product.setObjectName(u"save_product")
        font8 = QFont()
        font8.setPointSize(11)
        self.save_product.setFont(font8)
        icon16 = QIcon()
        icon16.addFile(u":/Icons/add(1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.save_product.setIcon(icon16)
        self.save_product.setIconSize(QSize(54, 54))

        self.horizontalLayout_24.addWidget(self.save_product)


        self.verticalLayout_22.addLayout(self.horizontalLayout_24)


        self.verticalLayout_41.addWidget(self.frame_13, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.add_product)
        self.add_os = QWidget()
        self.add_os.setObjectName(u"add_os")
        self.add_os.setMinimumSize(QSize(0, 0))
        self.verticalLayout_47 = QVBoxLayout(self.add_os)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_47.setContentsMargins(0, 0, 0, 0)
        self.frame_14 = QFrame(self.add_os)
        self.frame_14.setObjectName(u"frame_14")
        sizePolicy2.setHeightForWidth(self.frame_14.sizePolicy().hasHeightForWidth())
        self.frame_14.setSizePolicy(sizePolicy2)
        self.frame_14.setMinimumSize(QSize(0, 0))
        self.frame_14.setMaximumSize(QSize(1920, 1080))
        self.frame_14.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.frame_14.setFrameShape(QFrame.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Raised)
        self.gridLayout_8 = QGridLayout(self.frame_14)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(11, 5, 11, -1)
        self.horizontalLayout_43 = QHBoxLayout()
        self.horizontalLayout_43.setSpacing(0)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_43.setContentsMargins(-1, 0, -1, -1)
        self.comboBox = QComboBox(self.frame_14)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        self.comboBox.setMinimumSize(QSize(200, 30))

        self.horizontalLayout_43.addWidget(self.comboBox)

        self.calc = QPushButton(self.frame_14)
        self.calc.setObjectName(u"calc")
        self.calc.setMinimumSize(QSize(0, 0))
        self.calc.setFont(font4)
        icon17 = QIcon()
        icon17.addFile(u":/Icons/calculator.png", QSize(), QIcon.Normal, QIcon.Off)
        self.calc.setIcon(icon17)
        self.calc.setIconSize(QSize(54, 54))

        self.horizontalLayout_43.addWidget(self.calc)

        self.horizontalSpacer_22 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_43.addItem(self.horizontalSpacer_22)

        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.verticalLayout_46.setContentsMargins(-1, 0, 0, -1)
        self.horizontalLayout_41 = QHBoxLayout()
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.finish_os = QPushButton(self.frame_14)
        self.finish_os.setObjectName(u"finish_os")
        self.finish_os.setFont(font4)
        self.finish_os.setIcon(icon12)
        self.finish_os.setIconSize(QSize(38, 38))

        self.horizontalLayout_41.addWidget(self.finish_os)

        self.inserir_produto = QPushButton(self.frame_14)
        self.inserir_produto.setObjectName(u"inserir_produto")
        sizePolicy13.setHeightForWidth(self.inserir_produto.sizePolicy().hasHeightForWidth())
        self.inserir_produto.setSizePolicy(sizePolicy13)
        self.inserir_produto.setFont(font4)
        icon18 = QIcon()
        icon18.addFile(u":/Icons/payment.png", QSize(), QIcon.Normal, QIcon.Off)
        self.inserir_produto.setIcon(icon18)
        self.inserir_produto.setIconSize(QSize(300, 50))

        self.horizontalLayout_41.addWidget(self.inserir_produto)

        self.salvar_os = QPushButton(self.frame_14)
        self.salvar_os.setObjectName(u"salvar_os")
        self.salvar_os.setFont(font4)
        icon19 = QIcon()
        icon19.addFile(u":/Icons/check.png", QSize(), QIcon.Normal, QIcon.Off)
        self.salvar_os.setIcon(icon19)
        self.salvar_os.setIconSize(QSize(38, 48))

        self.horizontalLayout_41.addWidget(self.salvar_os)


        self.verticalLayout_46.addLayout(self.horizontalLayout_41)


        self.horizontalLayout_43.addLayout(self.verticalLayout_46)

        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.horizontalSpacer_23 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_42.addItem(self.horizontalSpacer_23)

        self.label_64 = QLabel(self.frame_14)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font7)

        self.horizontalLayout_42.addWidget(self.label_64, 0, Qt.AlignRight)

        self.total = QLineEdit(self.frame_14)
        self.total.setObjectName(u"total")
        sizePolicy10.setHeightForWidth(self.total.sizePolicy().hasHeightForWidth())
        self.total.setSizePolicy(sizePolicy10)
        self.total.setMinimumSize(QSize(0, 60))
        self.total.setFont(font7)

        self.horizontalLayout_42.addWidget(self.total, 0, Qt.AlignRight)


        self.horizontalLayout_43.addLayout(self.horizontalLayout_42)


        self.gridLayout_8.addLayout(self.horizontalLayout_43, 1, 1, 1, 1)

        self.tab_os = QTabWidget(self.frame_14)
        self.tab_os.setObjectName(u"tab_os")
        sizePolicy19 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy19.setHorizontalStretch(0)
        sizePolicy19.setVerticalStretch(0)
        sizePolicy19.setHeightForWidth(self.tab_os.sizePolicy().hasHeightForWidth())
        self.tab_os.setSizePolicy(sizePolicy19)
        self.tab_os.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.horizontalLayout_16 = QHBoxLayout(self.tab_5)
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.label_8 = QLabel(self.tab_5)
        self.label_8.setObjectName(u"label_8")
        sizePolicy9.setHeightForWidth(self.label_8.sizePolicy().hasHeightForWidth())
        self.label_8.setSizePolicy(sizePolicy9)
        self.label_8.setFont(font2)

        self.verticalLayout_58.addWidget(self.label_8, 0, Qt.AlignLeft)

        self.nm_os = QLineEdit(self.tab_5)
        self.nm_os.setObjectName(u"nm_os")
        sizePolicy10.setHeightForWidth(self.nm_os.sizePolicy().hasHeightForWidth())
        self.nm_os.setSizePolicy(sizePolicy10)
        self.nm_os.setMinimumSize(QSize(400, 30))
        self.nm_os.setFont(font2)

        self.verticalLayout_58.addWidget(self.nm_os, 0, Qt.AlignLeft)

        self.verticalLayout_64 = QVBoxLayout()
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.label_9 = QLabel(self.tab_5)
        self.label_9.setObjectName(u"label_9")
        sizePolicy9.setHeightForWidth(self.label_9.sizePolicy().hasHeightForWidth())
        self.label_9.setSizePolicy(sizePolicy9)
        self.label_9.setFont(font2)

        self.verticalLayout_64.addWidget(self.label_9)

        self.end_os = QLineEdit(self.tab_5)
        self.end_os.setObjectName(u"end_os")
        sizePolicy10.setHeightForWidth(self.end_os.sizePolicy().hasHeightForWidth())
        self.end_os.setSizePolicy(sizePolicy10)
        self.end_os.setMinimumSize(QSize(400, 30))
        self.end_os.setFont(font2)

        self.verticalLayout_64.addWidget(self.end_os)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.verticalLayout_65 = QVBoxLayout()
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.label_27 = QLabel(self.tab_5)
        self.label_27.setObjectName(u"label_27")
        sizePolicy20 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy20.setHorizontalStretch(0)
        sizePolicy20.setVerticalStretch(0)
        sizePolicy20.setHeightForWidth(self.label_27.sizePolicy().hasHeightForWidth())
        self.label_27.setSizePolicy(sizePolicy20)
        self.label_27.setFont(font2)

        self.verticalLayout_65.addWidget(self.label_27)

        self.tel1_os = QLineEdit(self.tab_5)
        self.tel1_os.setObjectName(u"tel1_os")
        sizePolicy11.setHeightForWidth(self.tel1_os.sizePolicy().hasHeightForWidth())
        self.tel1_os.setSizePolicy(sizePolicy11)
        self.tel1_os.setMinimumSize(QSize(200, 30))
        self.tel1_os.setFont(font2)

        self.verticalLayout_65.addWidget(self.tel1_os, 0, Qt.AlignLeft)


        self.horizontalLayout_13.addLayout(self.verticalLayout_65)

        self.verticalLayout_66 = QVBoxLayout()
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.label_37 = QLabel(self.tab_5)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font2)

        self.verticalLayout_66.addWidget(self.label_37)

        self.tel2_os = QLineEdit(self.tab_5)
        self.tel2_os.setObjectName(u"tel2_os")
        sizePolicy11.setHeightForWidth(self.tel2_os.sizePolicy().hasHeightForWidth())
        self.tel2_os.setSizePolicy(sizePolicy11)
        self.tel2_os.setMinimumSize(QSize(200, 30))
        self.tel2_os.setFont(font2)

        self.verticalLayout_66.addWidget(self.tel2_os, 0, Qt.AlignLeft)


        self.horizontalLayout_13.addLayout(self.verticalLayout_66)


        self.verticalLayout_64.addLayout(self.horizontalLayout_13)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.verticalLayout_67 = QVBoxLayout()
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.label_38 = QLabel(self.tab_5)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font2)

        self.verticalLayout_67.addWidget(self.label_38)

        self.email_os = QLineEdit(self.tab_5)
        self.email_os.setObjectName(u"email_os")
        sizePolicy11.setHeightForWidth(self.email_os.sizePolicy().hasHeightForWidth())
        self.email_os.setSizePolicy(sizePolicy11)
        self.email_os.setMinimumSize(QSize(300, 30))
        self.email_os.setFont(font2)

        self.verticalLayout_67.addWidget(self.email_os, 0, Qt.AlignLeft)


        self.horizontalLayout_14.addLayout(self.verticalLayout_67)

        self.verticalLayout_68 = QVBoxLayout()
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.label_39 = QLabel(self.tab_5)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font2)

        self.verticalLayout_68.addWidget(self.label_39)

        self.cpf_os = QLineEdit(self.tab_5)
        self.cpf_os.setObjectName(u"cpf_os")
        sizePolicy11.setHeightForWidth(self.cpf_os.sizePolicy().hasHeightForWidth())
        self.cpf_os.setSizePolicy(sizePolicy11)
        self.cpf_os.setMinimumSize(QSize(300, 30))
        self.cpf_os.setFont(font2)

        self.verticalLayout_68.addWidget(self.cpf_os, 0, Qt.AlignLeft)


        self.horizontalLayout_14.addLayout(self.verticalLayout_68)


        self.verticalLayout_64.addLayout(self.horizontalLayout_14)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.verticalLayout_69 = QVBoxLayout()
        self.verticalLayout_69.setObjectName(u"verticalLayout_69")
        self.label_48 = QLabel(self.tab_5)
        self.label_48.setObjectName(u"label_48")
        sizePolicy.setHeightForWidth(self.label_48.sizePolicy().hasHeightForWidth())
        self.label_48.setSizePolicy(sizePolicy)
        self.label_48.setFont(font2)

        self.verticalLayout_69.addWidget(self.label_48)

        self.brr_os = QLineEdit(self.tab_5)
        self.brr_os.setObjectName(u"brr_os")
        sizePolicy11.setHeightForWidth(self.brr_os.sizePolicy().hasHeightForWidth())
        self.brr_os.setSizePolicy(sizePolicy11)
        self.brr_os.setMinimumSize(QSize(300, 30))
        self.brr_os.setFont(font2)

        self.verticalLayout_69.addWidget(self.brr_os, 0, Qt.AlignLeft)


        self.horizontalLayout_15.addLayout(self.verticalLayout_69)

        self.verticalLayout_70 = QVBoxLayout()
        self.verticalLayout_70.setObjectName(u"verticalLayout_70")
        self.label_50 = QLabel(self.tab_5)
        self.label_50.setObjectName(u"label_50")
        sizePolicy.setHeightForWidth(self.label_50.sizePolicy().hasHeightForWidth())
        self.label_50.setSizePolicy(sizePolicy)
        self.label_50.setFont(font2)

        self.verticalLayout_70.addWidget(self.label_50)

        self.cdd_os = QLineEdit(self.tab_5)
        self.cdd_os.setObjectName(u"cdd_os")
        sizePolicy11.setHeightForWidth(self.cdd_os.sizePolicy().hasHeightForWidth())
        self.cdd_os.setSizePolicy(sizePolicy11)
        self.cdd_os.setMinimumSize(QSize(300, 30))
        self.cdd_os.setFont(font2)

        self.verticalLayout_70.addWidget(self.cdd_os, 0, Qt.AlignLeft)


        self.horizontalLayout_15.addLayout(self.verticalLayout_70)


        self.verticalLayout_64.addLayout(self.horizontalLayout_15)

        self.verticalLayout_71 = QVBoxLayout()
        self.verticalLayout_71.setObjectName(u"verticalLayout_71")
        self.check_obs = QCheckBox(self.tab_5)
        self.check_obs.setObjectName(u"check_obs")
        self.check_obs.setFont(font8)

        self.verticalLayout_71.addWidget(self.check_obs)

        self.obs_os = QTextEdit(self.tab_5)
        self.obs_os.setObjectName(u"obs_os")
        sizePolicy10.setHeightForWidth(self.obs_os.sizePolicy().hasHeightForWidth())
        self.obs_os.setSizePolicy(sizePolicy10)
        self.obs_os.setMinimumSize(QSize(800, 0))
        self.obs_os.setFont(font4)

        self.verticalLayout_71.addWidget(self.obs_os)

        self.verticalSpacer_5 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_71.addItem(self.verticalSpacer_5)

        self.verticalLayout_72 = QVBoxLayout()
        self.verticalLayout_72.setObjectName(u"verticalLayout_72")
        self.horizontalLayout_49 = QHBoxLayout()
        self.horizontalLayout_49.setObjectName(u"horizontalLayout_49")
        self.check_aprove = QCheckBox(self.tab_5)
        self.check_aprove.setObjectName(u"check_aprove")
        sizePolicy10.setHeightForWidth(self.check_aprove.sizePolicy().hasHeightForWidth())
        self.check_aprove.setSizePolicy(sizePolicy10)
        self.check_aprove.setFont(font1)
        self.check_aprove.setChecked(False)

        self.horizontalLayout_49.addWidget(self.check_aprove, 0, Qt.AlignRight)

        self.date_aprove = QDateEdit(self.tab_5)
        self.date_aprove.setObjectName(u"date_aprove")
        sizePolicy10.setHeightForWidth(self.date_aprove.sizePolicy().hasHeightForWidth())
        self.date_aprove.setSizePolicy(sizePolicy10)
        self.date_aprove.setMinimumSize(QSize(120, 40))
        self.date_aprove.setFont(font2)
        self.date_aprove.setWrapping(False)
        self.date_aprove.setFrame(True)
        self.date_aprove.setReadOnly(False)
        self.date_aprove.setProperty("showGroupSeparator", False)
        self.date_aprove.setCalendarPopup(True)
        self.date_aprove.setTimeSpec(Qt.LocalTime)

        self.horizontalLayout_49.addWidget(self.date_aprove, 0, Qt.AlignLeft)

        self.horizontalSpacer_26 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_49.addItem(self.horizontalSpacer_26)


        self.verticalLayout_72.addLayout(self.horizontalLayout_49)

        self.horizontalLayout_50 = QHBoxLayout()
        self.horizontalLayout_50.setObjectName(u"horizontalLayout_50")
        self.check_delivery = QCheckBox(self.tab_5)
        self.check_delivery.setObjectName(u"check_delivery")
        sizePolicy10.setHeightForWidth(self.check_delivery.sizePolicy().hasHeightForWidth())
        self.check_delivery.setSizePolicy(sizePolicy10)
        self.check_delivery.setFont(font1)
        self.check_delivery.setChecked(False)

        self.horizontalLayout_50.addWidget(self.check_delivery, 0, Qt.AlignRight)

        self.date_delivery = QDateEdit(self.tab_5)
        self.date_delivery.setObjectName(u"date_delivery")
        sizePolicy10.setHeightForWidth(self.date_delivery.sizePolicy().hasHeightForWidth())
        self.date_delivery.setSizePolicy(sizePolicy10)
        self.date_delivery.setMinimumSize(QSize(120, 40))
        self.date_delivery.setFont(font2)
        self.date_delivery.setCalendarPopup(True)

        self.horizontalLayout_50.addWidget(self.date_delivery, 0, Qt.AlignLeft)

        self.horizontalSpacer_27 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_50.addItem(self.horizontalSpacer_27)


        self.verticalLayout_72.addLayout(self.horizontalLayout_50)


        self.verticalLayout_71.addLayout(self.verticalLayout_72)


        self.verticalLayout_64.addLayout(self.verticalLayout_71)


        self.verticalLayout_58.addLayout(self.verticalLayout_64)


        self.verticalLayout_8.addLayout(self.verticalLayout_58)


        self.horizontalLayout_16.addLayout(self.verticalLayout_8)

        self.verticalLayout_75 = QVBoxLayout()
        self.verticalLayout_75.setSpacing(29)
        self.verticalLayout_75.setObjectName(u"verticalLayout_75")
        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.verticalLayout_75.addItem(self.horizontalSpacer_7)

        self.horizontalLayout_51 = QHBoxLayout()
        self.horizontalLayout_51.setObjectName(u"horizontalLayout_51")
        self.save_client_os = QPushButton(self.tab_5)
        self.save_client_os.setObjectName(u"save_client_os")
        sizePolicy10.setHeightForWidth(self.save_client_os.sizePolicy().hasHeightForWidth())
        self.save_client_os.setSizePolicy(sizePolicy10)
        self.save_client_os.setMinimumSize(QSize(150, 40))
        self.save_client_os.setFont(font2)
        self.save_client_os.setIcon(icon7)
        self.save_client_os.setIconSize(QSize(40, 40))

        self.horizontalLayout_51.addWidget(self.save_client_os, 0, Qt.AlignBottom)

        self.cancel_client_os = QPushButton(self.tab_5)
        self.cancel_client_os.setObjectName(u"cancel_client_os")
        sizePolicy10.setHeightForWidth(self.cancel_client_os.sizePolicy().hasHeightForWidth())
        self.cancel_client_os.setSizePolicy(sizePolicy10)
        self.cancel_client_os.setMinimumSize(QSize(150, 40))
        self.cancel_client_os.setFont(font2)
        self.cancel_client_os.setIcon(icon11)
        self.cancel_client_os.setIconSize(QSize(32, 32))

        self.horizontalLayout_51.addWidget(self.cancel_client_os, 0, Qt.AlignBottom)

        self.back_os_2 = QPushButton(self.tab_5)
        self.back_os_2.setObjectName(u"back_os_2")
        sizePolicy10.setHeightForWidth(self.back_os_2.sizePolicy().hasHeightForWidth())
        self.back_os_2.setSizePolicy(sizePolicy10)
        self.back_os_2.setMinimumSize(QSize(150, 40))
        self.back_os_2.setFont(font2)
        self.back_os_2.setIcon(icon10)
        self.back_os_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_51.addWidget(self.back_os_2, 0, Qt.AlignBottom)

        self.next = QPushButton(self.tab_5)
        self.next.setObjectName(u"next")
        sizePolicy10.setHeightForWidth(self.next.sizePolicy().hasHeightForWidth())
        self.next.setSizePolicy(sizePolicy10)
        self.next.setMinimumSize(QSize(150, 40))
        self.next.setFont(font2)
        icon20 = QIcon()
        icon20.addFile(u":/Icons/next.png", QSize(), QIcon.Normal, QIcon.Off)
        self.next.setIcon(icon20)
        self.next.setIconSize(QSize(32, 32))

        self.horizontalLayout_51.addWidget(self.next, 0, Qt.AlignBottom)


        self.verticalLayout_75.addLayout(self.horizontalLayout_51)


        self.horizontalLayout_16.addLayout(self.verticalLayout_75)

        self.tab_os.addTab(self.tab_5, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.verticalLayout_54 = QVBoxLayout(self.tab_4)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.horizontalLayout_40.setContentsMargins(-1, -1, -1, 0)
        self.verticalLayout_48 = QVBoxLayout()
        self.verticalLayout_48.setSpacing(0)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_48.setContentsMargins(-1, 0, -1, 0)
        self.label_51 = QLabel(self.tab_4)
        self.label_51.setObjectName(u"label_51")
        sizePolicy5.setHeightForWidth(self.label_51.sizePolicy().hasHeightForWidth())
        self.label_51.setSizePolicy(sizePolicy5)
        self.label_51.setMinimumSize(QSize(30, 0))

        self.verticalLayout_48.addWidget(self.label_51)

        self.search_product_2 = QLineEdit(self.tab_4)
        self.search_product_2.setObjectName(u"search_product_2")
        sizePolicy10.setHeightForWidth(self.search_product_2.sizePolicy().hasHeightForWidth())
        self.search_product_2.setSizePolicy(sizePolicy10)
        self.search_product_2.setMinimumSize(QSize(60, 40))
        self.search_product_2.setMaximumSize(QSize(60, 40))
        self.search_product_2.setFont(font4)

        self.verticalLayout_48.addWidget(self.search_product_2)


        self.horizontalLayout_40.addLayout(self.verticalLayout_48)

        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_84 = QLabel(self.tab_4)
        self.label_84.setObjectName(u"label_84")
        sizePolicy5.setHeightForWidth(self.label_84.sizePolicy().hasHeightForWidth())
        self.label_84.setSizePolicy(sizePolicy5)
        self.label_84.setMinimumSize(QSize(30, 0))

        self.verticalLayout_49.addWidget(self.label_84)

        self.nm_produto = QLineEdit(self.tab_4)
        self.nm_produto.setObjectName(u"nm_produto")
        sizePolicy18.setHeightForWidth(self.nm_produto.sizePolicy().hasHeightForWidth())
        self.nm_produto.setSizePolicy(sizePolicy18)
        self.nm_produto.setMinimumSize(QSize(240, 40))
        self.nm_produto.setMaximumSize(QSize(16777215, 60))
        self.nm_produto.setFont(font4)
        self.nm_produto.setReadOnly(True)

        self.verticalLayout_49.addWidget(self.nm_produto)


        self.horizontalLayout_40.addLayout(self.verticalLayout_49)

        self.verticalLayout_50 = QVBoxLayout()
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.label_85 = QLabel(self.tab_4)
        self.label_85.setObjectName(u"label_85")
        sizePolicy5.setHeightForWidth(self.label_85.sizePolicy().hasHeightForWidth())
        self.label_85.setSizePolicy(sizePolicy5)
        self.label_85.setMinimumSize(QSize(30, 0))
        self.label_85.setFont(font3)
        self.label_85.setAlignment(Qt.AlignCenter)
        self.label_85.setMargin(-4)

        self.verticalLayout_50.addWidget(self.label_85, 0, Qt.AlignLeft)

        self.qt = QSpinBox(self.tab_4)
        self.qt.setObjectName(u"qt")
        sizePolicy10.setHeightForWidth(self.qt.sizePolicy().hasHeightForWidth())
        self.qt.setSizePolicy(sizePolicy10)
        self.qt.setMinimumSize(QSize(80, 40))
        self.qt.setFont(font4)
        self.qt.setAlignment(Qt.AlignCenter)
        self.qt.setValue(1)

        self.verticalLayout_50.addWidget(self.qt, 0, Qt.AlignLeft)


        self.horizontalLayout_40.addLayout(self.verticalLayout_50)

        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setSpacing(7)
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.label_86 = QLabel(self.tab_4)
        self.label_86.setObjectName(u"label_86")
        sizePolicy5.setHeightForWidth(self.label_86.sizePolicy().hasHeightForWidth())
        self.label_86.setSizePolicy(sizePolicy5)
        self.label_86.setMinimumSize(QSize(30, 0))
        self.label_86.setMaximumSize(QSize(16777215, 19))
        self.label_86.setAlignment(Qt.AlignCenter)

        self.verticalLayout_51.addWidget(self.label_86, 0, Qt.AlignLeft)

        self.largura = QDoubleSpinBox(self.tab_4)
        self.largura.setObjectName(u"largura")
        self.largura.setEnabled(True)
        sizePolicy10.setHeightForWidth(self.largura.sizePolicy().hasHeightForWidth())
        self.largura.setSizePolicy(sizePolicy10)
        self.largura.setMinimumSize(QSize(80, 40))
        self.largura.setFont(font4)

        self.verticalLayout_51.addWidget(self.largura)


        self.horizontalLayout_40.addLayout(self.verticalLayout_51)

        self.verticalLayout_52 = QVBoxLayout()
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.label_78 = QLabel(self.tab_4)
        self.label_78.setObjectName(u"label_78")
        sizePolicy5.setHeightForWidth(self.label_78.sizePolicy().hasHeightForWidth())
        self.label_78.setSizePolicy(sizePolicy5)
        self.label_78.setMinimumSize(QSize(30, 0))
        self.label_78.setMaximumSize(QSize(16777215, 20))
        self.label_78.setAlignment(Qt.AlignCenter)
        self.label_78.setMargin(0)
        self.label_78.setIndent(-1)

        self.verticalLayout_52.addWidget(self.label_78, 0, Qt.AlignLeft)

        self.altura = QDoubleSpinBox(self.tab_4)
        self.altura.setObjectName(u"altura")
        sizePolicy10.setHeightForWidth(self.altura.sizePolicy().hasHeightForWidth())
        self.altura.setSizePolicy(sizePolicy10)
        self.altura.setMinimumSize(QSize(80, 40))
        self.altura.setFont(font4)

        self.verticalLayout_52.addWidget(self.altura)


        self.horizontalLayout_40.addLayout(self.verticalLayout_52)

        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_83 = QLabel(self.tab_4)
        self.label_83.setObjectName(u"label_83")
        sizePolicy5.setHeightForWidth(self.label_83.sizePolicy().hasHeightForWidth())
        self.label_83.setSizePolicy(sizePolicy5)
        self.label_83.setMinimumSize(QSize(50, 0))
        self.label_83.setMaximumSize(QSize(16777215, 20))
        self.label_83.setSizeIncrement(QSize(0, 0))
        self.label_83.setBaseSize(QSize(0, 0))
        self.label_83.setAlignment(Qt.AlignCenter)
        self.label_83.setMargin(0)

        self.verticalLayout_53.addWidget(self.label_83, 0, Qt.AlignLeft)

        self.comp = QDoubleSpinBox(self.tab_4)
        self.comp.setObjectName(u"comp")
        sizePolicy10.setHeightForWidth(self.comp.sizePolicy().hasHeightForWidth())
        self.comp.setSizePolicy(sizePolicy10)
        self.comp.setMinimumSize(QSize(100, 40))
        self.comp.setFont(font4)

        self.verticalLayout_53.addWidget(self.comp)


        self.horizontalLayout_40.addLayout(self.verticalLayout_53)

        self.horizontalLayout_39 = QHBoxLayout()
        self.horizontalLayout_39.setSpacing(0)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_39.setContentsMargins(-1, -1, -1, 0)
        self.insert_product = QPushButton(self.tab_4)
        self.insert_product.setObjectName(u"insert_product")
        sizePolicy1.setHeightForWidth(self.insert_product.sizePolicy().hasHeightForWidth())
        self.insert_product.setSizePolicy(sizePolicy1)
        self.insert_product.setMinimumSize(QSize(90, 0))
        self.insert_product.setFont(font2)
        icon21 = QIcon()
        icon21.addFile(u":/Icons/add.png", QSize(), QIcon.Normal, QIcon.Off)
        self.insert_product.setIcon(icon21)
        self.insert_product.setIconSize(QSize(32, 32))

        self.horizontalLayout_39.addWidget(self.insert_product)

        self.remove_product = QPushButton(self.tab_4)
        self.remove_product.setObjectName(u"remove_product")
        sizePolicy1.setHeightForWidth(self.remove_product.sizePolicy().hasHeightForWidth())
        self.remove_product.setSizePolicy(sizePolicy1)
        self.remove_product.setMinimumSize(QSize(90, 0))
        self.remove_product.setFont(font2)
        self.remove_product.setIcon(icon9)
        self.remove_product.setIconSize(QSize(32, 32))

        self.horizontalLayout_39.addWidget(self.remove_product)

        self.cancel_os = QPushButton(self.tab_4)
        self.cancel_os.setObjectName(u"cancel_os")
        self.cancel_os.setMinimumSize(QSize(90, 0))
        self.cancel_os.setFont(font2)
        self.cancel_os.setIcon(icon11)
        self.cancel_os.setIconSize(QSize(32, 32))

        self.horizontalLayout_39.addWidget(self.cancel_os)

        self.back_os = QPushButton(self.tab_4)
        self.back_os.setObjectName(u"back_os")
        self.back_os.setMinimumSize(QSize(90, 0))
        self.back_os.setIcon(icon10)
        self.back_os.setIconSize(QSize(32, 32))

        self.horizontalLayout_39.addWidget(self.back_os)


        self.horizontalLayout_40.addLayout(self.horizontalLayout_39)


        self.verticalLayout_54.addLayout(self.horizontalLayout_40)

        self.table_add_os = QTableWidget(self.tab_4)
        if (self.table_add_os.columnCount() < 7):
            self.table_add_os.setColumnCount(7)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.table_add_os.setHorizontalHeaderItem(0, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.table_add_os.setHorizontalHeaderItem(1, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.table_add_os.setHorizontalHeaderItem(2, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.table_add_os.setHorizontalHeaderItem(3, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        self.table_add_os.setHorizontalHeaderItem(4, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        self.table_add_os.setHorizontalHeaderItem(5, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.table_add_os.setHorizontalHeaderItem(6, __qtablewidgetitem49)
        self.table_add_os.setObjectName(u"table_add_os")
        sizePolicy21 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy21.setHorizontalStretch(0)
        sizePolicy21.setVerticalStretch(0)
        sizePolicy21.setHeightForWidth(self.table_add_os.sizePolicy().hasHeightForWidth())
        self.table_add_os.setSizePolicy(sizePolicy21)
        self.table_add_os.setRowCount(0)
        self.table_add_os.horizontalHeader().setMinimumSectionSize(200)
        self.table_add_os.horizontalHeader().setDefaultSectionSize(200)
        self.table_add_os.horizontalHeader().setStretchLastSection(True)
        self.table_add_os.verticalHeader().setVisible(False)
        self.table_add_os.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_54.addWidget(self.table_add_os)

        self.tab_os.addTab(self.tab_4, "")

        self.gridLayout_8.addWidget(self.tab_os, 0, 0, 1, 4)


        self.verticalLayout_47.addWidget(self.frame_14)

        self.pages.addWidget(self.add_os)
        self.alter_pdf = QWidget()
        self.alter_pdf.setObjectName(u"alter_pdf")
        self.verticalLayout_76 = QVBoxLayout(self.alter_pdf)
        self.verticalLayout_76.setObjectName(u"verticalLayout_76")
        self.frame_9 = QFrame(self.alter_pdf)
        self.frame_9.setObjectName(u"frame_9")
        sizePolicy7.setHeightForWidth(self.frame_9.sizePolicy().hasHeightForWidth())
        self.frame_9.setSizePolicy(sizePolicy7)
        self.frame_9.setMinimumSize(QSize(800, 600))
        self.frame_9.setStyleSheet(u"background-color: rgb(54, 54, 54);")
        self.frame_9.setFrameShape(QFrame.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Raised)
        self.verticalLayout_77 = QVBoxLayout(self.frame_9)
        self.verticalLayout_77.setObjectName(u"verticalLayout_77")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_67 = QLabel(self.frame_9)
        self.label_67.setObjectName(u"label_67")
        sizePolicy9.setHeightForWidth(self.label_67.sizePolicy().hasHeightForWidth())
        self.label_67.setSizePolicy(sizePolicy9)
        self.label_67.setFont(font2)

        self.verticalLayout_36.addWidget(self.label_67)

        self.nome_pdf = QLineEdit(self.frame_9)
        self.nome_pdf.setObjectName(u"nome_pdf")
        self.nome_pdf.setEnabled(False)
        sizePolicy10.setHeightForWidth(self.nome_pdf.sizePolicy().hasHeightForWidth())
        self.nome_pdf.setSizePolicy(sizePolicy10)
        self.nome_pdf.setMinimumSize(QSize(400, 30))
        self.nome_pdf.setFont(font2)
        self.nome_pdf.setReadOnly(False)

        self.verticalLayout_36.addWidget(self.nome_pdf)


        self.verticalLayout_26.addLayout(self.verticalLayout_36)

        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_68 = QLabel(self.frame_9)
        self.label_68.setObjectName(u"label_68")
        sizePolicy9.setHeightForWidth(self.label_68.sizePolicy().hasHeightForWidth())
        self.label_68.setSizePolicy(sizePolicy9)
        self.label_68.setFont(font2)

        self.verticalLayout_42.addWidget(self.label_68)

        self.cpf_pdf = QLineEdit(self.frame_9)
        self.cpf_pdf.setObjectName(u"cpf_pdf")
        self.cpf_pdf.setEnabled(False)
        sizePolicy10.setHeightForWidth(self.cpf_pdf.sizePolicy().hasHeightForWidth())
        self.cpf_pdf.setSizePolicy(sizePolicy10)
        self.cpf_pdf.setMinimumSize(QSize(400, 30))
        self.cpf_pdf.setFont(font2)

        self.verticalLayout_42.addWidget(self.cpf_pdf)


        self.verticalLayout_26.addLayout(self.verticalLayout_42)

        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.label_69 = QLabel(self.frame_9)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setFont(font2)

        self.horizontalLayout_46.addWidget(self.label_69)


        self.verticalLayout_44.addLayout(self.horizontalLayout_46)

        self.horizontalLayout_60 = QHBoxLayout()
        self.horizontalLayout_60.setObjectName(u"horizontalLayout_60")
        self.end_pdf = QLineEdit(self.frame_9)
        self.end_pdf.setObjectName(u"end_pdf")
        self.end_pdf.setEnabled(False)
        sizePolicy5.setHeightForWidth(self.end_pdf.sizePolicy().hasHeightForWidth())
        self.end_pdf.setSizePolicy(sizePolicy5)
        self.end_pdf.setMinimumSize(QSize(200, 30))
        self.end_pdf.setFont(font2)

        self.horizontalLayout_60.addWidget(self.end_pdf)


        self.verticalLayout_44.addLayout(self.horizontalLayout_60)


        self.verticalLayout_26.addLayout(self.verticalLayout_44)

        self.verticalLayout_73 = QVBoxLayout()
        self.verticalLayout_73.setObjectName(u"verticalLayout_73")
        self.horizontalLayout_61 = QHBoxLayout()
        self.horizontalLayout_61.setObjectName(u"horizontalLayout_61")
        self.label_70 = QLabel(self.frame_9)
        self.label_70.setObjectName(u"label_70")
        self.label_70.setFont(font2)

        self.horizontalLayout_61.addWidget(self.label_70)

        self.horizontalSpacer_9 = QSpacerItem(161, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_9)

        self.label_71 = QLabel(self.frame_9)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font2)

        self.horizontalLayout_61.addWidget(self.label_71)

        self.horizontalSpacer_24 = QSpacerItem(154, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_24)

        self.label_72 = QLabel(self.frame_9)
        self.label_72.setObjectName(u"label_72")
        self.label_72.setFont(font2)

        self.horizontalLayout_61.addWidget(self.label_72)

        self.horizontalSpacer_25 = QSpacerItem(20, 20, QSizePolicy.Fixed, QSizePolicy.Minimum)

        self.horizontalLayout_61.addItem(self.horizontalSpacer_25)

        self.label_73 = QLabel(self.frame_9)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font2)

        self.horizontalLayout_61.addWidget(self.label_73)


        self.verticalLayout_73.addLayout(self.horizontalLayout_61)

        self.horizontalLayout_62 = QHBoxLayout()
        self.horizontalLayout_62.setObjectName(u"horizontalLayout_62")
        self.brr_pdf = QLineEdit(self.frame_9)
        self.brr_pdf.setObjectName(u"brr_pdf")
        self.brr_pdf.setEnabled(False)
        sizePolicy10.setHeightForWidth(self.brr_pdf.sizePolicy().hasHeightForWidth())
        self.brr_pdf.setSizePolicy(sizePolicy10)
        self.brr_pdf.setMinimumSize(QSize(300, 30))
        self.brr_pdf.setFont(font2)

        self.horizontalLayout_62.addWidget(self.brr_pdf)

        self.cdd_pdf = QLineEdit(self.frame_9)
        self.cdd_pdf.setObjectName(u"cdd_pdf")
        self.cdd_pdf.setEnabled(False)
        sizePolicy11.setHeightForWidth(self.cdd_pdf.sizePolicy().hasHeightForWidth())
        self.cdd_pdf.setSizePolicy(sizePolicy11)
        self.cdd_pdf.setMinimumSize(QSize(300, 30))
        self.cdd_pdf.setFont(font2)

        self.horizontalLayout_62.addWidget(self.cdd_pdf)

        self.uf = QLineEdit(self.frame_9)
        self.uf.setObjectName(u"uf")
        self.uf.setEnabled(False)
        sizePolicy10.setHeightForWidth(self.uf.sizePolicy().hasHeightForWidth())
        self.uf.setSizePolicy(sizePolicy10)
        self.uf.setMinimumSize(QSize(40, 30))
        self.uf.setFont(font2)

        self.horizontalLayout_62.addWidget(self.uf)

        self.cep = QLineEdit(self.frame_9)
        self.cep.setObjectName(u"cep")
        self.cep.setEnabled(False)
        sizePolicy10.setHeightForWidth(self.cep.sizePolicy().hasHeightForWidth())
        self.cep.setSizePolicy(sizePolicy10)
        self.cep.setMinimumSize(QSize(40, 30))
        self.cep.setFont(font2)

        self.horizontalLayout_62.addWidget(self.cep)


        self.verticalLayout_73.addLayout(self.horizontalLayout_62)


        self.verticalLayout_26.addLayout(self.verticalLayout_73)

        self.verticalLayout_74 = QVBoxLayout()
        self.verticalLayout_74.setObjectName(u"verticalLayout_74")
        self.horizontalLayout_63 = QHBoxLayout()
        self.horizontalLayout_63.setObjectName(u"horizontalLayout_63")
        self.label_74 = QLabel(self.frame_9)
        self.label_74.setObjectName(u"label_74")
        sizePolicy.setHeightForWidth(self.label_74.sizePolicy().hasHeightForWidth())
        self.label_74.setSizePolicy(sizePolicy)
        self.label_74.setFont(font2)

        self.horizontalLayout_63.addWidget(self.label_74)

        self.label_75 = QLabel(self.frame_9)
        self.label_75.setObjectName(u"label_75")
        sizePolicy.setHeightForWidth(self.label_75.sizePolicy().hasHeightForWidth())
        self.label_75.setSizePolicy(sizePolicy)
        self.label_75.setFont(font2)

        self.horizontalLayout_63.addWidget(self.label_75)

        self.label_76 = QLabel(self.frame_9)
        self.label_76.setObjectName(u"label_76")
        sizePolicy.setHeightForWidth(self.label_76.sizePolicy().hasHeightForWidth())
        self.label_76.setSizePolicy(sizePolicy)
        self.label_76.setFont(font2)

        self.horizontalLayout_63.addWidget(self.label_76)


        self.verticalLayout_74.addLayout(self.horizontalLayout_63)

        self.horizontalLayout_64 = QHBoxLayout()
        self.horizontalLayout_64.setObjectName(u"horizontalLayout_64")
        self.tel1_pdf = QLineEdit(self.frame_9)
        self.tel1_pdf.setObjectName(u"tel1_pdf")
        self.tel1_pdf.setEnabled(False)
        sizePolicy10.setHeightForWidth(self.tel1_pdf.sizePolicy().hasHeightForWidth())
        self.tel1_pdf.setSizePolicy(sizePolicy10)
        self.tel1_pdf.setMinimumSize(QSize(300, 30))
        self.tel1_pdf.setFont(font2)

        self.horizontalLayout_64.addWidget(self.tel1_pdf)

        self.tel2_pdf = QLineEdit(self.frame_9)
        self.tel2_pdf.setObjectName(u"tel2_pdf")
        self.tel2_pdf.setEnabled(False)
        sizePolicy10.setHeightForWidth(self.tel2_pdf.sizePolicy().hasHeightForWidth())
        self.tel2_pdf.setSizePolicy(sizePolicy10)
        self.tel2_pdf.setMinimumSize(QSize(300, 30))
        self.tel2_pdf.setFont(font2)

        self.horizontalLayout_64.addWidget(self.tel2_pdf)

        self.email_pdf = QLineEdit(self.frame_9)
        self.email_pdf.setObjectName(u"email_pdf")
        self.email_pdf.setEnabled(False)
        sizePolicy10.setHeightForWidth(self.email_pdf.sizePolicy().hasHeightForWidth())
        self.email_pdf.setSizePolicy(sizePolicy10)
        self.email_pdf.setMinimumSize(QSize(300, 30))
        self.email_pdf.setFont(font2)

        self.horizontalLayout_64.addWidget(self.email_pdf)


        self.verticalLayout_74.addLayout(self.horizontalLayout_64)


        self.verticalLayout_26.addLayout(self.verticalLayout_74)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_26.addItem(self.verticalSpacer_2)

        self.horizontalLayout_65 = QHBoxLayout()
        self.horizontalLayout_65.setObjectName(u"horizontalLayout_65")
        self.cancel_pdf = QPushButton(self.frame_9)
        self.cancel_pdf.setObjectName(u"cancel_pdf")
        sizePolicy12.setHeightForWidth(self.cancel_pdf.sizePolicy().hasHeightForWidth())
        self.cancel_pdf.setSizePolicy(sizePolicy12)
        self.cancel_pdf.setMinimumSize(QSize(150, 70))
        self.cancel_pdf.setFont(font2)
        self.cancel_pdf.setIcon(icon11)
        self.cancel_pdf.setIconSize(QSize(32, 32))

        self.horizontalLayout_65.addWidget(self.cancel_pdf)

        self.back_13 = QPushButton(self.frame_9)
        self.back_13.setObjectName(u"back_13")
        sizePolicy12.setHeightForWidth(self.back_13.sizePolicy().hasHeightForWidth())
        self.back_13.setSizePolicy(sizePolicy12)
        self.back_13.setMinimumSize(QSize(150, 70))
        self.back_13.setFont(font2)
        self.back_13.setIcon(icon10)
        self.back_13.setIconSize(QSize(32, 32))

        self.horizontalLayout_65.addWidget(self.back_13)

        self.alter_pdf_2 = QPushButton(self.frame_9)
        self.alter_pdf_2.setObjectName(u"alter_pdf_2")

        self.horizontalLayout_65.addWidget(self.alter_pdf_2)

        self.edit_pdf_2 = QPushButton(self.frame_9)
        self.edit_pdf_2.setObjectName(u"edit_pdf_2")
        sizePolicy12.setHeightForWidth(self.edit_pdf_2.sizePolicy().hasHeightForWidth())
        self.edit_pdf_2.setSizePolicy(sizePolicy12)
        self.edit_pdf_2.setMinimumSize(QSize(150, 70))
        self.edit_pdf_2.setFont(font2)
        self.edit_pdf_2.setIcon(icon8)
        self.edit_pdf_2.setIconSize(QSize(32, 32))

        self.horizontalLayout_65.addWidget(self.edit_pdf_2)


        self.verticalLayout_26.addLayout(self.horizontalLayout_65)


        self.verticalLayout_77.addLayout(self.verticalLayout_26)


        self.verticalLayout_76.addWidget(self.frame_9, 0, Qt.AlignHCenter)

        self.pages.addWidget(self.alter_pdf)

        self.verticalLayout_2.addWidget(self.pages)


        self.verticalLayout.addLayout(self.verticalLayout_2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menuBar = QMenuBar(MainWindow)
        self.menuBar.setObjectName(u"menuBar")
        self.menuBar.setGeometry(QRect(0, 0, 1672, 21))
        self.menuCONFIG = QMenu(self.menuBar)
        self.menuCONFIG.setObjectName(u"menuCONFIG")
        self.menuAJUDA = QMenu(self.menuBar)
        self.menuAJUDA.setObjectName(u"menuAJUDA")
        self.menuSOBRE = QMenu(self.menuBar)
        self.menuSOBRE.setObjectName(u"menuSOBRE")
        MainWindow.setMenuBar(self.menuBar)

        self.menuBar.addAction(self.menuCONFIG.menuAction())
        self.menuBar.addAction(self.menuAJUDA.menuAction())
        self.menuBar.addAction(self.menuSOBRE.menuAction())
        self.menuCONFIG.addAction(self.change_pdf)

        self.retranslateUi(MainWindow)

        self.pages.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.tab_os.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SOFTWARE VIDRA\u00c7ARIA", None))
        self.change_pdf.setText(QCoreApplication.translate("MainWindow", u"Editar PDF", None))
        self.actionAlterar_Estilo.setText(QCoreApplication.translate("MainWindow", u"Alterar Estilo", None))
        self.client.setText("")
        self.task.setText("")
        self.cashier_2.setText("")
        self.product.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"Pesquisar Cliente", None))
        self.new_client.setText("")
        self.edit_client.setText("")
        self.delete_client.setText("")
        self.back_1.setText("")
        ___qtablewidgetitem = self.table_Cliente.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem1 = self.table_Cliente.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem2 = self.table_Cliente.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Tel1", None));
        ___qtablewidgetitem3 = self.table_Cliente.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Tel2", None));
        ___qtablewidgetitem4 = self.table_Cliente.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem5 = self.table_Cliente.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"Bairro", None));
        ___qtablewidgetitem6 = self.table_Cliente.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Cidade", None));
        ___qtablewidgetitem7 = self.table_Cliente.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem8 = self.table_Cliente.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"CPF", None));
        ___qtablewidgetitem9 = self.table_Cliente.horizontalHeaderItem(9)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem10 = self.table_Cliente.horizontalHeaderItem(10)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7ao", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Pesquisar Fornecedor", None))
        self.new_provider.setText("")
        self.edit_provider.setText("")
        self.delete_provider.setText("")
        self.back_3.setText("")
        ___qtablewidgetitem11 = self.table_fornecedor.horizontalHeaderItem(0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem12 = self.table_fornecedor.horizontalHeaderItem(1)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem13 = self.table_fornecedor.horizontalHeaderItem(2)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Tel1", None));
        ___qtablewidgetitem14 = self.table_fornecedor.horizontalHeaderItem(3)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"Tel2", None));
        ___qtablewidgetitem15 = self.table_fornecedor.horizontalHeaderItem(4)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem16 = self.table_fornecedor.horizontalHeaderItem(5)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"Complemento", None));
        ___qtablewidgetitem17 = self.table_fornecedor.horizontalHeaderItem(6)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Email", None));
        ___qtablewidgetitem18 = self.table_fornecedor.horizontalHeaderItem(7)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Pesquisar Agenda", None))
        self.new_task.setText("")
        self.edit_task.setText("")
        self.delete_task.setText("")
        self.back_6.setText("")
        ___qtablewidgetitem19 = self.table_agenda.horizontalHeaderItem(0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem20 = self.table_agenda.horizontalHeaderItem(1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Compromisso", None));
        ___qtablewidgetitem21 = self.table_agenda.horizontalHeaderItem(2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"Cliente", None));
        ___qtablewidgetitem22 = self.table_agenda.horizontalHeaderItem(3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"Tel1", None));
        ___qtablewidgetitem23 = self.table_agenda.horizontalHeaderItem(4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem24 = self.table_agenda.horizontalHeaderItem(5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Tel3", None));
        ___qtablewidgetitem25 = self.table_agenda.horizontalHeaderItem(6)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Hora", None));
        ___qtablewidgetitem26 = self.table_agenda.horizontalHeaderItem(7)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None));
        ___qtablewidgetitem27 = self.table_agenda.horizontalHeaderItem(8)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Agendado", None));
        ___qtablewidgetitem28 = self.table_agenda.horizontalHeaderItem(9)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"Observa\u00e7oes", None));
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Pesquisar </span></p></body></html>", None))
        self.new_cashier.setText("")
        self.edit_cashier.setText("")
        self.delete_cashier.setText("")
        self.print_cashier.setText("")
        ___qtablewidgetitem29 = self.table_caixa.horizontalHeaderItem(0)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem30 = self.table_caixa.horizontalHeaderItem(1)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        ___qtablewidgetitem31 = self.table_caixa.horizontalHeaderItem(2)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Entrada", None));
        ___qtablewidgetitem32 = self.table_caixa.horizontalHeaderItem(3)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Saida", None));
        ___qtablewidgetitem33 = self.table_caixa.horizontalHeaderItem(4)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"forma", None));
        ___qtablewidgetitem34 = self.table_caixa.horizontalHeaderItem(5)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o ", None));
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Saldo Atual</span></p></body></html>", None))
        self.back_8.setText("")
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("MainWindow", u"Caixa", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Pesquisar Produto", None))
        self.new_product.setText("")
        self.edit_product.setText("")
        self.delete_product.setText("")
        self.back_10.setText("")
        ___qtablewidgetitem35 = self.table_produto.horizontalHeaderItem(0)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem36 = self.table_produto.horizontalHeaderItem(1)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"Nome", None));
        ___qtablewidgetitem37 = self.table_produto.horizontalHeaderItem(2)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7ao", None));
        ___qtablewidgetitem38 = self.table_produto.horizontalHeaderItem(3)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        ___qtablewidgetitem39 = self.table_produto.horizontalHeaderItem(4)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Estoque", None));
        ___qtablewidgetitem40 = self.table_produto.horizontalHeaderItem(5)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"Categoria", None));
        ___qtablewidgetitem41 = self.table_produto.horizontalHeaderItem(6)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Grupo", None));
        ___qtablewidgetitem42 = self.table_produto.horizontalHeaderItem(7)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"Data", None));
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Pesquisar OS", None))
        self.new_os.setText("")
        self.edit_os.setText("")
        self.delete_os.setText("")
        self.print_os.setText("")
        self.back_12.setText("")
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Tel(1)", None))
        self.label_56.setText(QCoreApplication.translate("MainWindow", u"Tel(2)", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.label_65.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"CPF/CNPJ", None))
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.cancel_client.setText("")
        self.save_client.setText("")
        self.back_client.setText("")
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"CPF/CNPJ", None))
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Observa\u00e7\u00f5es</p></body></html>", None))
        self.cancel_provider.setText("")
        self.save_provider.setText("")
        self.back_provider.setText("")
        self.label_77.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_19.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Telefone (1)</span></p></body></html>", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Telefone (2)</span></p></body></html>", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Endere\u00e7o</span></p></body></html>", None))
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Nome </p></body></html>", None))
        self.label_31.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Compromisso</span></p></body></html>", None))
        self.com.setText("")
        self.label_32.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Nome Do Cliente</span></p></body></html>", None))
        self.cliente.setText("")
        self.label_36.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Tel(1)</p></body></html>", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Tel(2)</p></body></html>", None))
        self.tel1_3.setText("")
        self.tel2_3.setText("")
        self.label_28.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">DATA AGENDAMENTO</span></p></body></html>", None))
        self.label_29.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">HORA</span></p></body></html>", None))
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Endere\u00e7o</p></body></html>", None))
        self.end_2.setText("")
        self.cancel_task.setText("")
        self.print_task.setText("")
        self.save_task.setText("")
        self.back_task.setText("")
        self.label_30.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Observa\u00e7\u00f5es</span></p></body></html>", None))
        self.label_60.setText(QCoreApplication.translate("MainWindow", u"Valor", None))
        self.forma.setItemText(0, QCoreApplication.translate("MainWindow", u"A vista", None))
        self.forma.setItemText(1, QCoreApplication.translate("MainWindow", u"Parcelado 1x", None))
        self.forma.setItemText(2, QCoreApplication.translate("MainWindow", u"Parcelado 2x", None))
        self.forma.setItemText(3, QCoreApplication.translate("MainWindow", u"Parcelado 3x", None))
        self.forma.setItemText(4, QCoreApplication.translate("MainWindow", u"Parcelado 4x", None))
        self.forma.setItemText(5, QCoreApplication.translate("MainWindow", u"Parcelado 5x", None))
        self.forma.setItemText(6, QCoreApplication.translate("MainWindow", u"Parcelado 6x", None))
        self.forma.setItemText(7, QCoreApplication.translate("MainWindow", u"Parcelado 7x", None))
        self.forma.setItemText(8, QCoreApplication.translate("MainWindow", u"Parcelado 8x", None))
        self.forma.setItemText(9, QCoreApplication.translate("MainWindow", u"Parcelado 9x", None))
        self.forma.setItemText(10, QCoreApplication.translate("MainWindow", u"Parcelado 10x", None))

        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.label_59.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o", None))
        self.add_entry.setText("")
        self.add_out.setText("")
        self.back_cashier.setText("")
        self.label_44.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Nome Do Produto</span></p></body></html>", None))
        self.nm_prod.setText("")
        self.label_47.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Grupo</p></body></html>", None))
        self.grup_prod.setText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">ESTOQUE </span></p></body></html>", None))
        self.qt_prod.setText("")
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Descri\u00e7\u00e3o</span></p></body></html>", None))
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:14pt;\">CALCULOS</span></p></body></html>", None))
        self.uni.setText(QCoreApplication.translate("MainWindow", u"Unidade", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">VALOR </span></p></body></html>", None))
        self.valor_uni.setPrefix("")
        self.valor_uni.setSuffix("")
        self.m2.setText(QCoreApplication.translate("MainWindow", u"M2", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">VALOR </span></p></body></html>", None))
        self.kg.setText(QCoreApplication.translate("MainWindow", u"KG/Barra", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">VALOR </span></p></body></html>", None))
        self.back_product.setText("")
        self.cancel_product.setText("")
        self.save_product.setText("")
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"Aguardando Aprova\u00e7\u00e3o", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Em Prepara\u00e7ao", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Entrega Pendente", None))
        self.comboBox.setItemText(3, QCoreApplication.translate("MainWindow", u"Concluido", None))

        self.calc.setText("")
        self.finish_os.setText("")
        self.inserir_produto.setText("")
        self.salvar_os.setText("")
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:12pt;\">TOTAL</span></p></body></html>", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Tel(1)", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Tel(2)", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"CPF/CNPJ", None))
        self.label_48.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Cidade", None))
        self.check_obs.setText(QCoreApplication.translate("MainWindow", u"Incluir Oberva\u00e7\u00f5es Na OS", None))
        self.check_aprove.setText(QCoreApplication.translate("MainWindow", u"APROVADO EM", None))
        self.check_delivery.setText(QCoreApplication.translate("MainWindow", u"VALIDO ATE", None))
        self.save_client_os.setText("")
        self.cancel_client_os.setText("")
        self.back_os_2.setText("")
        self.next.setText("")
        self.tab_os.setTabText(self.tab_os.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"Cadastro Cliente", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Codigo</span></p></body></html>", None))
        self.search_product_2.setText("")
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Nome Do Produto</span></p></body></html>", None))
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">QT</span></p></body></html>", None))
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Largura</span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Altura</span></p><p><span style=\" font-size:10pt;\"><br/></span></p></body></html>", None))
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:10pt;\">Comprimento</span></p><p><br/></p></body></html>", None))
        self.insert_product.setText("")
        self.remove_product.setText("")
        self.cancel_os.setText("")
        self.back_os.setText("")
        ___qtablewidgetitem43 = self.table_add_os.horizontalHeaderItem(0)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"Codigo", None));
        ___qtablewidgetitem44 = self.table_add_os.horizontalHeaderItem(1)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"Descri\u00e7\u00e3o Do Produto", None));
        ___qtablewidgetitem45 = self.table_add_os.horizontalHeaderItem(2)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"QT", None));
        ___qtablewidgetitem46 = self.table_add_os.horizontalHeaderItem(3)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Largura", None));
        ___qtablewidgetitem47 = self.table_add_os.horizontalHeaderItem(4)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"Altura", None));
        ___qtablewidgetitem48 = self.table_add_os.horizontalHeaderItem(5)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Comprimento", None));
        ___qtablewidgetitem49 = self.table_add_os.horizontalHeaderItem(6)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"Valor", None));
        self.tab_os.setTabText(self.tab_os.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Lista De Produtos E Servi\u00e7os", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Nome", None))
        self.label_68.setText(QCoreApplication.translate("MainWindow", u"CPF/CNPJ", None))
        self.label_69.setText(QCoreApplication.translate("MainWindow", u"ENDERE\u00c7O", None))
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"BAIRRO", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"CIDADE", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"UF", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"CEP", None))
        self.label_74.setText(QCoreApplication.translate("MainWindow", u"TEL(1)", None))
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"TEL(2)", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"EMAIL", None))
        self.cancel_pdf.setText("")
        self.back_13.setText("")
        self.alter_pdf_2.setText(QCoreApplication.translate("MainWindow", u"Habilitar Edic\u00e7ao", None))
        self.edit_pdf_2.setText("")
        self.menuCONFIG.setTitle(QCoreApplication.translate("MainWindow", u"CONFIGURA\u00c7\u00d5ES", None))
        self.menuAJUDA.setTitle(QCoreApplication.translate("MainWindow", u"AJUDA", None))
        self.menuSOBRE.setTitle(QCoreApplication.translate("MainWindow", u"SOBRE", None))
    # retranslateUi

