class Banco:
    def __init__(self):
        self.saldo = 0.0 
        self.extrato = []  
        self.saques_diarios = 0  
        self.limite_saques_diarios = 3 
        self.limite_saque = 500.0  

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor  
            self.extrato.append(f"Depósito: +R${valor:.2f}")  
            print(f"Depósito de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para depósito. Por favor, insira um valor positivo.")

    def sacar(self, valor):
        if self.saques_diarios >= self.limite_saques_diarios:
            print("Limite diário de saques atingido. Não é possível realizar mais saques hoje.")
        elif valor > self.limite_saque:
            print(f"O valor do saque não pode exceder R${self.limite_saque:.2f}.")
        elif valor > self.saldo:
            print("Saldo insuficiente para realizar o saque.")
        elif valor > 0:
            self.saldo -= valor 
            self.saques_diarios += 1  
            self.extrato.append(f"Saque: -R${valor:.2f}") 
            print(f"Saque de R${valor:.2f} realizado com sucesso.")
        else:
            print("Valor inválido para saque. Por favor, insira um valor positivo.")

    def mostrar_extrato(self):
        print("\nExtrato:")
        for operacao in self.extrato:  
            print(operacao)
        print(f"Saldo atual: R${self.saldo:.2f}\n")  


conta = Banco()
conta.depositar(1000)
conta.sacar(200)
conta.sacar(300)
conta.sacar(100)
conta.mostrar_extrato()
