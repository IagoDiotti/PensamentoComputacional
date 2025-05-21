from models.Veiculos import Carro, Moto, Caminhao, VeiculoEletrico
from models.Frota import Frota

# ========== EXERCÍCIO 1: Criando veículos ==========
v1 = Carro("Toyota", "Corolla", "ABC1234", 2020, "Preto")
v2 = Moto("Honda", "CG 160", "DEF5678", 2019, "Vermelha")
v3 = Caminhao("Volvo", "FH", "GHI9012", 2018, "Branco")
v4 = VeiculoEletrico("Tesla", "Model 3", "ELE1234", 2022, "Branco", 60)

# Lista de veículos
veiculos = [v1, v2, v3, v4]

# ========== Entrada comum para todos os exercícios ==========
distancia = float(input("Informe a distância (km): "))

# ========== EXERCÍCIO 1: Consumo individual com polimorfismo ==========
print("\n[Exercício 1] Consumo individual dos veículos:")
for v in veiculos:
    consumo = v.calcular_consumo(distancia)
    unidade = "litros" if not isinstance(v, VeiculoEletrico) else "kWh"
    print(f"{v} -> Consumo: {consumo:.2f} {unidade}")

# ========== EXERCÍCIO 2: Criando uma frota e consumo total ==========
frota = Frota()
frota.adicionar_veiculo(v1)
frota.adicionar_veiculo(v2)
frota.adicionar_veiculo(v3)
frota.adicionar_veiculo(v4)

print("\n[Exercício 2] Veículos na frota:")
frota.listar_veiculos()

consumo_total = frota.calcular_consumo_total(distancia)
print(f"\nConsumo total da frota para {distancia:.1f} km: {consumo_total:.2f} (litros e/ou kWh)")

# ========== EXERCÍCIO 3: Recarregando veículo elétrico ==========
print("\n[Exercício 3] Recarregando veículos elétricos:")

carga = float(input("Informe a carga a ser adicionada (kWh): "))
for v in veiculos:
    if isinstance(v, VeiculoEletrico):
        v.recarregar(carga)
        
# ========== EXERCÍCIO 4: Encapsulamento da placa ==========
print("\n[Exercício 4] Testando encapsulamento da placa:")

veiculo_teste = Carro("Fiat", "Uno", "XYZ0000", 2010, "Prata")
print(f"Placa inicial: {veiculo_teste.get_placa()}")

# Tentativa de alterar para placa válida
nova_placa = input("Informe uma nova placa válida (ABC1234): ")
veiculo_teste.set_placa(nova_placa)

# testando se a placa foi alterada
print(f"Placa final: {veiculo_teste.get_placa()}")


# ========== EXERCÍCIO 5: Comparação de veículos ==========
print("\n[Exercício 5] Comparando veículos pela placa:")

veiculos_comparacao = [
    Carro("Toyota", "Corolla", "ABC1234", 2020, "Preto"),
    Moto("Yamaha", "Factor", "XYZ0000", 2019, "Azul"),
    Caminhao("Mercedes", "Actros", "ABC1234", 2018, "Branco"),
    VeiculoEletrico("Tesla", "Model X", "TES2024", 2024, "Cinza", 60),
    Carro("Honda", "Civic", "XYZ0000", 2021, "Cinza")
]

# Verificando duplicatas
for i in range(len(veiculos_comparacao)):
    for j in range(i + 1, len(veiculos_comparacao)):
        if veiculos_comparacao[i] == veiculos_comparacao[j]:
            print(f"Veículos iguais encontrados:\n  {veiculos_comparacao[i]}\n  {veiculos_comparacao[j]}\n")



