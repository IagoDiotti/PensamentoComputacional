from models.Retangulo import Retangulo
from models.Triangulo import Triangulo

triangulo_teste = Triangulo(3, 4)
retangulo_teste = Retangulo(3, 4)


print(f"Área do triângulo: {triangulo_teste.calcular_area()}")
print(f"Área do retângulo: {retangulo_teste.calcular_area()}")


