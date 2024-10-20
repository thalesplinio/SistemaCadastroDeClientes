# from app.models.Cliente import Cliente
from Cliente import Cliente

class ClientePessoaFisica(Cliente):
    def __init__(self, nome_completo, profissao, telefone, email, data_cadastro, cpf, rg, data_nascimento):
        super().__init__(nome_completo, profissao, telefone, email, data_cadastro)
        self.cpf = cpf
        self.rg = rg
        self.data_nascimento = data_nascimento
        
    def get_dados_pessoa_fisica_dict(self):
        return {
            "nome_completo": self.nome_completo,
            "profissao": self.profissao,
            "telefone": self.telefone,
            "email": self.email,
            "data_de_cadastro": self.data_cadastro,
            "cpf": self.cpf,
            "rg": self.rg,
            "data_de_nascimento": self.data_nascimento,
        }

    def __str__(self):
        return f"  Nome: {self.nome_completo}\n" \
               f"  CPF: {self.cpf}\n" \
               f"  RG: {self.rg}\n" \
               f"  Data de Nascimento: {self.data_nascimento}"

if __name__ == "__main__":
    cliente_fisica = ClientePessoaFisica(
        "João da Silva",
        "Analista",
        "(11) 12345-6789",
        "joao@hotmail.com",
        "2000-10-00",
        "000-000-000-00",
        "9999999",
        "2000-00-00"
    )
    dados_cliente = cliente_fisica.get_dados_pessoa_fisica_dict()
    print(dados_cliente)