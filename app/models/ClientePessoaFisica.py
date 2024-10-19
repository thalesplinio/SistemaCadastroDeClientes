from app.models.Cliente import Cliente


class ClientePessoaFisica(Cliente):
    def __init__(self, tipo_pessoa, nome_completo, profissao, cpf, rg, telefone,
                email, data_nascimento, data_cadastro):
        super().__init__(tipo_pessoa, nome_completo, profissao, cpf, rg, telefone, 
                         email, data_nascimento, data_cadastro)
        self.cpf = cpf
        self.rg = rg
        self.data_nascimento = data_nascimento
        