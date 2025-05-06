from models.Filmes import Filmes

TesteFilme = Filmes("O Senhor dos Anéis", "Fantasia", "")

TesteFilme.exibir_informacoes()

print("Digite a para avaliar o filme ou n para não avaliar:")
avaliar = input()
if avaliar == "a":
    print("Digite a avaliação do filme (0 a 10):")
    nova_avaliacao = float(input())
    TesteFilme.alterar_avaliacao(nova_avaliacao)



TesteFilme.exibir_informacoes()

