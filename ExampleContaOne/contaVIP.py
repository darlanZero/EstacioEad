from contaPoupanca import ContaCliente

class ContaVIP(ContaCliente):
    def __init__(self, numero, IOF, IR, valorInvestido, taxaRendimento):
        super().__init__(numero, IOF, IR, valorInvestido, taxaRendimento)

    def calculoRendimento(self): #2
        self.valorInvestido += (self.valorInvestido * self.taxaRendimento)
        self.valorInvestido = (self.valorInvestido - (self.taxaRendimento * self.IOF * self.IR))