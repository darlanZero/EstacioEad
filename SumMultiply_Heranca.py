class ClasseSomaMultiplica:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def somar(self):
        return self.a + self.b;

    def multiplica(self):
        return self.a * self.b;


class Derivada(ClasseSomaMultiplica):
    def subtrair(self):
        return self.a - self.b;

    def dividir(self):
        return self.a / self.b;


d = Derivada(int(input("Digite seu número: ")), int(input("Digite seu segundo número: ")))
print(f"A soma de seu primeiro número e o segundo número é {d.somar()}")
print(issubclass(Derivada, ClasseSomaMultiplica))
