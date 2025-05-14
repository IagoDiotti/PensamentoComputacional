from models.Veiculos import Veiculos
from models.CarroCombustao import CarroCombustao

voyage = Veiculos("BCE9D36", "Voyage", "Volkswagen", 2018, "Vermelho", 47793)


jetta_gli = CarroCombustao("JDM9D36", "Jetta GLI", "Volkswagen", 2025, "Vermelho", 250000, "Gasolina", 4, 5, 2000, "AT 7")
print(voyage)
print(jetta_gli)