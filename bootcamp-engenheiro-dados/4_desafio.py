import textwrap
from datetime import datetime

class Cliente:
    def __init__(self, nome, data_nascimento, cpf, endereco):
        self.nome = nome
        self.data_nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y")
        self.cpf = cpf
        self.endereco = endereco
        self.contas = []

    def realizar_transacao(self, conta, transacao):
        conta.registrar_transacao(transacao)

    def adicionar_conta(self, conta):
        self.contas.append(conta)


class Conta:
    def __init__(self, agencia, numero, cliente):
        self.agencia = agencia
        self.numero = numero
        self.cliente = cliente
        self.saldo = 0
        self.historico = Historico()
        cliente.adicionar_conta(self)

    def sacar(self, valor):
        if valor > self.saldo:
            print("\n@@@ Operação falhou! Saldo insuficiente. @@@")
            return False
        else:
            self.saldo -= valor
            self.historico.adicionar_transacao(Transacao('Saque', valor))
            print("\n=== Saque realizado com sucesso! ===")
            return True

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.adicionar_transacao(Transacao('Depósito', valor))
            print("\n=== Depósito realizado com sucesso! ===")
            return True
        else:
            print("\n@@@ Operação falhou! Valor inválido. @@@")
            return False

    def exibir_extrato(self):
        print("\n================ EXTRATO ================")
        for transacao in self.historico.transacoes:
            print(f"{transacao.tipo}:\tR$ {transacao.valor:.2f}")
        print(f"\nSaldo:\t\tR$ {self.saldo:.2f}")
        print("==========================================")


class Historico:
    def __init__(self):
        self.transacoes = []

    def adicionar_transacao(self, transacao):
        self.transacoes.append(transacao)


class Transacao:
    def __init__(self, tipo, valor):
        self.tipo = tipo
        self.valor = valor


def menu():
    menu = """\n
    ================ MENU ================
    [d]\tDepositar
    [s]\tSacar
    [e]\tExtrato
    [nc]\tNova conta
    [lc]\tListar contas
    [nu]\tNovo usuário
    [q]\tSair
    => """
    return input(textwrap.dedent(menu))


def criar_usuario(usuarios):
    cpf = input("Informe o CPF (somente número): ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        print("\n@@@ Já existe usuário com esse CPF! @@@")
        return

    nome = input("Informe o nome completo: ")
    data_nascimento = input("Informe a data de nascimento (dd-mm-aaaa): ")
    endereco = input("Informe o endereço (logradouro, nro - bairro - cidade/sigla estado): ")

    novo_usuario = Cliente(nome, data_nascimento, cpf, endereco)
    usuarios.append(novo_usuario)
    print("=== Usuário criado com sucesso! ===")


def filtrar_usuario(cpf, usuarios):
    for usuario in usuarios:
        if usuario.cpf == cpf:
            return usuario
    return None


def criar_conta(agencia, numero_conta, usuarios):
    cpf = input("Informe o CPF do usuário: ")
    usuario = filtrar_usuario(cpf, usuarios)

    if usuario:
        nova_conta = Conta(agencia, numero_conta, usuario)
        print("\n=== Conta criada com sucesso! ===")
        return nova_conta

    print("\n@@@ Usuário não encontrado, fluxo de criação de conta encerrado! @@@")


def listar_contas(contas):
    for conta in contas:
        linha = f"""\
            Agência:\t{conta.agencia}
            C/C:\t\t{conta.numero}
            Titular:\t{conta.cliente.nome}
        """
        print("=" * 100)
        print(textwrap.dedent(linha))


def main():
    LIMITE_SAQUES = 3
    AGENCIA = "0001"

    usuarios = []
    contas = []

    while True:
        opcao = menu()

        if opcao == "d":
            cpf = input("Informe o CPF do titular da conta: ")
            usuario = filtrar_usuario(cpf, usuarios)
            if usuario:
                valor = float(input("Informe o valor do depósito: "))
                usuario.contas[0].depositar(valor)

        elif opcao == "s":
            cpf = input("Informe o CPF do titular da conta: ")
            usuario = filtrar_usuario(cpf, usuarios)
            if usuario:
                valor = float(input("Informe o valor do saque: "))
                usuario.contas[0].sacar(valor)

        elif opcao == "e":
            cpf = input("Informe o CPF do titular da conta: ")
            usuario = filtrar_usuario(cpf, usuarios)
            if usuario:
                usuario.contas[0].exibir_extrato()

        elif opcao == "nu":
            criar_usuario(usuarios)

        elif opcao == "nc":
            numero_conta = len(contas) + 1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                contas.append(conta)

        elif opcao == "lc":
            listar_contas(contas)

        elif opcao == "q":
            break

        else:
            print("Operação inválida, por favor selecione novamente a operação desejada.")


main()
