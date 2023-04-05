class Pessoa:
    def __init__(self, nome, ender):
        self.set_nome(nome)
        self.set_ender(ender)

    def set_nome(self, nome):
        self.nome = nome

    def set_ender(self, ender):
        self.ender = ender

    def get_nome(self):
        return self.nome

    def get_ender(self):
        return self.ender


user_One = Pessoa(input("Nome:"), input("Endereço: "))
User_Two = Pessoa(input("Nome:"), input("Endereço: "))

print(f'Nome: {user_One.get_nome()}, Endereço: {user_One.get_ender()}')
print(f'Nome: {User_Two.get_nome()}, Endereço: {User_Two.get_ender()}')
