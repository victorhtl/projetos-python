from conta import ContaCorrente, ContaPoupança
from cliente import Cliente


conta1 = ContaCorrente(1111, 22333)

cliente = Cliente('Victor', 22)

cliente.criar_conta(conta1)

cliente.conta.depositar(100)

cliente.conta.sacar(150)

cliente.mostrar_situacao()
