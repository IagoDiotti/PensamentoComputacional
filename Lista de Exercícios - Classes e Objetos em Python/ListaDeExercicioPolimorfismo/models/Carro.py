from .Veiculos import Veiculos

class Carro(Veiculos):
    def __init__(self, modelo, marca, placa, ano, cor, km_litro):
        super().__init__(modelo, marca, placa, ano, cor)
        self.km_litro = km_litro
        
    def calcular_consumo(self, distancia) -> str:
        eficiencia = distancia / 12
        return f'eficiência do carro {self.modelo} é de {eficiencia:.2} km/litro'
    