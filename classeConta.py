class ContaBancaria:
    def __init__(self, numero_conta, titular, saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
        else:
            print('Saldo insuficiente')
    
    def exibir_saldo(self):
        print(f'Saldo: {self.saldo}')
    
c1 = ContaBancaria('132432', 'CJ', 45000)
c1.depositar(300)
c1.exibir_saldo()
c1.sacar(150)
c1.exibir_saldo()
