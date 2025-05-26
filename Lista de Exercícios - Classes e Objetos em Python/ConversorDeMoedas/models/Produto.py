class Produto:
    def __init__(self, nome: str, preco: float):
        self.__nome = nome
        self.__preco = preco
        self.__moeda = "BRL"

    def get_nome(self):
        return self.__nome

    def set_nome(self, nome):
        self.__nome = nome

    def get_preco(self):
        return self.__preco

    def set_preco(self, preco):
        self.__preco = preco

    def get_moeda(self):
        return self.__moeda

    def set_moeda(self, moeda):
        self.__moeda = moeda

    def __str__(self):
        return f"{self.__nome}: {self.__preco:.2f} {self.__moeda}"
