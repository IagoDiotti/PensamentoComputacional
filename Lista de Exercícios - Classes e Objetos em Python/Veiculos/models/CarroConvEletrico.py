from .CarroCombustao import CarroCombustao
from .CarroEletrico import CarroEletrico

class CarroConvEletrico(CarroCombustao, CarroEletrico):
    '''
    Classe que implementa métodos específicos de um carro convertido em elétrico
    '''
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float,
                 combustivel: str, nPortas: int, nAssentos: int, nCilindrada: int, nCambio: str,
                 nivel_combustivel: int,  nivel_bateria: int, tipo_bateria: str, autonomia: int) -> None:
        
        CarroCombustao.__init__(self, placa, modelo, marca, ano, cor, valor_fipe,
                         combustivel, nPortas, nAssentos, nCilindrada,
                         nCambio, nivel_combustivel)
        
        CarroEletrico.__init__(self, placa, modelo, marca, ano, cor, valor_fipe, nAssentos, nPortas,
                               nivel_bateria, tipo_bateria, autonomia)
       
    def __str__(self) -> str:
        infos = super().__str__()
        infos += f"Nível de Bateria: {CarroEletrico.get_nivel_bateria(self)}"
        infos += f"\nTipo de Bateria: {CarroEletrico.get_tipo_bateria(self)}"
        infos += f"\nAutonomia: {CarroEletrico.get_autonomia}\n"
        return infos
        
    def abastecer(self, percentual_adicionado: int) -> str:
        '''
        Método abastecer desativado
        Argumentos: percentual (int): 
        Retorno: False, pois não pode mais abastecer
        '''
        print("Carro convertido para elétrico, não é mais possível abastecer")
        return False
    
        