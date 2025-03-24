menu = """
---------------  MENU  ---------------

[1] Depositar
[2] Sacar
[3] Extrato
[4] Novo Cliente
[5] Nova Conta
[6] Listar Contas
[7] Filtrar Usuários
[0] Sair

-------------------------------------
=> """

def deposito(saldo, valor, extrato, /):
    if valor > 0:
        saldo += valor
        extrato += f"Depósito: R$ {valor:.2f}\n"
        print(f"Depósito de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado é inválido.")
    return saldo, extrato

def sacar(*, saldo, valor, extrato, limite, limite_saques, numero_saques):
    if valor > saldo:
        print("Operação falhou! Saldo insuficiente.")
    elif valor > limite:
        print("Operação falhou! O valor do saque excede o limite.")
    elif numero_saques >= limite_saques:
        print("Operação falhou! Número máximo de saques excedido.")
    elif valor > 0:
        saldo -= valor
        extrato += f"Saque: R$ {valor:.2f}\n"
        numero_saques += 1
        print(f"Saque de R$ {valor:.2f} realizado com sucesso!")
    else:
        print("Operação falhou! O valor informado não é válido.")
    return saldo, extrato, numero_saques

def exibir_extrato(saldo, /, *, extrato):
    print("\n====================EXTRATO====================")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print(f"\nSaldo: R$ {saldo:.2f}")
    print("===============================================")

def new_cliente(clientes):
    Cpf = input("Digite o seu CPF: ").strip()
    if not Cpf.isdigit():
        print("Erro: o CPF deve conter apenas números.")
        return
    for cliente in clientes:
        if cliente["Cpf"] == Cpf:
            print("Erro: CPF já cadastrado!")
            return
    nome = input("Digite seu nome completo: ").strip()
    data_nasc = input("Data de nascimento (DD/MM/AAAA): ").strip()
    logradouro = input("Logradouro: ").strip()
    bairro = input("Bairro: ").strip()
    cidade = input("Cidade: ").strip()
    estado = input("UF: ").strip()
    endereco = f"{logradouro}, {bairro}, {cidade}, {estado}"
    clientes.append({
        "Cpf": Cpf,
        "nome": nome,
        "data de nascimento": data_nasc,
        "endereco": endereco
    })
    print("Cliente cadastrado com sucesso!")

def new_conta(clientes, contas):
    cpf = input("Informe o CPF do usuário (somente números): ")
    usuario = next((u for u in clientes if u["Cpf"] == cpf), None)
    if not usuario:
        print("Usuário não encontrado! Cadastro de conta cancelado.")
        return
    numero_conta = len(contas) + 1
    conta = {"agencia": "0001", "numero_conta": numero_conta, "usuario": cpf}
    contas.append(conta)
    print(f"Conta {numero_conta} criada com sucesso para o usuário {usuario['nome']}!")

def listar_contas(contas, clientes):
    """Exibe todas as contas cadastradas com o nome do usuário."""
    if not contas:
        print("Nenhuma conta cadastrada.")
        return
    print("\n========== CONTAS CADASTRADAS ==========")
    for conta in contas:
        usuario = next((u for u in clientes if u["Cpf"] == conta["usuario"]), None)
        nome_usuario = usuario["nome"] if usuario else "Usuário não encontrado"
        print(f"Agência: {conta['agencia']} | Conta: {conta['numero_conta']} | CPF: {conta['usuario']} | Nome: {nome_usuario}")
    print("=========================================")

def filtrar_usuarios(clientes):
    """Busca um usuário pelo CPF e exibe seus dados."""
    cpf = input("Informe o CPF para busca: ").strip()
    usuario = next((u for u in clientes if u["Cpf"] == cpf), None)
    if usuario:
        print("\n========== DADOS DO USUÁRIO ==========")
        print(f"Nome: {usuario['nome']}")
        print(f"CPF: {usuario['Cpf']}")
        print(f"Data de nascimento: {usuario['data de nascimento']}")
        print(f"Endereço: {usuario['endereco']}")
        print("=======================================")
    else:
        print("Usuário não encontrado.")

def sair():
    print("Muito obrigado por utilizar nossos serviços, até logo!")
    exit()

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saques = 3
    clientes = []
    contas = []

    while True:
        opcao = input(menu)

        if opcao == "1":
            valor = float(input("Qual valor deseja depositar? "))
            saldo, extrato = deposito(saldo, valor, extrato)
        elif opcao == "2":
            valor = float(input("Informe o valor do saque: "))
            saldo, extrato, numero_saques = sacar(
                saldo=saldo, 
                valor=valor, 
                extrato=extrato, 
                limite=limite, 
                numero_saques=numero_saques, 
                limite_saques=limite_saques
            )
        elif opcao == "3":
            exibir_extrato(saldo, extrato=extrato)
        elif opcao == "4":
            new_cliente(clientes)
        elif opcao == "5":
            new_conta(clientes, contas)
        elif opcao == "6":
            listar_contas(contas, clientes)
        elif opcao == "7":
            filtrar_usuarios(clientes)
        elif opcao == "0":
            sair()

main()
