class Veiculos:
    def __init__(self, modelo, marca, placa, ano, cor):
        self.modelo = modelo
        self.marca = marca
        self.__placa = placa
        self.ano = ano
        self.cor = cor
        
    def get_placa(self):
        return self.__placa

    def set_placa(self, placa):
        
        self.__placa = placa
        
