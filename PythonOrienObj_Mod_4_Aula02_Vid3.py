# Classe Salário
class Salário:
    def __init__(self, base, bonus):
        self.base = base
        self.bonus = bonus

    def salario_anual(self):
        return (self.base * 12) + self.bonus


class Empregado:
    def __init__(self, nome, idade, salario):
        self.nome = nome
        self.idade = idade
        self.salario_agregado = salario

    def salario_total(self):
        return self.salario_agregado.salario_anual()


salario = Salário(int(input("Salário base: ")), int(input("Bonus Salarial: ")))
emp = Empregado(input("Nome do Empregado: "), int(input("Idade do Empregado: ")), salario)
print(f"Seu salário total é: {emp.salario_total()}")
