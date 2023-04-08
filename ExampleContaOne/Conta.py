import datetime
from Extrato import Extrato

class Conta:
    def __init__(self, numero, clientes, saldo):
        self.clientes = clientes
        self.numero = numero
        self._saldo = saldo
        self.data_abertura = datetime.datetime.today()
        self.extrato = Extrato ()

        @property
        def saldo(self):
            return self._saldo

        @saldo.setter
        def saldo(self, saldo):
            if (self.saldo < 0):
                print("Saldo inválido")
            else:
                self._saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        self.extrato.transacoes.append(["DEPOSITO", valor, "Data", datetime.datetime.today()])

    def sacar(self, valor):
        if self.saldo < valor:
            return print("Operação Inválida.")
        else:
            self.saldo -= valor
            self.extrato.transacoes.append(["SAQUE", valor, "Data", datetime.datetime.today()])
            return print("Operação realizada com sucesso!")

    def transfereValor(self, contaDestino, valor):
        if self.saldo < valor:
            return print("Saldo insuficiente!")
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            self.extrato.transacoes.append(["TRANSFERENCIA", valor, "Data", datetime.datetime.today()])
            return print("Transferência Realizada!")

    def __gerarsaldo(self):
        print(f"Numero: {self.numero}\n"
              f"saldo: {self.saldo}")

