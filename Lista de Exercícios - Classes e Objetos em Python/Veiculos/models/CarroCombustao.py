from .Veiculos import Veiculos

class CarroCombustao(Veiculos):
    '''
    Classe que representa um carro a combustão, herda da classe Veiculos
    '''
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float,
                 combustivel: str, nPortas: int, nAssentos: int, nCilindrada: int, nCambio: str, nivel_combustivel: int) -> None:
        
        Veiculos.__init__(self, placa, modelo, marca, ano, cor, valor_fipe)
        
        self.__combustivel = combustivel
        self.__nPortas = nPortas
        self.__nAssentos = nAssentos
        self.__nCilindrada = nCilindrada
        self.__nCambio = nCambio
        self.__nivel_combustivel = nivel_combustivel
        
        
    def __str__(self) -> str:
        infos = super().__str__() # Reutiliza o método __str__ da classe pai
        ## Adiciona as informações específicas do carro a combustão
        infos += f"\nCombustível: {self.__combustivel}"
        infos += f"\nNúmero de Portas: {self.__nPortas}"
        infos += f"\nNúmero de Assentos: {self.__nAssentos}"
        infos += f"\nNúmero de Cilindrada: {self.__nCilindrada}"
        infos += f"\nCâmbio: {self.__nCambio}"
        infos += f"\nNível de Combustível: {self.__nivel_combustivel}\n"
        return infos       
    
    
    def abastecer(self, percentual_adicionado: int) -> bool:
        '''
        Método que abastece o carro a combustão
        Argumento: percentual (int): percentual de abastecimento
        Retorno: True se foi possível abastecer e False se não
        '''
        novo_percentual  = self.__nivel_combustivel + percentual_adicionado
        if novo_percentual <= 100:
            self.__nivel_combustivel = novo_percentual
            return True
        return False