from app.models.Cliente import Cliente


class ClientePessoaJuridica(Cliente):
    def __init__(self, tipo_pessoa, nome_completo, profissao, cnpj, ie, telefone,
                email, data_abertura, data_cadastro):
        super().__init__(tipo_pessoa, nome_completo, profissao, cnpj, ie, telefone, 
                         email, data_abertura, data_cadastro)
        self.cnpj = cnpj
        self.ie = ie
        self.data_abertura = data_abertura
