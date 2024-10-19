# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainsjTnYR.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QFrame,
    QGridLayout, QGroupBox, QHBoxLayout, QHeaderView,
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QSpacerItem, QStackedWidget, QStatusBar,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1280, 743)
        MainWindow.setMinimumSize(QSize(1280, 691))
        MainWindow.setMaximumSize(QSize(1280, 772))
        MainWindow.setSizeIncrement(QSize(1280, 0))
        MainWindow.setBaseSize(QSize(1280, 691))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.lb_msg_rodape = QLabel(self.centralwidget)
        self.lb_msg_rodape.setObjectName(u"lb_msg_rodape")
        self.lb_msg_rodape.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_2.addWidget(self.lb_msg_rodape, 4, 1, 1, 1)

        self.lb_date_time_local = QLabel(self.centralwidget)
        self.lb_date_time_local.setObjectName(u"lb_date_time_local")

        self.gridLayout_2.addWidget(self.lb_date_time_local, 4, 0, 1, 1)

        self.groupBox = QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(u"groupBox")
        self.gridLayout_4 = QGridLayout(self.groupBox)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.stackedWidget = QStackedWidget(self.groupBox)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout = QGridLayout(self.page)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gb_enderecos = QGroupBox(self.page)
        self.gb_enderecos.setObjectName(u"gb_enderecos")
        self.gridLayout_5 = QGridLayout(self.gb_enderecos)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.verticalLayout_13 = QVBoxLayout()
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.lb_title_cep = QLabel(self.gb_enderecos)
        self.lb_title_cep.setObjectName(u"lb_title_cep")

        self.verticalLayout_13.addWidget(self.lb_title_cep)

        self.horizontalLayout_17 = QHBoxLayout()
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lb_img_cep = QLabel(self.gb_enderecos)
        self.lb_img_cep.setObjectName(u"lb_img_cep")
        self.lb_img_cep.setMaximumSize(QSize(24, 24))
        self.lb_img_cep.setScaledContents(True)

        self.horizontalLayout_17.addWidget(self.lb_img_cep)

        self.le_cep = QLineEdit(self.gb_enderecos)
        self.le_cep.setObjectName(u"le_cep")

        self.horizontalLayout_17.addWidget(self.le_cep)


        self.verticalLayout_13.addLayout(self.horizontalLayout_17)


        self.horizontalLayout_16.addLayout(self.verticalLayout_13)


        self.gridLayout_5.addLayout(self.horizontalLayout_16, 0, 1, 1, 1)

        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.lb_separator_8 = QLabel(self.gb_enderecos)
        self.lb_separator_8.setObjectName(u"lb_separator_8")
        self.lb_separator_8.setMaximumSize(QSize(1, 200))
        self.lb_separator_8.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(181, 181, 181);\n"
"}")

        self.horizontalLayout_22.addWidget(self.lb_separator_8)

        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.lb_title_uf = QLabel(self.gb_enderecos)
        self.lb_title_uf.setObjectName(u"lb_title_uf")

        self.verticalLayout_16.addWidget(self.lb_title_uf)

        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.lb_img_uf = QLabel(self.gb_enderecos)
        self.lb_img_uf.setObjectName(u"lb_img_uf")
        self.lb_img_uf.setMaximumSize(QSize(24, 24))
        self.lb_img_uf.setScaledContents(True)

        self.horizontalLayout_23.addWidget(self.lb_img_uf)

        self.cb_estado = QComboBox(self.gb_enderecos)
        self.cb_estado.addItem("")
        self.cb_estado.setObjectName(u"cb_estado")

        self.horizontalLayout_23.addWidget(self.cb_estado)

        self.horizontalSpacer_7 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_23.addItem(self.horizontalSpacer_7)


        self.verticalLayout_16.addLayout(self.horizontalLayout_23)


        self.horizontalLayout_22.addLayout(self.verticalLayout_16)


        self.gridLayout_5.addLayout(self.horizontalLayout_22, 1, 2, 1, 1)

        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.verticalLayout_15 = QVBoxLayout()
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.lb_title_city = QLabel(self.gb_enderecos)
        self.lb_title_city.setObjectName(u"lb_title_city")

        self.verticalLayout_15.addWidget(self.lb_title_city)

        self.horizontalLayout_21 = QHBoxLayout()
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.lb_img_city = QLabel(self.gb_enderecos)
        self.lb_img_city.setObjectName(u"lb_img_city")
        self.lb_img_city.setMaximumSize(QSize(24, 24))
        self.lb_img_city.setScaledContents(True)

        self.horizontalLayout_21.addWidget(self.lb_img_city)

        self.le_cidade = QLineEdit(self.gb_enderecos)
        self.le_cidade.setObjectName(u"le_cidade")

        self.horizontalLayout_21.addWidget(self.le_cidade)


        self.verticalLayout_15.addLayout(self.horizontalLayout_21)


        self.horizontalLayout_20.addLayout(self.verticalLayout_15)


        self.gridLayout_5.addLayout(self.horizontalLayout_20, 1, 1, 1, 1)

        self.horizontalLayout_29 = QHBoxLayout()
        self.horizontalLayout_29.setObjectName(u"horizontalLayout_29")
        self.lb_separator_9 = QLabel(self.gb_enderecos)
        self.lb_separator_9.setObjectName(u"lb_separator_9")
        self.lb_separator_9.setMaximumSize(QSize(1, 200))
        self.lb_separator_9.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(181, 181, 181);\n"
