import sys
import re
import requests  # type: ignore
import threading
from PySide6.QtWidgets import (QMainWindow, QApplication)  # type: ignore
from PySide6.QtGui import QIcon, QPixmap  # type: ignore
from PySide6.QtCore import QSize  # type: ignore

from app.ui.ui_main import Ui_MainWindow
from app.utils.images_local import *
from app.database.db_connection import BancoDeDados
from app.models.EnderecoCliente import EnderecoCliente
from app.models.ClientePessoaFisica import ClientePessoaFisica
from app.models.ClientePessoaJuridica import ClientePessoaJuridico

from app.utils.config import DATA_FORMATADA
from app.utils.aditional_functions import (
    setup_connections_menu, populate_combobox,)


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.lb_date_time_local.setText(DATA_FORMATADA)

        setup_connections_menu(self,
                               self.stackedWidget.setCurrentWidget,
                               self.stackedWidget.setCurrentWidget,
                               self.page,
                               self.page_2
                               )
        self.set_images()

        # TESTANDO BANCO
        self.data_base = BancoDeDados()

        self.cb_tipo_pessoa.currentIndexChanged.connect(
            self.select_type_person)
        self.btn_save.clicked.connect(self.insert_data)
        # -------------------------------------------------------------------
        self.le_cep.textChanged.connect(self.worker_cep)
        # -------------------------------------------------------------------
        populate_combobox(
            self,
            self.data_base.select_talela_tipo_pessoa(),
            self.cb_tipo_pessoa.addItems
        )
        populate_combobox(
            self,
            ["AC", "AL", "AP", "AM", "CE", "ES", "BA", "GO", "MA",
             "MT", "MS", "MG", "PA", "PB", "PR", "PE", "PI", "RJ",
             "RN", "RS", "RO", "RR", "SC", "SP", "SE", "TO", "DF"],
            self.cb_estado.addItems
        )

    def limpa_campos(self):
        self.le_nome_completo.setText(""),
        self.le_profissao.setText(""),
        self.le_telefone.setText(""),
        self.le_email.setText(""),

        self.lb_title_type_person.setText("Tipo de Pessoa:")
        self.lb_message_user.setText("")

    def select_type_person(self, index):
        select_item = self.cb_tipo_pessoa.itemText(index)
        self.le_telefone.setInputMask("(000) 00000-0000;_")

        if select_item == "Pessoa Física":
            self.lb_title_cpf_cnpj.setText("CPF:")
            self.lb_title_rg_ie.setText("RG:")
            self.le_cpf.setInputMask("000.000.000-00;_")
            self.lb_title_date_birth.setText("Data de nascimento:")
            # reset de cores do combobox - apos selecionar pessoaZ
            self.lb_message_user.setText("")

        elif select_item == "Pessoa Jurídica":
            self.lb_title_cpf_cnpj.setText("CNPJ:")
            self.lb_title_rg_ie.setText("IE:")
            self.le_cpf.setInputMask("00.000.000/0000-00;_")
            self.lb_title_date_birth.setText("Data de abertura:")
            # reset de cores do combobox - apos selecionar pessoa
            self.lb_title_type_person.setStyleSheet("color: ;")
            self.lb_message_user.setText("")

    def valida_cep(self):
        # Remove hífens e preenche com zeros à esquerda
        self.cep = self.le_cep.text().replace('-', '').zfill(8)
        link_request = f"http://viacep.com.br/ws/{self.cep}/json/"

        try:
            response = requests.get(link_request)
            response.raise_for_status()  # Lança uma exceção para status HTTPs inválidos
            dict_content = response.json()

            if 'erro' not in dict_content:
                self.lb_title_cep.setText("CPF: cep encontrado ✅*")

                self.le_endereco.setText(dict_content.get('logradouro', ''))
                self.le_bairro.setText(dict_content.get('bairro', ''))
                self.le_cidade.setText(dict_content.get('localidade', ''))
                self.cb_estado.setCurrentText(dict_content.get('uf', ''))
            else:
                ...
        except requests.exceptions.RequestException as e:
            ...

    def worker_cep(self):
        t1 = threading.Thread(target=self.valida_cep)
        t1.start()

    def insert_data(self):
        tipo_pessoa = self.cb_tipo_pessoa.currentText()

        dados_endereco = {
            'cep': re.sub(r"[.\-]", "", self.le_cep.text()),
            'rua': self.le_endereco.text().upper().lower(),
            'bairro': self.le_bairro.text().upper().lower(),
            'cidade': self.le_cidade.text().upper().lower(),
            'estado': self.cb_estado.currentText(),
            'numero': self.le_numero_casa.text(),
            'complemento': self.le_complemento.text().upper().lower()
        }
        dados_pessoa_fisica = {
            'nome_completo': self.le_nome_completo.text().upper().lower(),
            'profissao': self.le_profissao.text().upper().lower(),
            'telefone': re.sub(r"[()\-\s]", "", self.le_telefone.text()),
            'email': self.le_email.text().upper().lower(),
        }
        dados_cpf_rg_nascimento = {
            # Remove pontos e hífens
            'cpf': re.sub(r"[.\-]", "", self.le_cpf.text()),
            'rg': re.sub(r"[.\-]", "", self.le_rg.text()),
            'data_nascimento': self.de_data_nascimento.text(),
        }
        dados_pessoa_juridica = {
            'nome_completo': self.le_nome_completo.text().upper().lower(),
            'profissao': self.le_profissao.text().upper().lower(),
            'telefone': re.sub(r"[()\-\s]", "", self.le_telefone.text()),
            'email': self.le_email.text().upper().lower(),
        }
        dados_cnpj_ie_data_fundacao = {
            'cnpj': re.sub(r"[.\-\\]", "", self.le_cpf.text()),
            'ie': re.sub(r"[.\-]", "", self.le_rg.text()),
            'data_fundacao': self.de_data_nascimento.text(),
        }

        if tipo_pessoa == "Pessoa Física":  # CLIENTE FISICO = 1
            # Inserir endereco
            endereco_id_1 = self.data_base.inserir_endereco(dados_endereco)

            # Inserir cliente físico
            cliente_id_1 = self.data_base.inserir_cliente(
                dados_pessoa_fisica, 1, endereco_id_1)

            # inserir cliente fisico
            self.data_base.inserir_cliente_fisico(
                cliente_id_1, dados_cpf_rg_nascimento)

            self.limpa_campos()

        elif tipo_pessoa == "Pessoa Jurídica":  # CLIENTE JURIDITO = 2
            # Inserir endereco
            endereco_id_1 = self.data_base.inserir_endereco(dados_endereco)

            # Inserir cliente físico
            cliente_id_1 = self.data_base.inserir_cliente(
                dados_pessoa_juridica, 1, endereco_id_1)

            # inserir cliente fisico
            self.data_base.inserir_cliente_juridico(
                cliente_id_1, dados_cnpj_ie_data_fundacao)

            self.limpa_campos()
        else:
            self.lb_title_type_person.setStyleSheet("color: red;")
            self.lb_title_type_person.setText("Tipo de Pessoa: *")
            self.lb_message_user.setStyleSheet("color: red;")
            self.lb_message_user.setText("Selecione o tipo de pessoa!!!")

    def set_images(self):
        # icon window
        app_icon = QIcon()
        app_icon.addFile(str(ICON_LOGO), QSize(16, 15))
        app.setWindowIcon(app_icon)

        # icons
        self.lb_img_logo.setPixmap(QPixmap(ICON_LOGO))
        self.lb_img_type_person.setPixmap(QPixmap(ICON_PERSON_TYPE))
        self.lb_img_name.setPixmap(QPixmap(ICON_NAME))
        self.lb_img_job.setPixmap(QPixmap(ICON_JOB))
        self.lb_img_cpf.setPixmap(QPixmap(ICON_CPF))
        self.lb_img_rg.setPixmap(QPixmap(ICON_RG))
        self.lb_img_email.setPixmap(QPixmap(ICON_EMAIL))
        self.lb_img_date.setPixmap(QPixmap(ICON_DATE))
        self.lb_img_phone.setPixmap(QPixmap(ICON_PHONE))
        self.lb_img_cep.setPixmap(QPixmap(ICON_CEP))
        self.lb_img_district.setPixmap(QPixmap(ICON_DISTRICT))
        self.lb_img_address.setPixmap(QPixmap(ICON_ADDRESS))
        self.lb_img_number.setPixmap(QPixmap(ICON_NUMBER))
        self.lb_img_complement.setPixmap(QPixmap(ICON_HOME))
        self.lb_img_uf.setPixmap(QPixmap(ICON_UF))
        self.lb_img_city.setPixmap(QPixmap(ICON_CITY))

        # btn icons
        self.btn_home.setIcon(QPixmap(ICON_HOME))
        self.btn_registrations.setIcon(QPixmap(ICON_REGISTRATION))
        self.btn_save.setIcon(QPixmap(ICON_SAVE))
        self.btn_clean_fields.setIcon(QPixmap(ICON_CLEAN_FIELDS))
        self.btn_remove_registration.setIcon(QPixmap(ICON_CLEAN_FIELDS))
        self.btn_update_table.setIcon(QPixmap(ICON_UPDATE_TABLE))
        self.btn_export_pdf.setIcon(QPixmap(ICON_EXPORT_PDF))
        self.btn_export_excel.setIcon(QPixmap(ICON_EXPORT_EXCEL))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    # app.exec()
    try:
        sys.exit(app.exec())
    except Exception:
        print('Fechando programa!')
