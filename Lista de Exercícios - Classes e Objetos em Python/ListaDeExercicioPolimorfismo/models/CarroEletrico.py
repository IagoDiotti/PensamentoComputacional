from .Veiculos import Veiculos

class CarroEletrico(Veiculos):
    def __init__(self, modelo, marca, placa, ano, cor, km_kwh, bateria):
        super().__init__(modelo, marca, placa, ano, cor)
        self.km_kwh = km_kwh
        self.bateria = bateria
        
    def calcular_consumo(self, distancia) -> str:
        eficiencia = distancia / self.km_kwh
        return f'eficiência do carro elétrico {self.modelo} é de {eficiencia:.2} kwh/km'
    
    def recarregar(self, carga) -> str:
        if carga + self.bateria > 100:
            return f'Não é possível carregar a bateria do carro elétrico {self.modelo} com {carga} kwh'
        else:
            self.bateria += carga
            return f'Carregando a bateria do carro elétrico {self.modelo} com {carga} %'
        
    def __str__(self) -> str:
        ''' Retorna uma string com as informações do veiculo '''
        infos = f"\nModelo: {self.modelo}"
        infos += f"\nMarca: {self.marca}"
        infos += f"\nPlaca: {Veiculos.get_placa(self)}"
        infos += f"\nAno: {self.ano}"
        infos += f"\nCor: {self.cor}"
        infos += f"\nkm por kwh: {self.km_kwh}"
        infos += f"\nBateria: {self.bateria}"
        return infos
    
    
    
    def set_placa(self, placa):
        Veiculos.set_placa(self, placa)