class Livro:
    def __init__(self, titulo, autor, ano_publicacao, numero_paginas, pagina_atual):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao
        self.numero_paginas = numero_paginas
        self.pagina_atual = pagina_atual

    def avancar_pagina(self):
        if self.pagina_atual < self.numero_paginas:
            self.pagina_atual += 1
        else:
            print("Você já está na última página do livro.")
    
    def voltar_pagina(self):
        if self.pagina_atual > 1:
            self.pagina_atual -= 1
        else:
            print("Você já está na primeira página do livro.")
            
    def exibir_informacoes(self):
        print(f"Título: {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"Ano de Publicação: {self.ano_publicacao}")
        print(f"Número de Páginas: {self.numero_paginas}")
        print(f"Página Atual: {self.pagina_atual}")
        
# Exemplo de uso da classe Livro


livro1 = Livro("Dom Casmurro", "Machado de Assis", 1899, 300, 1)
livro2 = Livro("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1200, 1)
livro3 = Livro("1984", "George Orwell", 1949, 328, 1)

print("selecione o livro que deseja ler:")
print("1 - Dom Casmurro")  
print("2 - O Senhor dos Anéis")
print("3 - 1984")
opcao = int(input("Digite o número do livro: "))
if opcao == 1:
    livro1.exibir_informacoes()
    Livro.exibir_informacoes(self=livro1)
    print("Você está na página 1 do livro.")
    print("pressione 'a' para avançar, 'v' para voltar, 'e' para exibir informações ou 's' para sair.")
    opcao = input("")
    while opcao != 's':
        if opcao == 'a':
            Livro.avancar_pagina(self=livro1)
            print("Você avançou uma página.")
            print(f"Você está na página {livro1.pagina_atual} do livro.")
        elif opcao == 'v':
            Livro.voltar_pagina(self=livro1)
            print("Você voltou uma página.")
            print(f"Você está na página {livro1.pagina_atual} do livro.")
        elif opcao == 'e':
            Livro.exibir_informacoes(self=livro1)
        else:
            print("Opção inválida. Tente novamente.")
        opcao = input("")
    
    
elif opcao == 2:
    livro2.exibir_informacoes()
    Livro.exibir_informacoes(self=livro2)
    print("Você está na página 1 do livro.")
    print("pressione 'a' para avançar, 'v' para voltar, 'e' para exibir informações ou 's' para sair.")
    opcao = input("")
    while opcao != 's':
        if opcao == 'a':
            Livro.avancar_pagina(self=livro2)
            print("Você avançou uma página.")
            print(f"Você está na página {livro2.pagina_atual} do livro.")
        elif opcao == 'v':
            Livro.voltar_pagina(self=livro2)
            print("Você voltou uma página.")
            print(f"Você está na página {livro2.pagina_atual} do livro.")
        elif opcao == 'e':
            Livro.exibir_informacoes(self=livro2)
        else:
            print("Opção inválida. Tente novamente.")
        opcao = input("")
elif opcao == 3:   
    livro3.exibir_informacoes()
    Livro.exibir_informacoes(self=livro3)
    print("Você está na página 1 do livro.")
    print("pressione 'a' para avançar, 'v' para voltar, 'e' para exibir informações ou 's' para sair.")
    opcao = input("")
    while opcao != 's':
        if opcao == 'a':
            Livro.avancar_pagina(self=livro3)
            print("Você avançou uma página.")
            print(f"Você está na página {livro3.pagina_atual} do livro.")
        elif opcao == 'v':
            Livro.voltar_pagina(self=livro3)
            print("Você voltou uma página.")
            print(f"Você está na página {livro3.pagina_atual} do livro.")
        elif opcao == 'e':
            Livro.exibir_informacoes(self=livro3)
        else:
            print("Opção inválida. Tente novamente.")
        opcao = input("")