"}")

        self.horizontalLayout_29.addWidget(self.lb_separator_9)

        self.verticalLayout_19 = QVBoxLayout()
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.lb_title_number = QLabel(self.gb_enderecos)
        self.lb_title_number.setObjectName(u"lb_title_number")

        self.verticalLayout_19.addWidget(self.lb_title_number)

        self.horizontalLayout_30 = QHBoxLayout()
        self.horizontalLayout_30.setObjectName(u"horizontalLayout_30")
        self.lb_img_number = QLabel(self.gb_enderecos)
        self.lb_img_number.setObjectName(u"lb_img_number")
        self.lb_img_number.setMaximumSize(QSize(24, 24))
        self.lb_img_number.setScaledContents(True)

        self.horizontalLayout_30.addWidget(self.lb_img_number)

        self.le_numero_casa = QLineEdit(self.gb_enderecos)
        self.le_numero_casa.setObjectName(u"le_numero_casa")

        self.horizontalLayout_30.addWidget(self.le_numero_casa)


        self.verticalLayout_19.addLayout(self.horizontalLayout_30)


        self.horizontalLayout_29.addLayout(self.verticalLayout_19)


        self.gridLayout_5.addLayout(self.horizontalLayout_29, 1, 4, 1, 1)

        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.lb_separator_5 = QLabel(self.gb_enderecos)
        self.lb_separator_5.setObjectName(u"lb_separator_5")
        self.lb_separator_5.setMaximumSize(QSize(1, 200))
        self.lb_separator_5.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(181, 181, 181);\n"
"}")

        self.horizontalLayout_18.addWidget(self.lb_separator_5)

        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.lb_title_address = QLabel(self.gb_enderecos)
        self.lb_title_address.setObjectName(u"lb_title_address")

        self.verticalLayout_14.addWidget(self.lb_title_address)

        self.horizontalLayout_19 = QHBoxLayout()
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.lb_img_address = QLabel(self.gb_enderecos)
        self.lb_img_address.setObjectName(u"lb_img_address")
        self.lb_img_address.setMaximumSize(QSize(24, 24))
        self.lb_img_address.setScaledContents(True)

        self.horizontalLayout_19.addWidget(self.lb_img_address)

        self.le_endereco = QLineEdit(self.gb_enderecos)
        self.le_endereco.setObjectName(u"le_endereco")

        self.horizontalLayout_19.addWidget(self.le_endereco)


        self.verticalLayout_14.addLayout(self.horizontalLayout_19)


        self.horizontalLayout_18.addLayout(self.verticalLayout_14)


        self.gridLayout_5.addLayout(self.horizontalLayout_18, 0, 2, 1, 1)

        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.lb_separator_6 = QLabel(self.gb_enderecos)
        self.lb_separator_6.setObjectName(u"lb_separator_6")
        self.lb_separator_6.setMaximumSize(QSize(1, 200))
        self.lb_separator_6.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(181, 181, 181);\n"
"}")

        self.horizontalLayout_24.addWidget(self.lb_separator_6)

        self.verticalLayout_17 = QVBoxLayout()
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.lb_title_district = QLabel(self.gb_enderecos)
        self.lb_title_district.setObjectName(u"lb_title_district")

        self.verticalLayout_17.addWidget(self.lb_title_district)

        self.horizontalLayout_25 = QHBoxLayout()
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.lb_img_district = QLabel(self.gb_enderecos)
        self.lb_img_district.setObjectName(u"lb_img_district")
        self.lb_img_district.setMaximumSize(QSize(24, 24))
        self.lb_img_district.setScaledContents(True)

        self.horizontalLayout_25.addWidget(self.lb_img_district)

        self.le_bairro = QLineEdit(self.gb_enderecos)
        self.le_bairro.setObjectName(u"le_bairro")

        self.horizontalLayout_25.addWidget(self.le_bairro)


        self.verticalLayout_17.addLayout(self.horizontalLayout_25)


        self.horizontalLayout_24.addLayout(self.verticalLayout_17)


        self.gridLayout_5.addLayout(self.horizontalLayout_24, 0, 4, 1, 1)

        self.verticalLayout_18 = QVBoxLayout()
        self.verticalLayout_18.setObjectName(u"verticalLayout_18")
        self.lb_title_complement = QLabel(self.gb_enderecos)
        self.lb_title_complement.setObjectName(u"lb_title_complement")

        self.verticalLayout_18.addWidget(self.lb_title_complement)

        self.horizontalLayout_27 = QHBoxLayout()
        self.horizontalLayout_27.setObjectName(u"horizontalLayout_27")
        self.lb_img_complement = QLabel(self.gb_enderecos)
        self.lb_img_complement.setObjectName(u"lb_img_complement")
        self.lb_img_complement.setMaximumSize(QSize(24, 24))
        self.lb_img_complement.setScaledContents(True)

        self.horizontalLayout_27.addWidget(self.lb_img_complement)

        self.le_complemento = QLineEdit(self.gb_enderecos)
        self.le_complemento.setObjectName(u"le_complemento")

        self.horizontalLayout_27.addWidget(self.le_complemento)


        self.verticalLayout_18.addLayout(self.horizontalLayout_27)


        self.gridLayout_5.addLayout(self.verticalLayout_18, 2, 1, 1, 1)


        self.gridLayout.addWidget(self.gb_enderecos, 3, 0, 1, 1)

        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer_2)

        self.btn_save = QPushButton(self.page)
        self.btn_save.setObjectName(u"btn_save")
        self.btn_save.setMinimumSize(QSize(100, 35))
        self.btn_save.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_save.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(52, 156, 118);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: rgb(56, 168, 127);\n"
