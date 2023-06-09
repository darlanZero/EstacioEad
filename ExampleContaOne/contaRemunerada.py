from  Conta import Conta
from contaPoupanca import ContaPoupanca

class ContaRemuneradaPoupanca(Conta, ContaPoupanca):
    def __init__(self, taxaRemuneracao, clientes, numero, saldo, taxaremuneracao):
        Conta.__init__(self, clientes, numero, saldo)
        ContaPoupanca.__init__(self, taxaRemuneracao)
        self.taxaRemuneracao = taxaremuneracao

    def remuneraConta(self):
        self.saldo += self.saldo * (self.taxaRemuneracao/30)
        self.saldo -= self.taxaRemuneracao

cx = ContaRemuneradaPoupanca([c1, c2], 98939123, 1500.00, 0.03)
cx.remuneraConta()
print(cx.saldo)