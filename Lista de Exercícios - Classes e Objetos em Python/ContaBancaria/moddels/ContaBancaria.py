class ContaBancaria:
    def __init__(self, titular, saldo, limite, historico):
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico
    
    def depositar(self, valor):
        if valor > 0:
            self.saldo += valor
            self.historico.append({})
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O Valor de depósito deve ser maior que zero.")
    
    def sacar(self, valor):
        if valor <= self.saldo:
            self.saldo -= valor
            
            print(f"Saque de R${valor} realizado com sucesso.")
        else: #sem grana em conta
            a = input(f"Você não tem saldo suficiente. Deseja usar o limite? (R${self.limite}) [s para sim]")
            if a == 's':
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    
                    print(f"Saque de R${valor} realizado com sucesso.")
                else:
                    print("saldo e limite insuficientes.")
            else:
                print("Operação de saque cancelado.")
                    
    
    
    def transferir():
    
    
    def exibirHistorico():
    
    
    def exibirSaldo():
        