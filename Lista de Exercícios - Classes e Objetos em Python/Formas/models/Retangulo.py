class Retangulo:
    def __init__(self, base, altura):
        
        self.__base = base
        self.__altura = altura
        
    def calcular_area(self):
        return self.__base * self.__altura
    