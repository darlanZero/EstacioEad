from Conta import Conta
from Clientes import cliente
from Extrato import gerarExtrato

cl1 = cliente((input("CPF do Titular: ")),
              input("Nome do titular: "),
              input("Endereço do Titular: "))

cl2 = cliente((input("CPF do Titular: ")),
              input("Nome do titular: "),
              input("Endereço do Titular: "))

co1 = Conta([cl1, cl2],
            int(input("Digite seu número: ")),
            int(input("Digite seu saldo: ")))

co1.gerarExtrato ()
co1.depositar(int(input("Quanto irá depositar? ")))
co1.sacar(int(input("Quanto irá sacar? ")))
co1.gerarExtrato ()
