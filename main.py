import sys
from PySide6.QtWidgets import (
    QMainWindow, QApplication)  # type: ignore
from PySide6.QtGui import QIcon, QPixmap
from PySide6.QtCore import QSize

from app.ui.ui_main import Ui_MainWindow
from app.utils.variables import *


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)

        self.setup_connections_menu()
        self.set_images()
        
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
