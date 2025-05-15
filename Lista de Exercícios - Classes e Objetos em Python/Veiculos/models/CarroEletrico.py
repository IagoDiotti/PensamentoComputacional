from .Veiculos import Veiculos

class CarroEletrico(Veiculos):
    '''
    Classe que implementa métodos específicos de carros elétricos
    Argumento: Classe pai Veiculo
    '''
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float,
                 nAssentos: int, nPortas: int, nivel_bateria: int, tipo_bateria: str, autonomia: int) -> None:
        Veiculos.__init__(self, placa, modelo, marca, ano, cor, valor_fipe)
        self.__nAssentos = nAssentos
        self.__nPortas = nPortas
        self.__nivel_bateria = nivel_bateria
        self.__tipo_bateria = tipo_bateria
        self.__autonomia = autonomia
        
    def __str__(self) -> str:
        infos = super().__str__()
        infos += f"\nNúmero de Assentos: {self.__nAssentos}"
        infos += f"\nNúmero de Portas: {self.__nPortas}"
        infos += f"\nNível de Bateria: {self.__nivel_bateria}"
        infos += f"\nTipo de Bateria: {self.__tipo_bateria}"
        infos += f"\nAutonomia: {self.__autonomia}\n"
        return infos
    
    def get_nivel_bateria(self):
        ''' Retorna o nível da bateria do carro elétrico '''
        return self.__nivel_bateria
    
    def get_tipo_bateria(self,):
        ''' Altera o nível da bateria do carro elétrico '''
        return self.__tipo_bateria 
        
    def get_autonomia(self) :
        ''' Retorna a autonomia do carro elétrico '''
        return self.__autonomia
        