from datetime import date


class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def apartirAnoNascimento(cls, nome, ano):
        return cls(nome, date.today().year - ano)

    # método estático: Verificar se é maior de idade
    @staticmethod
    def ifMaiorIdade(idade):
        return idade >= 18


p1 = Pessoa(input("Nome: "), int(input("Idade: ")))
print(f"A idade da primeira pessoa é {p1.idade} anos.")

p2 = Pessoa.apartirAnoNascimento(input("Nome: "), int(input("Ano de Nascimento: ")))
print(f"A idade da segunda pessoa é {p2.idade} anos.")

user = print(Pessoa.ifMaiorIdade(int(input("Digite sua idade: "))))

if user == False:
    print("Opa, parece que você é menor de idade")
else:
    print("Então tu é maior de idade. Bem vindo ao mundo adulto!")