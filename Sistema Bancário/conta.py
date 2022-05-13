from abc import abstractmethod


class Conta:
    def __init__(self, agencia, nconta, saldo=0):
        self.agencia = agencia
        self.nconta = nconta
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
        print('Saldo depositado')

    @abstractmethod
    def sacar(self, valor):
        pass


class ContaCorrente(Conta):
    def sacar(self, valor):
        if valor > (self.saldo + 100):
            print('Saldo Insuficiente')
        else:
            self.saldo -= valor
            print('Saque realizado com sucesso')


class ContaPoupança(Conta):
    def sacar(self, valor):
        if valor > self.saldo:
            print('Saldo Insuficiente')
        else:
            self.saldo -= valor
            print('Saque realizado com sucesso')
