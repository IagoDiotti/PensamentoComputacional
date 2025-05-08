from models.ContaBancaria import ContaBancaria

Banco = []

print("Bem-vindo ao sistema de contas bancárias!")
while True:
    print("Digite o número da opção desejada:")
    print("1 - Criar conta")
    print("2 - Exibir Saldo")
    print("3 - Sacar")
    print("4 - Depositar")
    print("5 - Realizar transferência")
    print("6 - Exibir histórico")
    print("7 - Excluir conta")
    opcao = int(input("Opção: "))
    
    if opcao == 1:
        titular = input("Digite o nome do titular da conta: ")
        Banco.append(ContaBancaria(titular, 0, 1000, []))
        print("Conta criada com sucesso!")
    elif opcao == 2:
        titular = input("Digite o nome do titular da conta que deseja verificar o saldo: ")
        for conta in Banco:
            if conta.titular == titular:
                print(f"O {titular} tem R${conta.saldo} em conta")
    elif opcao == 3:
        titular = input("Digite o nome do titular da conta:")
        valor = float(input("Digite o valor que deseja sacar: "))
        titular.sacar(valor)
        if titular.sacar == True:
            print("Saque realizado com sucesso ")
    elif opcao == 4:
        titular = input("Digite o nome do titular da conta que você deseja depositar: ")
        valor = float(input("Digite o valor que você deseja depositar: "))
        titular.depositar(valor)
    elif opcao == 5:
        titular = input("Digite o nome do titular da conta: ")
        destinatario = input("Digite o nome do destinatário: ")
        valor = float(input(f"Digite o valor que deseja tranferir para a conta de {destinatario}"))
        titular.transferir(destinatario, valor)
    elif opcao == 6:
        titular = input("Digite o nome do titular da conta que deseja verificar o histórico: ")
        titular.exibirHistorico()
    elif opcao == 7:
        titular = input("Digite o nome do titular da conta que deseja ser excluída: ")
        for conta in Banco:
            if conta.titular == titular:   
                while True:
                    if conta.saldo > 0:
                        print("Não é possível excluir uma conta com fundos.")
                        print(f"Saldo restante: {conta.saldo}")
                        destinatario = input("Insira uma conta para transferir o saldo restante: ")
                        titular.transferir(destinatario, conta.saldo)
                        if titular.transferir(destinatario, conta.saldo):
                            break
                        else:
                            print("Não foi possível prosseguir com o encerramento da conta")
                    elif conta.saldo < 0:
                        print("Não foi possível encerrar a conta devido ao saldo negativado.")
                        print(f"Deposite {abs(conta.saldo)} para regularizar a sua conta e seguir com a exclusão!")
                        resposta = input(f"Digite s para confirmar o depósito de {conta.saldo} e regularizar a sua conta: ")
                        if resposta == "s":
                            titular.deposito(conta.saldo * -1)
                            if titular.deposito(conta.saldo * -1):
                                break
                            else:
                                print("Não foi possível prosseguir com o encerramento da conta")
                        else:
                            break
                    elif conta.saldo == 0:
                        resposta = input("Digite [s] para confirmar a exclusão da conta: ")       
                        if resposta == "s":
                            Banco.remove(titular.ContaBancaria)
                        else:
                            print("Operação cancelada")
                    else:
                        print("Não foi possível concluir a operação, verifique os valores inseridos e tente novamente!")
                        break
    else:
        print("Comando desconhecido, encerrando programa!")