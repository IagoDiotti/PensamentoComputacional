from models.ContaBancaria import ContaBancaria

Banco = []

def buscar_conta(titular):
        for conta in Banco:
            if conta.titular == titular:
                return conta
        return None

print("Bem-vindo ao sistema de contas bancárias!")
while True:
    print("\nDigite o número da opção desejada:")
    print("1 - Criar conta")
    print("2 - Exibir Saldo")
    print("3 - Sacar")
    print("4 - Depositar")
    print("5 - Realizar transferência")
    print("6 - Exibir histórico")
    print("7 - Excluir conta")
    print("8 - Sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        titular = input("Digite o nome do titular da conta: ")
        Banco.append(ContaBancaria(titular, 0, 1000, []))
        print("Conta criada com sucesso!")

    elif opcao == 2:
        titular = input("Digite o nome do titular da conta: ")
        conta = buscar_conta(titular)
        if conta:
            print(f"O {titular} tem R${conta.saldo:.2f} em conta.")
        else:
            print("Conta não encontrada.")

    elif opcao == 3:
        titular = input("Digite o nome do titular da conta: ")
        conta = buscar_conta(titular)
        if conta:
            valor = float(input("Digite o valor que deseja sacar: "))
            if conta.sacar(valor):
                print("Saque realizado com sucesso.")
            else:
                print("Saldo insuficiente ou valor inválido.")
        else:
            print("Conta não encontrada.")

    elif opcao == 4:
        titular = input("Digite o nome do titular da conta: ")
        conta = buscar_conta(titular)
        if conta:
            valor = float(input("Digite o valor que deseja depositar: "))
            if conta.depositar(valor):
                print("Depósito realizado com sucesso.")
            else:
                print("Valor inválido.")
        else:
            print("Conta não encontrada.")

    elif opcao == 5:
        origem_nome = input("Digite o nome do titular da conta de origem: ")
        destino_nome = input("Digite o nome do destinatário: ")
        valor = float(input(f"Digite o valor que deseja transferir: "))
        conta_origem = buscar_conta(origem_nome)
        conta_destino = buscar_conta(destino_nome)
        if conta_origem and conta_destino and conta_origem != conta_destino:
            if conta_origem.transferir(conta_destino, valor):
                print("Transferência realizada com sucesso.")
            else:
                print("Transferência não realizada. Verifique o saldo ou o valor.")
        else:
            print("Conta de origem ou destino não encontrada, ou são a mesma conta.")

    elif opcao == 6:
        titular = input("Digite o nome do titular da conta: ")
        conta = buscar_conta(titular)
        if conta:
            conta.exibirHistorico()
        else:
            print("Conta não encontrada.")

    elif opcao == 7:
        titular = input("Digite o nome do titular da conta que deseja excluir: ")
        conta = buscar_conta(titular)

        if not conta:
            print("Conta não encontrada.")
            continue

        if conta.saldo > 0:
            print(f"Conta com saldo R${conta.saldo}. Transfira o valor antes de excluir.")
            destinatario_nome = input("Digite o nome da conta destinatária: ")
            destinatario = buscar_conta(destinatario_nome)
            if destinatario and destinatario != conta:
                if conta.transferir(destinatario, conta.saldo):
                    print("Transferência realizada.")
                else:
                    print("Erro na transferência. Conta não excluída.")
                    continue
            else:
                print("Destinatário inválido.")
                continue

        elif conta.saldo < 0:
            print(f"Conta com saldo negativo R${conta.saldo}. Deposite para regularizar.")
            resposta = input("Deseja regularizar e excluir a conta? (s/n): ")
            if resposta == 's':
                if conta.depositar(abs(conta.saldo)):
                    print("Conta regularizada.")
                else:
                    print("Erro no depósito.")
                    continue
            else:
                continue

        if conta.saldo == 0:
            resposta = input("Deseja realmente excluir a conta? (s/n): ")
            if resposta == 's':
                Banco.remove(conta)
                print("Conta excluída com sucesso.")
            else:
                print("Operação cancelada.")

    elif opcao == 8:
        print("Encerrando o programa. Até logo!")
        break

    else:
        print("Comando desconhecido. Tente novamente.")
