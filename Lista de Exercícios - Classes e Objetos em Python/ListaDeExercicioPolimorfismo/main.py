from models.Caminhao import Caminhao
from models.Moto import Moto
from models.Carro import Carro
from models.CarroEletrico import CarroEletrico
import re

Corolla = Carro("Corolla", "Toyota", "ABC1234", 2020, "Preto", 12)
Factor_150 = Moto("Factor 150", "Yamaha", "XYZ5678", 2019, "Vermelho", 20)
f4000 = Caminhao("F4000", "Ford", "LMN9012", 2018, "Branco", 5)
tesla_model_s = CarroEletrico("Model S", "Tesla", "QRS3456", 2021, "Azul", 15, 60)

"""
distancia = int(input("Digite a distância percorrida (em km): "))
print(Carro.calcular_consumo(Corolla, distancia))
print(Moto.calcular_consumo(Factor_150, distancia))
print(Caminhao.calcular_consumo(f4000, distancia))
print(CarroEletrico.calcular_consumo(tesla_model_s, distancia))

print(tesla_model_s)

carga = int(input("Digite a carga da bateria com números inteiros baseado em porcentagem: "))

tesla_model_s.recarregar(carga)

print(tesla_model_s)
"""

print(tesla_model_s.get_placa())


while True:
    placa = input("Digite a nova placa do carro: ").replace(r"[a-z]", r"[A-Z]")
    if re.fullmatch(r"[A-Z]{3}[0-9]{4}", placa.upper()):
        tesla_model_s.set_placa(placa)
        print("Placa válida!")
        break
    else:
        print("Placa inválida! Certifique-se de usar o formato antigo: 3 letras seguidas de 4 números.")
print(tesla_model_s.get_placa())
