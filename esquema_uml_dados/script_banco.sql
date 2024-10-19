CREATE DATABASE banco_de_dados_cliente;
USE banco_de_dados_cliente;


CREATE TABLE IF NOT EXISTS cliente(
	id_cliente INTEGER PRIMARY KEY AUTO_INCREMENT,
	tipo_pessoa VARCHAR(20),
	nome_completo VARCHAR(255),
	profissao VARCHAR(255),
	cpf_cnpj VARCHAR(14),
	rg_ir VARCHAR(9),
	telefone VARCHAR(15),
	email VARCHAR(255),
	data_inicio date,
	data_de_cadastro date
);
INSERT INTO cliente VALUES(
	DEFAULT, "Pessoa Física", "Thales Plinio Alves Feitosa", 
	"analista de sistemas", "04703024101", "1773975", 
	"67 99336 7597", "thales@email.com", "1993-12-05", "2024-10-19");
SELECT * FROM cliente;

CREATE TABLE IF NOT EXISTS endereco_cliente(
	id_endereco_cliente INTEGER PRIMARY KEY AUTO_INCREMENT,
	id_cliente INTEGER,
	cep VARCHAR(9),
	bairro VARCHAR(255),
	rua VARCHAR(100),
	cidade VARCHAR(35),
	estado CHAR(2),
	numero VARCHAR(10),
	complemento VARCHAR(255),

	FOREIGN KEY(id_cliente) REFERENCES cliente(id_cliente)
);
INSERT INTO endereco_cliente VALUES(DEFAULT, 1, "79014070", "campo novo", "adis abeba","campo grande", "MS",  "263",  "casa");
SELECT * FROM endereco_cliente;


---------------------------------------------------------------------------------------------------------------------------------------
-- MODIFICAÇÃO APÓS A HERANÇA DOS DADOS
CREATE DATABASE banco_de_dados_cliente;
USE banco_de_dados_cliente;

CREATE TABLE cliente (
    id_cliente INTEGER PRIMARY KEY AUTO_INCREMENT,
    tipo_cliente VARCHAR(20),
    nome_completo VARCHAR(255),
    profissao VARCHAR(255),
    telefone VARCHAR(15),
    email VARCHAR(255),
    data_cadastro DATE
);
INSERT INTO cliente (tipo_pessoa, nome_completo, profissao, telefone, email, data_cadastro)
VALUES ('fisica', 'João da Silva', 'Programador', '11987654321', 'joao@email.com', '2023-11-22');

CREATE TABLE cliente_fisica (
    id_cliente_fisico INTEGER PRIMARY KEY,
    cpf VARCHAR(14),
    rg VARCHAR(9),
    data_nascimento DATE,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

CREATE TABLE cliente_juridica (
    id_cliente_juridico INTEGER PRIMARY KEY,
    cnpj VARCHAR(14),
    ie VARCHAR(9),
    data_abertura DATE,
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);

CREATE TABLE endereco_cliente (
    id_endereco_cliente INTEGER PRIMARY KEY AUTO_INCREMENT,
    id_cliente INTEGER,
    cep VARCHAR(9),
    bairro VARCHAR(255),
    rua VARCHAR(100),
    cidade VARCHAR(35),
    estado CHAR(2),
    numero VARCHAR(10),
    complemento VARCHAR(255),
    FOREIGN KEY (id_cliente) REFERENCES cliente(id_cliente)
);