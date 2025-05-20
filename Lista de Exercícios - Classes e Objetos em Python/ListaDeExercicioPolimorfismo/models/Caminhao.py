from .Veiculos import Veiculos

class Caminhao(Veiculos):
    def __init__(self, modelo, marca, placa, ano, cor, km_litro):
        super().__init__(modelo, marca, placa, ano, cor)
        self.km_litro = km_litro
        
    def calcular_consumo(self, distancia) -> str:
        eficiencia = distancia / self.km_litro
        return f'eficiência do caminhão {self.modelo} é de {eficiencia:.2} km/litro'