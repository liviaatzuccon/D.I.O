usuarios = []
contas = []

def criar_usuario(nome, data_nascimento, cpf, endereco):
    cpf = cpf.replace(".", "").replace("-", "")  
    if any(usuario["cpf"] == cpf for usuario in usuarios):
        print("Erro: Já existe um usuário com esse CPF.")
        return
    
    novo_usuario = {"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco}
    usuarios.append(novo_usuario)
    print("Usuário criado com sucesso!")

def criar_conta_corrente(cpf):
    usuario = next((usuario for usuario in usuarios if usuario["cpf"] == cpf), None)
    
    if usuario is None:
        print("Erro: Usuário não encontrado.")
        return
    
    numero_conta = len(contas) + 1  # Número da conta é sequencial
    nova_conta = {"agencia": "0001", "numero_conta": numero_conta, "usuario": usuario}
    contas.append(nova_conta)
    print(f"Conta criada com sucesso! Agência: 0001, Número da Conta: {numero_conta}")

def depositar(saldo, valor, extrato):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
    else:
        print("Erro: Valor de depósito inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if valor > saldo:
        print("Erro: Saldo insuficiente.")
    elif valor > limite:
        print("Erro: Limite de saque excedido.")
    elif numero_saques >= limite_saques:
        print("Erro: Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
    else:
        print("Erro: Valor de saque inválido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, *, extrato):
    print("\n================ EXTRATO ================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("==========================================")

criar_usuario("Maria Silva", "01/01/1990", "123.456.789-00", "Rua A, 123 - Bairro X - Cidade/UF")
criar_conta_corrente("12345678900")

saldo = 0
extrato = ""
limite = 500
numero_saques = 0
LIMITE_SAQUES = 3

saldo, extrato = depositar(saldo, 1000, extrato)

saldo, extrato, numero_saques = sacar(saldo=saldo, valor=200, extrato=extrato, limite=limite, numero_saques=numero_saques, limite_saques=LIMITE_SAQUES)

exibir_extrato(saldo, extrato=extrato)