"}")
        icon = QIcon()
        icon.addFile(u"../../assets/img/save.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_save.setIcon(icon)
        self.btn_save.setIconSize(QSize(20, 20))

        self.horizontalLayout_26.addWidget(self.btn_save)

        self.btn_clean_fields = QPushButton(self.page)
        self.btn_clean_fields.setObjectName(u"btn_clean_fields")
        self.btn_clean_fields.setMinimumSize(QSize(150, 35))
        self.btn_clean_fields.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_clean_fields.setStyleSheet(u"QPushButton{\n"
"	background-color: #dd5138;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #dd654b;\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u"../../assets/img/garbage.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_clean_fields.setIcon(icon1)
        self.btn_clean_fields.setIconSize(QSize(20, 20))

        self.horizontalLayout_26.addWidget(self.btn_clean_fields)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_26.addItem(self.horizontalSpacer)


        self.gridLayout.addLayout(self.horizontalLayout_26, 7, 0, 1, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 6, 0, 1, 1)

        self.gp_dados_pessoais = QGroupBox(self.page)
        self.gp_dados_pessoais.setObjectName(u"gp_dados_pessoais")
        self.gridLayout_3 = QGridLayout(self.gp_dados_pessoais)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.lb_title_full_name = QLabel(self.gp_dados_pessoais)
        self.lb_title_full_name.setObjectName(u"lb_title_full_name")

        self.verticalLayout_2.addWidget(self.lb_title_full_name)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.lb_img_name = QLabel(self.gp_dados_pessoais)
        self.lb_img_name.setObjectName(u"lb_img_name")
        self.lb_img_name.setMaximumSize(QSize(24, 24))
        self.lb_img_name.setScaledContents(True)

        self.horizontalLayout_3.addWidget(self.lb_img_name)

        self.le_nome_completo = QLineEdit(self.gp_dados_pessoais)
        self.le_nome_completo.setObjectName(u"le_nome_completo")

        self.horizontalLayout_3.addWidget(self.le_nome_completo)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.gridLayout_3.addLayout(self.verticalLayout_2, 2, 0, 1, 2)

        self.horizontalLayout_14 = QHBoxLayout()
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.lb_separator = QLabel(self.gp_dados_pessoais)
        self.lb_separator.setObjectName(u"lb_separator")
        self.lb_separator.setMaximumSize(QSize(1, 200))
        self.lb_separator.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(181, 181, 181);\n"
"}")

        self.horizontalLayout_14.addWidget(self.lb_separator)

        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.lb_title_job = QLabel(self.gp_dados_pessoais)
        self.lb_title_job.setObjectName(u"lb_title_job")

        self.verticalLayout_12.addWidget(self.lb_title_job)

        self.horizontalLayout_15 = QHBoxLayout()
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.lb_img_job = QLabel(self.gp_dados_pessoais)
        self.lb_img_job.setObjectName(u"lb_img_job")
        self.lb_img_job.setMaximumSize(QSize(24, 24))
        self.lb_img_job.setScaledContents(True)

        self.horizontalLayout_15.addWidget(self.lb_img_job)

        self.le_profissao = QLineEdit(self.gp_dados_pessoais)
        self.le_profissao.setObjectName(u"le_profissao")

        self.horizontalLayout_15.addWidget(self.le_profissao)


        self.verticalLayout_12.addLayout(self.horizontalLayout_15)


        self.horizontalLayout_14.addLayout(self.verticalLayout_12)


        self.gridLayout_3.addLayout(self.horizontalLayout_14, 2, 2, 1, 1)

        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.lb_title_date_birth = QLabel(self.gp_dados_pessoais)
        self.lb_title_date_birth.setObjectName(u"lb_title_date_birth")

        self.verticalLayout_10.addWidget(self.lb_title_date_birth)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.lb_img_date = QLabel(self.gp_dados_pessoais)
        self.lb_img_date.setObjectName(u"lb_img_date")
        self.lb_img_date.setMaximumSize(QSize(24, 24))
        self.lb_img_date.setScaledContents(True)

        self.horizontalLayout_9.addWidget(self.lb_img_date)

        self.de_data_nascimento = QDateEdit(self.gp_dados_pessoais)
        self.de_data_nascimento.setObjectName(u"de_data_nascimento")

        self.horizontalLayout_9.addWidget(self.de_data_nascimento)


        self.verticalLayout_10.addLayout(self.horizontalLayout_9)


        self.gridLayout_3.addLayout(self.verticalLayout_10, 8, 0, 1, 1)

        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.lb_separator_2 = QLabel(self.gp_dados_pessoais)
        self.lb_separator_2.setObjectName(u"lb_separator_2")
        self.lb_separator_2.setMaximumSize(QSize(1, 200))
        self.lb_separator_2.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(181, 181, 181);\n"
"}")

        self.horizontalLayout_12.addWidget(self.lb_separator_2)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lb_title_rg_ie = QLabel(self.gp_dados_pessoais)
        self.lb_title_rg_ie.setObjectName(u"lb_title_rg_ie")

        self.verticalLayout_4.addWidget(self.lb_title_rg_ie)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.lb_img_rg = QLabel(self.gp_dados_pessoais)
        self.lb_img_rg.setObjectName(u"lb_img_rg")
        self.lb_img_rg.setMaximumSize(QSize(24, 24))
        self.lb_img_rg.setScaledContents(True)

        self.horizontalLayout_6.addWidget(self.lb_img_rg)

        self.le_rg = QLineEdit(self.gp_dados_pessoais)
        self.le_rg.setObjectName(u"le_rg")

        self.horizontalLayout_6.addWidget(self.le_rg)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)


        self.horizontalLayout_12.addLayout(self.verticalLayout_4)


        self.gridLayout_3.addLayout(self.horizontalLayout_12, 7, 1, 1, 1)

        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.lb_separator_3 = QLabel(self.gp_dados_pessoais)
        self.lb_separator_3.setObjectName(u"lb_separator_3")
        self.lb_separator_3.setMaximumSize(QSize(1, 200))
        self.lb_separator_3.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(181, 181, 181);\n"
