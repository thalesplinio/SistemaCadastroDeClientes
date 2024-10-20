class Endereco:
    def __init__(self, cep, bairro, rua, cidade, estado, numero,
                complemento):
        self.cep = cep
        self.bairro = bairro
        self.rua = rua
        self.cidade = cidade
        self.estado = estado
        self.numero = numero
        self.complemento = complemento
        
    def get_dados_endereco_dict(self):
        return {
            "cep": self.cep,
            "bairro": self.bairro,
            "rua": self.rua,
            "cidade": self.cidade,
            "estado": self.estado,
            "numero": self.numero,
            "complemento": self.complemento,
        }

    def __str__(self):
        return f"  cep: {self.cep}\n" \
               f"  bairro: {self.bairro}\n" \
               f"  rua: {self.rua}\n" \
               f"  cidade: {self.cidade}\n" \
               f"  estado: {self.estado}\n" \
               f"  numero: {self.numero}\n" \
               f"  complemento: {self.complemento}"
               
if __name__ == "__main__":
    endereco = Endereco(
        "12345-678",
        "Centro",
        "Avenida Brasil",
        "São Paulo",
        "SP",
        "123",
        "Apartamento 101",
    )
    dados_endereco = endereco.get_dados_endereco_dict()
    print(dados_endereco)
