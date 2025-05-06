class Filmes:
    def __init__(self, titulo, genero, avaliacao):
        self.titulo = titulo
        self.genero = genero
        self.avaliacao = avaliacao
       

    def alterar_avaliacao(Filmes, nova_avaliacao):
        if 0 <= nova_avaliacao <= 10:
            Filmes.avaliacao = nova_avaliacao
            print(f"Avaliação do filme '{Filmes.titulo}' alterada para {Filmes.avaliacao}.")
        else:
            print("Erro: A avaliação deve estar entre 0 e 10.")

    def exibir_informacoes(Filmes):
        print(f"Título: {Filmes.titulo}")
        print(f"Gênero: {Filmes.genero}")
        print(f"Avaliação: {Filmes.avaliacao}")