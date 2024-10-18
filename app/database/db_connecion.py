import sqlite3
from app.utils.config import BANCO_DE_DADOS

class ConexaoBanco():
    def __init__(self):
        ...
        self.connection = sqlite3.connect(BANCO_DE_DADOS)
        self.cursor = self.connection.cursor()
        self.connection.close()

    def inserir_cliente(self, nome, email, telefone):
        self.conexao.cursor.execute(
            "INSERT INTO clientes (nome, email, telefone)"
            " VALUES (?, ?, ?)", (nome, email, telefone))
        self.conexao.connection.commit()
        self.conexao.cursor.close()
        