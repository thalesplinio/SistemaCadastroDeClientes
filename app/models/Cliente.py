class Cliente:
    def __init__(
        self, tipo_pessoa, nome_completo, profissao, 
        telefone, email, data_cadastro):
        
        # self.id = id
        self.tipo_pessoa = tipo_pessoa  # "fisica" ou "juridica"
        self.nome_completo = nome_completo
        self.profissao = profissao
        self.telefone = telefone
        self.email = email
        self.data_cadastro = data_cadastro
        
    def __str__(self):
        return f"""Tipo: {self.tipo_pessoa},
            Nome: {self.nome_completo},
            Profissão: {self.profissao},
            Telefone: {self.telefone},
            Email: {self.email},
            Data de cadastro: {self.data_cadastro}
        """

if __name__ == "__main__":
    cliente1 = Cliente(
        "juridico",
        "thales",
        "analista",
        "67 99999 8888",
        "thales@email.com",
        "2024-10-19"
    )
    print(cliente1)
