import sqlite3

class BancoDeDados:
    def __init__(self, database_file):
        self.conn = sqlite3.connect(database_file)
        self.cursor = self.conn.cursor()

        # Criar a tabela caso não exista
        self.criar_tabela_cliente_fisico()
        self.criar_tabela_cliente_juridico()
        
    def criar_tabela_cliente_fisico(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cliente_fisico(
                id_cliente INTEGER PRIMARY KEY AUTO_INCREMENT,
                tipo_pessoa VARCHAR(20),
                nome_completo VARCHAR(255),
                profissao VARCHAR(255),
                telefone VARCHAR(15),
                email VARCHAR(255),
                data_de_cadastro date,
                cpfj VARCHAR(14),
                rg VARCHAR(9),
                data_inicio date
            )
        ''')
        self.conn.commit()
    
    def criar_tabela_cliente_juridico(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS cliente_juridico(
                id_cliente INTEGER PRIMARY KEY AUTO_INCREMENT,
                tipo_pessoa VARCHAR(20),
                nome_completo VARCHAR(255),
                profissao VARCHAR(255),
                telefone VARCHAR(15),
                email VARCHAR(255),
                data_de_cadastro date,
                cpf_cnpj VARCHAR(14),
                ir VARCHAR(9),
                data_inicio date
            )
        ''')
        self.conn.commit()
        
    def inserir_cliente_fisico(self, cliente):
        with self.cursor() as cursor:
            cursor.execute('''
                INSERT INTO cliente_fisico (
                    tipo_pessoa, nome_completo, profissao, telefone, email,
                    data_cadastro, cpf, rg, data_nascimento
                ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            ''', (
                cliente.tipo_pessoa,
                cliente.nome_completo,
                cliente.profissao,
                cliente.telefone,
                cliente.email,
                cliente.data_cadastro,
                cliente.cpf,
                cliente.rg,
                cliente.data_nascimento
            ))
        self.conn.commit()
        
    def inserir_cliente_juridico(self, cliente):
        with self.cursor() as cursor:
            cursor.execute('''
            INSERT INTO cliente_juridico (
                tipo_pessoa, nome_completo, profissao, telefone, email, 
                data_cadastro, cnpj, ie, data_abertura
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (
            cliente.tipo_pessoa,
            cliente.nome_completo,
            cliente.profissao,
            cliente.telefone,
            cliente.email,
            cliente.data_cadastro,
            cliente.cnpj,
            cliente.ie,
            cliente.data_abertura
        ))
        self.conn.commit()
        