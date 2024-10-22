from Cliente import Cliente
import json

class ClienteJuridico(Cliente):
    def __init__(self, nome_completo, profissao, telefone, email, cnpj, ie, data_fundacao):
        super().__init__(nome_completo, profissao, telefone, email)
        self.cnpj = cnpj
        self.ie = ie
        self.data_fundacao = data_fundacao
        
    def get_dados_pessoa_juridica_dict(self):
        return {
            "nome_completo": self.nome_completo,
            "profissao": self.profissao,
            "telefone": self.telefone,
            "email": self.email,
            "cnpj": self.cnpj,
            "ie": self.ie,
            "data_fundacao": self.data_fundacao,
        }

    def __str__(self):
        return f"Nome: {self.nome_completo},\n"\
               f"CPF: {self.cnpj},\n"\
               f"RG: {self.ie},\n"\
               f"Data Fundação: {self.data_fundacao},\n"\


if __name__ == "__main__":
    cliente_juridico = ClienteJuridico(
        "Tech Code",
        "Technology",
        "(67) 3333 3333",
        "tech_code@email.com",
        "10987654321",
        "87654321",
        "2000-06-12",
    )
    dados_cliente_juridico = cliente_juridico.get_dados_pessoa_juridica_dict()
    dados_json = json.dumps(dados_cliente_juridico, indent=4)
    print(dados_json)
