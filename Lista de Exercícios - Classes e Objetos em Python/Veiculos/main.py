from models.Veiculos import Veiculos
from models.CarroCombustao import CarroCombustao
from models.CarroEletrico import CarroEletrico
from models.CarroConvEletrico import CarroConvEletrico

voyage = Veiculos("BCE9D36", "Voyage", "Volkswagen", 2018, "Vermelho", 47793)


jetta_gli = CarroCombustao("JDM9D36", "Jetta GLI", "Volkswagen", 2025, "Vermelho", 250000, 
                           "Gasolina", 4, 5, 2000, "AT 7", 24)

tesla_model_s = CarroEletrico("JDN0A00", "Tesla Model S", "Tesla", 2021, "Branco", 950000, 
                            5, 4, 65, "Lítio", 491)

fusca_eletrico = CarroConvEletrico("IAA0D36", "Fusca 1600 Elétrico", "Volkswagen", 1975, "Azul", 70000, 
                           "Gasolina", 4, 5, 1600, "MT 4", 24, 65, "Lítio", 150)


print(fusca_eletrico)

fusca_eletrico.abastecer(10)