import re

class Veiculo:
    def __init__(self, marca, modelo, placa, ano, cor):
        self.marca = marca
        self.modelo = modelo
        self.__placa = None
        self.set_placa(placa)
        self.ano = ano
        self.cor = cor

    def calcular_consumo(self, distancia):
        pass  # será sobrescrito

    def get_placa(self):
        return self.__placa

    def set_placa(self, nova_placa):
        if re.fullmatch(r"[A-Z]{3}\d{4}", nova_placa.upper()):
            self.__placa = nova_placa.upper()
        else:
            print(f"Placa inválida: {nova_placa}. Deve estar no formato ABC1234.")

    def __eq__(self, other):
        if isinstance(other, Veiculo):
            return self.get_placa() == other.get_placa()
        return False

    def __str__(self):
        return f"{self.__class__.__name__}: {self.marca} {self.modelo} ({self.__placa})"



class Carro(Veiculo):
    def calcular_consumo(self, distancia):
        eficiencia = 12  # km por litro
        return distancia / eficiencia

class Moto(Veiculo):
    def calcular_consumo(self, distancia):
        eficiencia = 20
        return distancia / eficiencia

class Caminhao(Veiculo):
    def calcular_consumo(self, distancia):
        eficiencia = 5
        return distancia / eficiencia


class VeiculoEletrico(Veiculo):
    def __init__(self, marca, modelo, placa, ano, cor, bateria):
        super().__init__(marca, modelo, placa, ano, cor)
        self._bateria = bateria
        
    def calcular_consumo(self, distancia):
        consumo_por_km = 0.15  # kWh por km
        return distancia * consumo_por_km

    def recarregar(self, carga):
        if carga + self._bateria > 100:
            print(f"{self} não pode carregar mais do que 100% da bateria.")
        else:
            print(f"{self} está recarregando...")
            self._bateria += carga
            print("Carregamento concluído.")
            print(f"carga atual: {self._bateria}%")

