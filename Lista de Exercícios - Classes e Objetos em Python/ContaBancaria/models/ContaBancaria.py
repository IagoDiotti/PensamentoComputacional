class ContaBancaria:
    """
    Classe que implementa métodos parar manipular uma conta bancária.
    Atributos:
    - titular: str
    - saldo: float
    - limite: float
    - historico: lista de dicionário
    
    OBS: Operações no histórico: 0 - sacar, 1- depositar, 2 - transferir
    
    """
    import time
    
    
    
    
    def __init__(self, titular, saldo, limite, historico):
        '''
        construtor da classe ContaBancaria
        '''
        
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico
    
    def depositar(self, valor):
        '''
        Método que realiza o depósito na conta bancária.
        Entrada: valor (float)
        return: true se a operação foi realizada com sucesso. False sea operação não foi realizada.
        '''
        if valor > 0:
            self.saldo += valor
            self.historico.append({"operacao": 1,
                                   "remetente": self.titular,
                                   "destinatario": self.titular,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "dataetempo": int(self.time.time())})
            return True
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O Valor de depósito deve ser maior que zero.")
            return False
    
    def sacar(self, valor):
        '''
        Método que realiza o saque na conta bancária.
        Entrada: valor (float)
        return: true se a operação foi realizada com sucesso. False sea operação não foi realizada.
        '''
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append({"operacao": 0,
                                   "remetente": self.titular,
                                   "destinatario": self.titular, 
                                   "valor": valor ,
                                   "saldo": self.saldo,
                                   "dataetempo": int(self.time.time())})
            return True
            print(f"Saque de R${valor} realizado com sucesso.")
        else: #sem grana em conta
            a = input(f"Você não tem saldo suficiente. Deseja usar o limite? (R${self.limite}) [s para sim]")
            if a == 's':
                if (self.saldo + self.limite) >= valor:
                    self.saldo -= valor
                    
                    print(f"Saque de R${valor} realizado com sucesso.")
                    return
                else:
                    print("saldo e limite insuficientes.")
            else:
                print("Operação de saque cancelado.")
                return False
        
    
    def exibirHistorico(self):
        '''
        Método que exibe o histórico de operações da conta bancária.
        '''
        print("Histórico de operações:")
        for transacao in self.historico:
            dt = self.time.localtime(transacao["dataetempo"])
            print("- Op:", transacao["operacao"],
                  "- Rementente:", transacao["remetente"],
                  "- Destinatário:", transacao["destinatario"],
                  "- Saldo:", transacao["saldo"], 
                  "- valor:", transacao["valor"],
                  "- Data e Tempo:", 
                  str(dt.tm_hour) + ":" + str(dt.tm_min) + ":" + str(dt.tm_sec) + " - " + str(dt.tm_mday) + "/" + str(dt.tm_mon) + "/" + str(dt.tm_year))
    
    def transferir(self, titular, valor, destinatario):
        '''
        Método que realiza a transferência de valores entre contas bancárias.
        Entrada: valor (float), destinatario (str)
        return: true se a operação foi realizada com sucesso. False sea operação não foi realizada.
        '''
        if valor <= self.saldo:
            titular.sacar(valor)
            destinatario.depositar(valor)
            self.historico.append({"operacao": 2,
                                   "remetente": self.titular,
                                   "destinatario": destinatario.titular, 
                                   "valor": valor ,
                                   "saldo": self.saldo,
                                   "dataetempo": int(self.time.time())})
        else: #sem grana em conta
            print("Saldo insuficiente para realizar a transferência")
