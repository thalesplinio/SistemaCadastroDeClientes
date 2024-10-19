def setup_connections_menu(self, item1, item2, pag1, pag2):
    self.btn_home.clicked.connect(
        lambda: item1(pag1)
    )
    self.btn_registrations.clicked.connect(
        lambda: item2(pag2)
    )

def populate_combobox(self, lista, element):
    element(lista)
