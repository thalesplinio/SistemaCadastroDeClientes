import json

class EnderecoCliente:
    def __init__(self, cep, bairro, rua, cidade, estado, numero, complemento):
        self.cep = cep
        self.bairro = bairro
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.numero = numero
        self.complemeneto = complemento

    def get_endereco_cliente_dict(self):
        return {
            "cep": self.cep,
            "bairro": self.bairro,
            "rua": self.rua,
            "cidade": self.cidade,
            "estado": self.estado,
            "numero": self.numero,
            "complemento": self.complemeneto,
        }
        
    def __str__(self):
        return f"""CEP: {self.cep}
               Bairro: {self.bairro}
               Rua: {self.rua}
               Cidade: {self.cidade}"""


if __name__ == "__main__":
    dados_endereco_cliente = EnderecoCliente(
        "12345-678",
        "Centro",
        "Avenida Brasil",
        "São Paulo",
        "SP",
        "123",
        "Apartamento 101",
    )
    endereco = dados_endereco_cliente.get_endereco_cliente_dict()
    dados_json = json.dumps(endereco, indent=4)
    print(dados_json)
