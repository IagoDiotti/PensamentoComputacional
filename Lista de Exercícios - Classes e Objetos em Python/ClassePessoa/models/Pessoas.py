class Pessoas:
    def __init__(self, nome, idade, altura):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def aniversario(self):
        print(f"Feliz aniversário, {self.nome}! Você agora tem {self.idade} anos.")
        self.idade += 1
    
    def exibir_informacoes(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade} anos")
        print(f"Altura: {self.altura} metros")
        