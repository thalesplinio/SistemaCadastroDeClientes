# from app.models.Cliente import Cliente
from Cliente import Cliente


class ClientePessoaJuridica(Cliente):
    def __init__(self, nome_completo, profissao, telefone, email, data_cadastro, cnpj, ie, data_abertura):
        super().__init__(nome_completo, profissao, telefone, email, data_cadastro)
        self.cnpj = cnpj
        self.ie = ie
        self.data_abertura = data_abertura
        
    def get_dados_pessoa_juridico_dict(self):
        return {
            "nome_completo": self.nome_completo,
            "profissao": self.profissao,
            "telefone": self.telefone,
            "email": self.email,
            "data_de_cadastro": self.data_cadastro,
            "cnpj": self.cnpj,
            "ie": self.ie,
            "data_de_abertura": self.data_abertura,
        }

    def __str__(self):
        return f"  Nome: {self.nome_completo}\n" \
               f"  CPF: {self.cnpj}\n" \
               f"  RG: {self.ie}\n" \
               f"  Data de Abertura: {self.data_abertura}"

if __name__ == "__main__":
    cliente_juridico = ClientePessoaJuridica(
        "Empresa XYZ",
        "Tecnologia",
        "(67) 98765-4321",
        "xyz_contato@hotmail.com",
        "2000-10-00",
        "12.345.678/0001-12",
        "123456789",
        "2000-00-00"
    )
    dados_cliente = cliente_juridico.get_dados_pessoa_juridico_dict()
    print(dados_cliente)