"}")

        self.horizontalLayout_13.addWidget(self.lb_separator_3)

        self.verticalLayout_9 = QVBoxLayout()
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lb_title_email = QLabel(self.gp_dados_pessoais)
        self.lb_title_email.setObjectName(u"lb_title_email")

        self.verticalLayout_9.addWidget(self.lb_title_email)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.lb_img_email = QLabel(self.gp_dados_pessoais)
        self.lb_img_email.setObjectName(u"lb_img_email")
        self.lb_img_email.setMaximumSize(QSize(24, 24))
        self.lb_img_email.setScaledContents(True)

        self.horizontalLayout_8.addWidget(self.lb_img_email)

        self.le_email = QLineEdit(self.gp_dados_pessoais)
        self.le_email.setObjectName(u"le_email")

        self.horizontalLayout_8.addWidget(self.le_email)


        self.verticalLayout_9.addLayout(self.horizontalLayout_8)


        self.horizontalLayout_13.addLayout(self.verticalLayout_9)


        self.gridLayout_3.addLayout(self.horizontalLayout_13, 7, 2, 1, 1)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.lb_title_type_person = QLabel(self.gp_dados_pessoais)
        self.lb_title_type_person.setObjectName(u"lb_title_type_person")

        self.verticalLayout_6.addWidget(self.lb_title_type_person)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.lb_img_type_person = QLabel(self.gp_dados_pessoais)
        self.lb_img_type_person.setObjectName(u"lb_img_type_person")
        self.lb_img_type_person.setMaximumSize(QSize(24, 24))
        self.lb_img_type_person.setScaledContents(True)

        self.horizontalLayout_4.addWidget(self.lb_img_type_person)

        self.cb_tipo_pessoa = QComboBox(self.gp_dados_pessoais)
        self.cb_tipo_pessoa.addItem("")
        self.cb_tipo_pessoa.setObjectName(u"cb_tipo_pessoa")

        self.horizontalLayout_4.addWidget(self.cb_tipo_pessoa)

        self.horizontalSpacer_6 = QSpacerItem(80, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_6)


        self.verticalLayout_6.addLayout(self.horizontalLayout_4)


        self.gridLayout_3.addLayout(self.verticalLayout_6, 0, 0, 1, 1)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.lb_separator_4 = QLabel(self.gp_dados_pessoais)
        self.lb_separator_4.setObjectName(u"lb_separator_4")
        self.lb_separator_4.setMaximumSize(QSize(1, 200))
        self.lb_separator_4.setStyleSheet(u"QLabel{\n"
"	background-color: rgb(181, 181, 181);\n"
"}")

        self.horizontalLayout_11.addWidget(self.lb_separator_4)

        self.verticalLayout_11 = QVBoxLayout()
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.lb_title_phone = QLabel(self.gp_dados_pessoais)
        self.lb_title_phone.setObjectName(u"lb_title_phone")

        self.verticalLayout_11.addWidget(self.lb_title_phone)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.lb_img_phone = QLabel(self.gp_dados_pessoais)
        self.lb_img_phone.setObjectName(u"lb_img_phone")
        self.lb_img_phone.setMaximumSize(QSize(24, 24))
        self.lb_img_phone.setScaledContents(True)

        self.horizontalLayout_10.addWidget(self.lb_img_phone)

        self.le_telefone = QLineEdit(self.gp_dados_pessoais)
        self.le_telefone.setObjectName(u"le_telefone")

        self.horizontalLayout_10.addWidget(self.le_telefone)


        self.verticalLayout_11.addLayout(self.horizontalLayout_10)


        self.horizontalLayout_11.addLayout(self.verticalLayout_11)


        self.gridLayout_3.addLayout(self.horizontalLayout_11, 8, 1, 1, 1)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lb_title_cpf_cnpj = QLabel(self.gp_dados_pessoais)
        self.lb_title_cpf_cnpj.setObjectName(u"lb_title_cpf_cnpj")

        self.verticalLayout_3.addWidget(self.lb_title_cpf_cnpj)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.lb_img_cpf = QLabel(self.gp_dados_pessoais)
        self.lb_img_cpf.setObjectName(u"lb_img_cpf")
        self.lb_img_cpf.setMaximumSize(QSize(24, 24))
        self.lb_img_cpf.setScaledContents(True)

        self.horizontalLayout_5.addWidget(self.lb_img_cpf)

        self.le_cpf = QLineEdit(self.gp_dados_pessoais)
        self.le_cpf.setObjectName(u"le_cpf")

        self.horizontalLayout_5.addWidget(self.le_cpf)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)


        self.verticalLayout_5.addLayout(self.verticalLayout_3)


        self.gridLayout_3.addLayout(self.verticalLayout_5, 7, 0, 1, 1)


        self.gridLayout.addWidget(self.gp_dados_pessoais, 2, 0, 1, 1)

        self.lineEdit_11 = QLineEdit(self.page)
        self.lineEdit_11.setObjectName(u"lineEdit_11")
        self.lineEdit_11.setMaximumSize(QSize(16777215, 1))

        self.gridLayout.addWidget(self.lineEdit_11, 5, 0, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_2, 4, 0, 1, 1)

        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.gridLayout_6 = QGridLayout(self.page_2)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gb_registros = QGroupBox(self.page_2)
        self.gb_registros.setObjectName(u"gb_registros")
        self.gridLayout_7 = QGridLayout(self.gb_registros)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gb_pesquisa_nome = QGroupBox(self.gb_registros)
        self.gb_pesquisa_nome.setObjectName(u"gb_pesquisa_nome")
        self.gridLayout_8 = QGridLayout(self.gb_pesquisa_nome)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.le_pesquisa_nome = QLineEdit(self.gb_pesquisa_nome)
        self.le_pesquisa_nome.setObjectName(u"le_pesquisa_nome")

        self.gridLayout_8.addWidget(self.le_pesquisa_nome, 0, 1, 1, 1)


        self.gridLayout_7.addWidget(self.gb_pesquisa_nome, 0, 0, 1, 1)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.btn_remove_registration = QPushButton(self.gb_registros)
        self.btn_remove_registration.setObjectName(u"btn_remove_registration")
        self.btn_remove_registration.setMinimumSize(QSize(120, 35))
        self.btn_remove_registration.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_remove_registration.setStyleSheet(u"QPushButton{\n"
"	background-color: #dd5138;\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #dd654b;\n"
"}")
        self.btn_remove_registration.setIcon(icon1)
        self.btn_remove_registration.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_remove_registration)

        self.btn_update_table = QPushButton(self.gb_registros)
        self.btn_update_table.setObjectName(u"btn_update_table")
        self.btn_update_table.setMinimumSize(QSize(120, 35))
        self.btn_update_table.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_update_table.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(36, 74, 109);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #245b75;\n"
