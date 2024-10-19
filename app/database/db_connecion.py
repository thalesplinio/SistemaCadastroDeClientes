import sqlite3
from app.utils.config import BANCO_DE_DADOS
from app.models import ClientePessoaFisica
from app.models import ClientePessoaJuridica

class BancoDeDados():
    def __init__(self):
        try:
            self.connection = sqlite3.connect(BANCO_DE_DADOS)
            self.cursor = self.connection.cursor()
            self.criar_tabela_cliente()
            self.criar_tabela_cliente_fisica()
            self.criar_tabela_cliente_juridica()
            self.criar_tabela_endereco_cliente()
        except sqlite3.Error as e:
            print(f"Erro ao conectar ao banco de dados: {e}")
    
    def criar_tabela_cliente(self):
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS cliente("
                "id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,"
                "tipo_pessoa VARCHAR(20),"
                "nome_completo VARCHAR(255),"
                "profissao VARCHAR(255),"
                "telefone VARCHAR(15),"
                "email VARCHAR(255),"
                "data_cadastro date"
            ")"
        )
        self.connection.commit()
        
    def criar_tabela_cliente_fisica(self):
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS cliente_fisica("
                "id_cliente INTEGER PRIMARY KEY,"
                "cpf VARCHAR(14),"
                "rg VARCHAR(9),"
                "data_nascimento date,"
                "FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente)"
            ")"
        )
        self.connection.commit()
        
    def criar_tabela_cliente_juridica(self):
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS cliente_juridica("
                "id_cliente INTEGER PRIMARY KEY,"
                "cnpj VARCHAR(14),"
                "ie VARCHAR(9),"
                "data_abertura date,"
                "FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente)"
            ")"
        )
        self.connection.commit()

    def criar_tabela_endereco_cliente(self):
        self.cursor.execute(
            f"CREATE TABLE IF NOT EXISTS endereco_cliente("
                "id_endereco_cliente INTEGER PRIMARY KEY AUTOINCREMENT,"
                "id_cliente INTEGER,"
                "cep VARCHAR(9),"
                "bairro VARCHAR(255),"
                "rua VARCHAR(100),"
                "cidade VARCHAR(35),"
                "estado CHAR(2),"
                "numero VARCHAR(10),"
                "complemento VARCHAR(255),"
                "FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente)"
            ");"
        )
        
    def inserir_cliente(self, cliente, endereco=None):
        with self.cursor() as cursor:
            cursor.execute("""
                INSERT INTO cliente (
                    tipo_pessoa, nome_completo, profissao, telefone, email, 
                    data_cadastro) 
                VALUES 
                    (?,?,?,?,?,?)""",
            (cliente.tipo_pessoa, cliente.nome_completo, cliente.profissao, 
            cliente.telefone, cliente.email, cliente.data_cadastro))
        self.connection.commit()

        if isinstance(cliente, ClientePessoaFisica):
            with self.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO cliente_fisico(
                        id_cliente, cpf, rg, data_nascimento)
                    VALUES(?,?,?,?)""",
                    ( self.cursor.lastrowid, cliente.cpf, cliente.rg, cliente.data_nascimento))
        if isinstance(cliente, ClientePessoaJuridica):
            with self.cursor() as cursor:
                cursor.execute("""
                    INSERT INTO cliente_juridico(
                        id_cliente, cnpj, ir, data_abertura)
                    VALUES(?,?,?,?)""", 
                    ( self.cursor.lastrowid, cliente.cnpj, cliente.ie, cliente.data_abertura))
        self.connection.commit()
