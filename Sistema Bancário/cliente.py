class Cliente:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.conta = None

    def criar_conta(self, conta):
        self.conta = conta
        print(f'Conta de {self.nome} criada')

    def mostrar_situacao(self):
        print(f'\nTitular da conta: {self.nome}')
        print(f'Agencia: {self.conta.agencia}')
        print(f'Número da conta: {self.conta.nconta}')
        print(f'Saldo: R${self.conta.saldo}')