"}")
        icon2 = QIcon()
        icon2.addFile(u"../../assets/img/repeat.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_update_table.setIcon(icon2)
        self.btn_update_table.setIconSize(QSize(20, 20))

        self.horizontalLayout.addWidget(self.btn_update_table)


        self.gridLayout_7.addLayout(self.horizontalLayout, 1, 0, 1, 1)

        self.gb_pesquisa_rg_cpf = QGroupBox(self.gb_registros)
        self.gb_pesquisa_rg_cpf.setObjectName(u"gb_pesquisa_rg_cpf")
        self.gridLayout_9 = QGridLayout(self.gb_pesquisa_rg_cpf)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.le_pesquisa_rg_cpf = QLineEdit(self.gb_pesquisa_rg_cpf)
        self.le_pesquisa_rg_cpf.setObjectName(u"le_pesquisa_rg_cpf")

        self.gridLayout_9.addWidget(self.le_pesquisa_rg_cpf, 0, 0, 1, 1)


        self.gridLayout_7.addWidget(self.gb_pesquisa_rg_cpf, 0, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_3, 0, 3, 1, 1)

        self.lb_desc_clica_duas_vezes = QLabel(self.gb_registros)
        self.lb_desc_clica_duas_vezes.setObjectName(u"lb_desc_clica_duas_vezes")

        self.gridLayout_7.addWidget(self.lb_desc_clica_duas_vezes, 1, 1, 1, 1)

        self.horizontalSpacer_4 = QSpacerItem(100, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.gridLayout_7.addItem(self.horizontalSpacer_4, 0, 4, 1, 1)

        self.lb_qtd_registros = QLabel(self.gb_registros)
        self.lb_qtd_registros.setObjectName(u"lb_qtd_registros")

        self.gridLayout_7.addWidget(self.lb_qtd_registros, 1, 4, 1, 1)

        self.lb_titulo_total_registro = QLabel(self.gb_registros)
        self.lb_titulo_total_registro.setObjectName(u"lb_titulo_total_registro")
        self.lb_titulo_total_registro.setAlignment(Qt.AlignmentFlag.AlignRight|Qt.AlignmentFlag.AlignTrailing|Qt.AlignmentFlag.AlignVCenter)

        self.gridLayout_7.addWidget(self.lb_titulo_total_registro, 1, 3, 1, 1)

        self.tw_tabela_registros = QTableWidget(self.gb_registros)
        self.tw_tabela_registros.setObjectName(u"tw_tabela_registros")

        self.gridLayout_7.addWidget(self.tw_tabela_registros, 2, 0, 1, 5)


        self.gridLayout_6.addWidget(self.gb_registros, 1, 0, 1, 1)

        self.stackedWidget.addWidget(self.page_2)

        self.gridLayout_4.addWidget(self.stackedWidget, 1, 0, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_4.addItem(self.verticalSpacer_3, 2, 0, 1, 1)


        self.gridLayout_2.addWidget(self.groupBox, 2, 0, 1, 2)

        self.horizontalLayout_32 = QHBoxLayout()
        self.horizontalLayout_32.setObjectName(u"horizontalLayout_32")
        self.lineEdit = QLineEdit(self.centralwidget)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(50, 1))

        self.horizontalLayout_32.addWidget(self.lineEdit)

        self.btn_home = QPushButton(self.centralwidget)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(130, 40))
        self.btn_home.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_home.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(36, 74, 109);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #245b75;\n"
"}")
        icon3 = QIcon()
        icon3.addFile(u"../resources/img/house.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_home.setIcon(icon3)
        self.btn_home.setIconSize(QSize(24, 24))

        self.horizontalLayout_32.addWidget(self.btn_home)

        self.btn_registrations = QPushButton(self.centralwidget)
        self.btn_registrations.setObjectName(u"btn_registrations")
        self.btn_registrations.setMinimumSize(QSize(130, 40))
        self.btn_registrations.setCursor(QCursor(Qt.CursorShape.PointingHandCursor))
        self.btn_registrations.setStyleSheet(u"QPushButton{\n"
"	background-color: rgb(36, 74, 109);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 8px;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color: #245b75;\n"
"}")
        icon4 = QIcon()
        icon4.addFile(u"../resources/img/folder_1.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.btn_registrations.setIcon(icon4)
        self.btn_registrations.setIconSize(QSize(24, 24))

        self.horizontalLayout_32.addWidget(self.btn_registrations)

        self.lineEdit_17 = QLineEdit(self.centralwidget)
        self.lineEdit_17.setObjectName(u"lineEdit_17")
        self.lineEdit_17.setMaximumSize(QSize(16777215, 1))

        self.horizontalLayout_32.addWidget(self.lineEdit_17)


        self.gridLayout_2.addLayout(self.horizontalLayout_32, 1, 0, 1, 2)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_2)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.lb_img_logo = QLabel(self.frame_2)
        self.lb_img_logo.setObjectName(u"lb_img_logo")
        self.lb_img_logo.setMinimumSize(QSize(0, 0))
        self.lb_img_logo.setMaximumSize(QSize(80, 70))
        self.lb_img_logo.setPixmap(QPixmap(u"../../assets/img/logo_opac.png"))
        self.lb_img_logo.setScaledContents(True)

        self.horizontalLayout_33.addWidget(self.lb_img_logo)

        self.horizontalSpacer_5 = QSpacerItem(20, 20, QSizePolicy.Policy.Fixed, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_33.addItem(self.horizontalSpacer_5)

        self.lb_titulo_app = QLabel(self.frame_2)
        self.lb_titulo_app.setObjectName(u"lb_titulo_app")
        font = QFont()
        font.setPointSize(30)
        self.lb_titulo_app.setFont(font)

        self.horizontalLayout_33.addWidget(self.lb_titulo_app)


        self.gridLayout_2.addWidget(self.frame_2, 0, 0, 1, 2)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        QWidget.setTabOrder(self.btn_home, self.btn_registrations)
        QWidget.setTabOrder(self.btn_registrations, self.cb_tipo_pessoa)
        QWidget.setTabOrder(self.cb_tipo_pessoa, self.le_nome_completo)
        QWidget.setTabOrder(self.le_nome_completo, self.le_profissao)
        QWidget.setTabOrder(self.le_profissao, self.le_cpf)
        QWidget.setTabOrder(self.le_cpf, self.le_rg)
        QWidget.setTabOrder(self.le_rg, self.le_email)
        QWidget.setTabOrder(self.le_email, self.de_data_nascimento)
        QWidget.setTabOrder(self.de_data_nascimento, self.le_telefone)
        QWidget.setTabOrder(self.le_telefone, self.le_cep)
        QWidget.setTabOrder(self.le_cep, self.le_endereco)
        QWidget.setTabOrder(self.le_endereco, self.le_bairro)
        QWidget.setTabOrder(self.le_bairro, self.le_cidade)
        QWidget.setTabOrder(self.le_cidade, self.cb_estado)
        QWidget.setTabOrder(self.cb_estado, self.le_numero_casa)
        QWidget.setTabOrder(self.le_numero_casa, self.le_complemento)
        QWidget.setTabOrder(self.le_complemento, self.btn_save)
        QWidget.setTabOrder(self.btn_save, self.btn_clean_fields)
        QWidget.setTabOrder(self.btn_clean_fields, self.le_pesquisa_nome)
        QWidget.setTabOrder(self.le_pesquisa_nome, self.le_pesquisa_rg_cpf)
        QWidget.setTabOrder(self.le_pesquisa_rg_cpf, self.btn_remove_registration)
        QWidget.setTabOrder(self.btn_remove_registration, self.btn_update_table)
        QWidget.setTabOrder(self.btn_update_table, self.tw_tabela_registros)
        QWidget.setTabOrder(self.tw_tabela_registros, self.lineEdit)
        QWidget.setTabOrder(self.lineEdit, self.lineEdit_17)
        QWidget.setTabOrder(self.lineEdit_17, self.lineEdit_11)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Cadastro de Clientes", None))
        self.lb_msg_rodape.setText(QCoreApplication.translate("MainWindow", u"Thales Plinio \u00a9 - 2004 - Todos os direitos reservados.", None))
        self.lb_date_time_local.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.groupBox.setTitle("")
        self.gb_enderecos.setTitle(QCoreApplication.translate("MainWindow", u"Endere\u00e7o", None))
        self.lb_title_cep.setText(QCoreApplication.translate("MainWindow", u"CEP:", None))
        self.lb_img_cep.setText("")
#if QT_CONFIG(tooltip)
        self.le_cep.setToolTip(QCoreApplication.translate("MainWindow", u"C\u00f3digo de Endere\u00e7amento Postal (CEP)", None))
#endif // QT_CONFIG(tooltip)
        self.lb_separator_8.setText("")
        self.lb_title_uf.setText(QCoreApplication.translate("MainWindow", u"Estado:", None))
        self.lb_img_uf.setText("")
        self.cb_estado.setItemText(0, QCoreApplication.translate("MainWindow", u"--- Selecione ---", None))

#if QT_CONFIG(tooltip)
        self.cb_estado.setToolTip(QCoreApplication.translate("MainWindow", u"Selecione um Estado", None))
#endif // QT_CONFIG(tooltip)
        self.lb_title_city.setText(QCoreApplication.translate("MainWindow", u"Cidade:", None))
        self.lb_img_city.setText("")
#if QT_CONFIG(tooltip)
        self.le_cidade.setToolTip(QCoreApplication.translate("MainWindow", u"Cidade", None))
#endif // QT_CONFIG(tooltip)
        self.lb_separator_9.setText("")
        self.lb_title_number.setText(QCoreApplication.translate("MainWindow", u"N\u00famero:", None))
        self.lb_img_number.setText("")
#if QT_CONFIG(tooltip)
        self.le_numero_casa.setToolTip(QCoreApplication.translate("MainWindow", u"N\u00famero residencial", None))
#endif // QT_CONFIG(tooltip)
        self.lb_separator_5.setText("")
        self.lb_title_address.setText(QCoreApplication.translate("MainWindow", u"Rua:", None))
        self.lb_img_address.setText("")
#if QT_CONFIG(tooltip)
        self.le_endereco.setToolTip(QCoreApplication.translate("MainWindow", u"Endere\u00e7o Rua", None))
#endif // QT_CONFIG(tooltip)
        self.lb_separator_6.setText("")
        self.lb_title_district.setText(QCoreApplication.translate("MainWindow", u"Bairro", None))
        self.lb_img_district.setText("")
#if QT_CONFIG(tooltip)
        self.le_bairro.setToolTip(QCoreApplication.translate("MainWindow", u"N\u00famero residencial", None))
#endif // QT_CONFIG(tooltip)
        self.lb_title_complement.setText(QCoreApplication.translate("MainWindow", u"Complemento", None))
        self.lb_img_complement.setText("")
#if QT_CONFIG(tooltip)
        self.le_complemento.setToolTip(QCoreApplication.translate("MainWindow", u"Complemento Ex. casa, escrit\u00f3rio ...", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_save.setToolTip(QCoreApplication.translate("MainWindow", u"<html><head/><body><p>Salvar registro</p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.btn_save.setText(QCoreApplication.translate("MainWindow", u"Salvar", None))
#if QT_CONFIG(tooltip)
        self.btn_clean_fields.setToolTip(QCoreApplication.translate("MainWindow", u"Limpar todos os campos", None))
#endif // QT_CONFIG(tooltip)
        self.btn_clean_fields.setText(QCoreApplication.translate("MainWindow", u"Limpar campos", None))
        self.gp_dados_pessoais.setTitle(QCoreApplication.translate("MainWindow", u"Dados Pessoais", None))
        self.lb_title_full_name.setText(QCoreApplication.translate("MainWindow", u"Nome Completo:", None))
        self.lb_img_name.setText("")
#if QT_CONFIG(tooltip)
        self.le_nome_completo.setToolTip(QCoreApplication.translate("MainWindow", u"Nome completo", None))
#endif // QT_CONFIG(tooltip)
        self.lb_separator.setText("")
        self.lb_title_job.setText(QCoreApplication.translate("MainWindow", u"Profiss\u00e3o:", None))
        self.lb_img_job.setText("")
#if QT_CONFIG(tooltip)
        self.le_profissao.setToolTip(QCoreApplication.translate("MainWindow", u"Profiss\u00e3o", None))
#endif // QT_CONFIG(tooltip)
        self.lb_title_date_birth.setText(QCoreApplication.translate("MainWindow", u"Data de nascimento:", None))
        self.lb_img_date.setText("")
#if QT_CONFIG(tooltip)
        self.de_data_nascimento.setToolTip(QCoreApplication.translate("MainWindow", u"Data de nascimento", None))
#endif // QT_CONFIG(tooltip)
        self.lb_separator_2.setText("")
#if QT_CONFIG(tooltip)
        self.lb_title_rg_ie.setToolTip(QCoreApplication.translate("MainWindow", u"Registro geral ou Inscri\u00e7\u00e3o estadual", None))
#endif // QT_CONFIG(tooltip)
        self.lb_title_rg_ie.setText(QCoreApplication.translate("MainWindow", u"RG:", None))
        self.lb_img_rg.setText("")
#if QT_CONFIG(tooltip)
        self.le_rg.setToolTip(QCoreApplication.translate("MainWindow", u"Registro Geral (RG) ou Inscri\u00e7\u00e3o Estadual (IE)", None))
#endif // QT_CONFIG(tooltip)
        self.lb_separator_3.setText("")
        self.lb_title_email.setText(QCoreApplication.translate("MainWindow", u"E-Mail:", None))
        self.lb_img_email.setText("")
#if QT_CONFIG(tooltip)
        self.le_email.setToolTip(QCoreApplication.translate("MainWindow", u"Endere\u00e7o de E-Mail", None))
#endif // QT_CONFIG(tooltip)
        self.lb_title_type_person.setText(QCoreApplication.translate("MainWindow", u"Tipo de Pessoa:", None))
        self.lb_img_type_person.setText("")
        self.cb_tipo_pessoa.setItemText(0, QCoreApplication.translate("MainWindow", u"--- Selecione ---", None))

        self.lb_separator_4.setText("")
        self.lb_title_phone.setText(QCoreApplication.translate("MainWindow", u"Telefone/Celular:", None))
        self.lb_img_phone.setText("")
#if QT_CONFIG(tooltip)
        self.le_telefone.setToolTip(QCoreApplication.translate("MainWindow", u"Telefone fixo ou Celular", None))
#endif // QT_CONFIG(tooltip)
        self.lb_title_cpf_cnpj.setText(QCoreApplication.translate("MainWindow", u"CPF:", None))
        self.lb_img_cpf.setText("")
#if QT_CONFIG(tooltip)
        self.le_cpf.setToolTip(QCoreApplication.translate("MainWindow", u"Cadastro de Pessoa F\u00edsica (CPF)", None))
#endif // QT_CONFIG(tooltip)
        self.gb_registros.setTitle(QCoreApplication.translate("MainWindow", u"Registros", None))
        self.gb_pesquisa_nome.setTitle(QCoreApplication.translate("MainWindow", u"Pesquisa por nome", None))
#if QT_CONFIG(tooltip)
        self.le_pesquisa_nome.setToolTip(QCoreApplication.translate("MainWindow", u"Informe um nome para pesquisa", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.btn_remove_registration.setToolTip(QCoreApplication.translate("MainWindow", u"Remover revistro selecionado", None))
#endif // QT_CONFIG(tooltip)
        self.btn_remove_registration.setText(QCoreApplication.translate("MainWindow", u"Remover registro", None))
#if QT_CONFIG(tooltip)
        self.btn_update_table.setToolTip(QCoreApplication.translate("MainWindow", u"Atualizar tabela", None))
#endif // QT_CONFIG(tooltip)
        self.btn_update_table.setText(QCoreApplication.translate("MainWindow", u"Atualiar tabela", None))
        self.gb_pesquisa_rg_cpf.setTitle(QCoreApplication.translate("MainWindow", u"Pesquisa por RG / CPF", None))
#if QT_CONFIG(tooltip)
        self.le_pesquisa_rg_cpf.setToolTip(QCoreApplication.translate("MainWindow", u"Informe um RG ou CPF para pesquisar", None))
#endif // QT_CONFIG(tooltip)
        self.lb_desc_clica_duas_vezes.setText(QCoreApplication.translate("MainWindow", u"Clique duas vezes em um registro para mais detalhes", None))
        self.lb_qtd_registros.setText(QCoreApplication.translate("MainWindow", u"...", None))
        self.lb_titulo_total_registro.setText(QCoreApplication.translate("MainWindow", u"Total de registros:", None))
#if QT_CONFIG(tooltip)
        self.btn_home.setToolTip(QCoreApplication.translate("MainWindow", u"P\u00e1gina inicial de cadastro", None))
#endif // QT_CONFIG(tooltip)
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"P\u00e1gina inicial", None))
#if QT_CONFIG(tooltip)
        self.btn_registrations.setToolTip(QCoreApplication.translate("MainWindow", u"Ver todos os registros", None))
#endif // QT_CONFIG(tooltip)
        self.btn_registrations.setText(QCoreApplication.translate("MainWindow", u"Ver registros", None))
        self.lb_img_logo.setText("")
        self.lb_titulo_app.setText(QCoreApplication.translate("MainWindow", u"Cadastro de clientes", None))
    # retranslateUi

