class Filme:
    def __init__(self, titulo, genero, avaliacao):
        self.titulo = titulo
        self.genero = genero
        self.avaliacao = avaliacao
       

    def avaliar(self):
        self.avaliacao = float(input("Digite a avaliação do filme (0 a 10): "))
        while self.avaliacao < 0 or self.avaliacao > 10:
            print("Avaliação inválida. Digite um valor entre 0 e 10.")
            self.avaliacao = float(input("Digite a avaliação do filme (0 a 10): "))

    def exibir_informacoes(filme):
        print(f"Título: {filme.titulo}")
        print(f"Gênero: {filme.genero}")
        print(f"Avaliação: {filme.avaliacao}")

TesteFilme = Filme("O Senhor dos Anéis", "Fantasia", "")

TesteFilme.avaliar()

TesteFilme.exibir_informacoes()

