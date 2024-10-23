from models.Cliente import CLiente
from database.db_connection import BancoDeDados

class ClienteController:
    def salvar_cliente(self, nome, email, telefone):
        cliente = CLiente(None, nome, email, telefone)
        BancoDeDados.inserir_cliente(cliente.nome, cliente.email, cliente.telefone)
        