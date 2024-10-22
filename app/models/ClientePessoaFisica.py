from Cliente import Cliente
import json

class ClienteFisico(Cliente):
    def __init__(self, nome_completo, profissao, telefone, email, cpf, rg, data_nascimento):
        super().__init__(nome_completo, profissao, telefone, email)
        self.cpf = cpf
        self.rg = rg
        self.data_nascimento = data_nascimento

    def get_dados_pessoa_fisica_dict(self):
        return {
            "nome_completo": self.nome_completo,
            "profissao": self.profissao,
            "telefone": self.telefone,
            "email": self.email,
            "cpf": self.cpf,
            "rg": self.rg,
            "data_nascimento": self.data_nascimento,
        }
        
    def __str__(self):
        return f"Nome: {self.nome_completo}\n" \
               f"CPF: {self.cpf}\n" \
               f"RG: {self.rg}\n" \
               f"Data de Nascimento: {self.data_nascimento}"


if __name__ == "__main__":
    cliente_fisico = ClienteFisico(
        "nome cliente1",
        "profissao 1",
        "67 99999 8888",
        "cliente1@email.com",
        "12345678901",
        "12345678",
        "1993-06-12",
    )
    dados_cliente_fisico = cliente_fisico.get_dados_pessoa_fisica_dict()
    dados_json = json.dumps(dados_cliente_fisico, indent=4)
    print(dados_json)
