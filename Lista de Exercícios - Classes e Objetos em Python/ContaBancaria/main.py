from models.ContaBancaria import ContaBancaria

Banco = []

def buscar_conta(titular):  
        for conta in Banco:
            if conta.getTitular() == titular:
                return conta
        return None

def buscar_conta_por_chave_pix(chave_pix):  
        for chave in conta.getChavesPix():
            if chave_pix in conta.getChavesPix():
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
    print("8 - Realizar transferência via PIX")
    print("9 - Sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        titular = input("Digite o nome do titular da conta: ")
        chave_pix = input("Digite chave pix que deseja cadastrar: ")
        Banco.append(ContaBancaria(titular, 0, 1000, [chave_pix], []))
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
            conta.sacar(valor)
        else:
            print("Conta não encontrada.")

    elif opcao == 4:
        titular = input("Digite o nome do titular da conta: ")
        conta = buscar_conta(titular)
        if conta:
            valor = float(input("Digite o valor que deseja depositar: "))
            conta.depositar(valor)
        else:
            print("Conta não encontrada.")
            
    elif opcao == 5:
        origem_nome = input("Digite o nome do titular da conta de origem: ")
        destino_nome = input("Digite o nome do destinatário: ")
        valor = float(input(f"Digite o valor que deseja transferir: "))
        conta_origem = buscar_conta(origem_nome)
        conta_destino = buscar_conta(destino_nome)
        if conta_origem and conta_destino and conta_origem != conta_destino:
            conta_origem.transferir(conta_destino, valor)
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
        origem_nome = input("Digite o nome do titular da conta: ")
        chave_transferencia = input("Digite a chave PIX que deseja realizar a transferência: ")
        valor = float(input("Digite o valor que deseja transferir: "))
        conta = buscar_conta_por_chave_pix(chave_transferencia)
        origem_nome.transferir(conta, valor)
    
    
    elif opcao == 9:
        print("Encerrando o programa. Até logo!")
        break

    else:
        print("Comando desconhecido. Tente novamente.")

