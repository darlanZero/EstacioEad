from contaPoupanca import ContaCliente
from ContaComum import ContaComum
from ContaClienteRemunerada import ContaRemunerada
class banco():
    def __init__(self, codigo, nome):
        self.Codigo = codigo
        self.Nome = nome
        self.Contas = []

    def adicionaConta(self, contaCliente):
        self.Contas.append(contaCliente)

    def calculaRendimentoMensal(self): #7
        for c in self.Contas:
            c.CalculoRendimento()

    def imprimeSaldoContas(self):
        for c in self.Contas:


banco1 = banco(999, "Teste")
contaCliente1 = ContaCliente (1,0.01,0.1,1000,0.05)
contaComum1 = ContaComum(2,0.01,0.1,2000,0.05)
contaRemunerada1 = ContaRemunerada(3,0.01,0.1,2000,0.05)

banco1.adicionaConta(contaCliente1) #4
banco1.adicionaConta(contaComum1) #5
banco1.adicionaConta(contaRemunerada1) #6
banco1.calculaRendimentoMensal() #7
banco1.imprimeSaldoContas()

