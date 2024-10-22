class Cliente:
    def __init__(self, nome_completo, profissao, telefone, email):
        self.nome_completo = nome_completo
        self.profissao = profissao
        self.telefone = telefone
        self.email = email
        
    def __str__(self):
        return f"Nome: {self.nome_completo},\n"\
            f"Profissão: {self.profissao},\n"\
            f"Telefone: {self.telefone},\n"\
            f"Email: {self.email},\n"\


if __name__ == "__main__":
    cliente1 = Cliente(
        "nome cliente1",
        "profissao 1",
        "67 99999 8888",
        "cliente1@email.com",
    )
    print(cliente1)
