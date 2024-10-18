import sys
import requests
import threading
from PySide6.QtWidgets import (QMainWindow, QApplication)  # type: ignore
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize

from app.ui.ui_main import Ui_MainWindow
from app.utils.images_local import *
from app.database.db_connecion import ConexaoBanco


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setup_connections_menu()
        self.set_images()
        
        # TESTANDO BANCO
        self.data_base = ConexaoBanco()

        self.btn_save.clicked.connect(self.insert_data)
        
        self.populate_combobox_type_person()
        self.populate_combobox_uf()
        
        # -------------------------------------------------------------------
        self.le_cep.textChanged.connect(self.worker_cep)
        # -------------------------------------------------------------------

    def populate_combobox_type_person(self):
        list_types = ["Pessoa Física", "Pessoa Jurídica"]
        self.cb_tipo_pessoa.addItems(list_types)
        
    def populate_combobox_uf(self):
        list_ufs = [
            "AC","AL","AP","AM","CE","ES","BA","GO","MA",
            "MT","MS","MG","PA","PB","PR","PE","PI","RJ",
            "RN","RS","RO","RR","SC","SP","SE","TO","DF",
        ]
        self.cb_estado.addItems(list_ufs)
    
    def valida_cep(self):
        self.cep = self.le_cep.text().replace('-', '').zfill(8)  # Remove hífens e preenche com zeros à esquerda
        link_request = f"http://viacep.com.br/ws/{self.cep}/json/"

        try:
            response = requests.get(link_request)
            response.raise_for_status()  # Lança uma exceção para status HTTPs inválidos
            dict_content = response.json()

            if 'erro' not in dict_content:
                self.le_endereco.setText(dict_content.get('logradouro', ''))
                self.le_bairro.setText(dict_content.get('bairro', ''))
                self.le_cidade.setText(dict_content.get('localidade', ''))
                self.cb_estado.addItem(dict_content.get('uf', ''))
            else:
                print("CEP não encontrado")
        except requests.exceptions.RequestException as e:
            print(f"Erro na requisição: {e}")
    
        
    def worker_cep(self):
        t1 = threading.Thread(target=self.valida_cep)
        t1.start()
    
    def insert_data(self):
        self.nome_completo = self.le_nome_completo.text().upper().lower()
        
        print(self.nome_completo)
          
    def setup_connections_menu(self):
        self.btn_home.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page)
        )
        self.btn_registrations.clicked.connect(
            lambda: self.stackedWidget.setCurrentWidget(self.page_2)
        )
        
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
        self.lb_img_address.setPixmap(QPixmap(ICON_ADDRESS))
        self.lb_img_number.setPixmap(QPixmap(ICON_NUMBER))
        self.lb_img_uf.setPixmap(QPixmap(ICON_UF))
        self.lb_img_city.setPixmap(QPixmap(ICON_CITY))

        # btn icons
        self.btn_home.setIcon(QPixmap(ICON_HOME))
        self.btn_registrations.setIcon(QPixmap(ICON_REGISTRATION))
        self.btn_save.setIcon(QPixmap(ICON_SAVE))
        self.btn_clean_fields.setIcon(QPixmap(ICON_CLEAN_FIELDS))
        self.btn_remove_registration.setIcon(QPixmap(ICON_CLEAN_FIELDS))
        self.btn_update_table.setIcon(QPixmap(ICON_UPDATE_TABLE))
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    # app.exec()
    try:
        sys.exit(app.exec())
    except Exception:
        print('Fechando programa!')
