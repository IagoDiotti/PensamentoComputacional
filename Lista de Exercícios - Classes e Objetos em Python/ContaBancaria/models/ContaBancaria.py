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
    from main import Banco
    
    
    
    
    def __init__(self, titular, saldo, limite, historico):
        '''
        construtor da classe ContaBancaria
        '''
        
        self.titular = titular
        self.saldo = saldo
        self.limite = limite
        self.historico = historico
    
    def depositar(self, valor, remetente = None):
        '''
        Método que realiza o depósito na conta bancária.
        Entrada: valor (float), remetente (str)
        return: true se a operação foi realizada com sucesso. False sea operação não foi realizada.
        '''
        # detecta se é uma tranferência
        op = 1
        if remetente != None:
            op = 2
        if valor > 0:
            self.saldo += valor
            self.historico.append({"operacao": op,
                                   "remetente": remetente,
                                   "destinatario": self.titular,
                                   "valor": valor,
                                   "saldo": self.saldo,
                                   "dataetempo": int(self.time.time())})
            return True
            print(f"Depósito de R${valor} realizado com sucesso.")
        else:
            print("O Valor de depósito deve ser maior que zero.")
            return False
    
    def sacar(self, valor, destinatario = None):
        '''
        Método que realiza o saque na conta bancária.
        Entrada: valor (float), destinatario (str)
        return: true se a operação foi realizada com sucesso. False sea operação não foi realizada.
        '''
          # detecta se é uma tranferência e muda a operação
        op = 0
        if destinatario != None:
            op = 2
        if valor <= self.saldo:
            self.saldo -= valor
            self.historico.append({"operacao": op,
                                   "remetente": self.titular,
                                   "destinatario": destinatario, 
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
        
    def transferir(self, destinatario, valor):
        '''
        Objetivo: Método para a transferência de valores entre contas bancárias.
        Entrada: valor (float), e o obj do destinatario (str)
        Saida: se ok ->True, se NOK -> False
        '''
        # se o saque ocorrer com sucesso
        if self.sacar(valor, destinatario.titular):
            # deposita na conta do destinatario
            destinatario.depositar(valor, self.titular)
            return True
        
            
   
    
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
    
    def criarConta(self, titular,):
        '''
        Método que cria uma nova conta bancária.
        Entrada: titular (str)
        Saida: retorna o objeto da conta bancária criada.
        '''
        return ContaBancaria(titular, 0, 0, [])
    
    
    
            
    
   