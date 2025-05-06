''''
class ContaBancaria:
    def __init__(self, titular, saldo, limite, historico):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico

    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append(f"Depósito: R$ {valor:.2f}")
            return True
        else:
            print("Valor de depósito inválido.")
            return False
    
    def sacar(self, valor):
        if valor > 0 and valor <= self.saldo + self.limite:
            self.saldo -= valor
            self.historico.append(f"Saque: R$ {valor:.2f}")
            return True
        else:
            print("Valor de saque inválido.")
            return False
    
    def transferir(self, valor, conta_destino):
        if self.sacar(valor):
            conta_destino.depositar(valor)
            self.historico.append(f"Transferência: R$ {valor:.2f} para {conta_destino.titular}")
            return True
        else:
            print("Transferência não realizada.")
            return False
        
    def exibir_historico(self):
        print(f"Histórico de transações de {self.titular}:")
        for transacao in self.historico:
            print(transacao)
        print(f"Saldo atual: R$ {self.saldo:.2f}")
        print(f"limite: R$ {self.limite:.2f}")

# Exemplo de uso
conta1 = ContaBancaria("João", 1000, 500, [])
conta2 = ContaBancaria("Maria", 500, 300, [])

ContaBancaria.exibir_historico(conta1)
ContaBancaria.exibir_historico(conta2)

conta1.depositar(200)
conta1.sacar(100)   

conta1.transferir(300, conta2)
conta2.depositar(150)

ContaBancaria.exibir_historico(conta1)
ContaBancaria.exibir_historico(conta2)

'''

