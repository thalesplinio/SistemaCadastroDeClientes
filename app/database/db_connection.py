import sqlite3

class BancoDeDados:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.cursor = self.conn.cursor()

        # Criar a tabela caso não exista
        self.criar_tabela_tipo_cliente()
        self.cria_tipo_cliente_padrao()
        self.criar_tabela_endereco_cliente()
        self.criar_tabela_cliente()
        self.criar_tabela_cliente_fisico()
        self.criar_tabela_cliente_juridico()
        
    def criar_tabela_tipo_cliente(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS tipo_pessoa(
                id_tipo_pessoa INTEGER PRIMARY KEY AUTOINCREMENT,
                descricao VARCHAR(50)
            )
        ''')
        self.conn.commit()
        
    def cria_tipo_cliente_padrao(self):
        self.cursor.execute('''
            INSERT INTO tipo_pessoa (descricao) VALUES('Física'),('Jurídica')
        ''')
        self.conn.commit()
        
    def criar_tabela_endereco_cliente(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS endereco_cliente(
                id_endereco INTEGER PRIMARY KEY AUTOINCREMENT,
                cep VARCHAR(9),
                bairro VARCHAR(255),
                rua VARCHAR(100),
                cidade VARCHAR(35),
                estado CHAR(2),
                numero INTEGER,
                complemento VARCHAR(255)
            )
        ''')
        self.conn.commit()
        self.conn.commit()
        
    def criar_tabela_cliente(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cliente(
                id_cliente INTEGER PRIMARY KEY AUTOINCREMENT,
                nome_completo VARCHAR(255),
                profissao VARCHAR(150),
                telefone VARCHAR(15),
                email VARCHAR(255),
                tipo_pessoa INTEGER,
                id_endereco INTEGER,
                
                FOREIGN KEY (tipo_pessoa) REFERENCES tipo_pessoa(id_tipo_pessoa),
                FOREIGN KEY (id_endereco) REFERENCES endereco_cliente(id_endereco)
            )
        ''')
        self.conn.commit()
        
    def criar_tabela_cliente_fisico(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cliente_fisico(
                id_pessoa_fisica INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cliente INTEGER,
                cpf VARCHAR(11),
                rg VARCHAR(9),
                data_nascimento DATE,
                
                FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
            )
        ''')
        self.conn.commit()
        
    def criar_tabela_cliente_juridico(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cliente_juridico(
                id_pessoa_juridica INTEGER PRIMARY KEY AUTOINCREMENT,
                id_cliente INTEGER,
                cnpj VARCHAR(18),
                ie VARCHAR(9),
                data_fundacao DATE,
                
                FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
            )
        ''')
        self.conn.commit()

    def inserir_tipo_pessoa(self, descricao):
        self.cursor.execute("INSERT INTO tipo_pessoa (descricao) VALUES (?)", (descricao,))
        self.conn.commit()

    def inserir_endereco(self, cep, bairro, rua, cidade, estado, numero, complemento):
        self.cursor.execute("INSERT INTO endereco_cliente (cep, bairro, rua, cidade, estado, numero, complemento) VALUES (?, ?, ?, ?, ?, ?, ?)",
                            (cep, bairro, rua, cidade, estado, numero, complemento))
        self.conn.commit()
        return self.cursor.lastrowid  # Retorna o ID do último registro inserido

    def inserir_cliente(self, nome_completo, profissao, telefone, email, tipo_pessoa, endereco_id):
        self.cursor.execute("INSERT INTO cliente (nome_completo, profissao, telefone, email, tipo_pessoa, id_endereco) VALUES (?, ?, ?, ?, ?, ?)",
                            (nome_completo, profissao, telefone, email, tipo_pessoa, endereco_id))
        self.conn.commit()
        return self.cursor.lastrowid

    def inserir_cliente_fisico(self, cliente_id, cpf, rg, data_nascimento):
        self.cursor.execute("INSERT INTO cliente_fisico (id_cliente, cpf, rg, data_nascimento) VALUES (?, ?, ?, ?)",
                            (cliente_id, cpf, rg, data_nascimento))
        self.conn.commit()

    def inserir_cliente_juridico(self, cliente_id, cnpj, ie, data_fundacao):
        self.cursor.execute("INSERT INTO cliente_juridico (id_cliente, cnpj, ie, data_fundacao) VALUES (?, ?, ?, ?)",
                            (cliente_id, cnpj, ie, data_fundacao))
        self.conn.commit()
