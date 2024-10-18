from models.Cliente import CLiente
from database.db_queries import ConsultarBanco

class ClienteController:
    def salvar_cliente(self, nome, email, telefone):
        cliente = CLiente(None, nome, email, telefone)
        ConsultarBanco.inserir_cliente(cliente.nome, cliente.email, cliente.telefone)
        