from models.Livros import Livros

livro1 = Livros("Dom Casmurro", "Machado de Assis", 1899, 300, 1)
livro2 = Livros("O Senhor dos Anéis", "J.R.R. Tolkien", 1954, 1200, 1)
livro3 = Livros("1984", "George Orwell", 1949, 328, 1)

print("selecione o livro que deseja ler:")
print("1 - Dom Casmurro")  
print("2 - O Senhor dos Anéis")
print("3 - 1984")
opcao = int(input("Digite o número do livro: "))
if opcao == 1:
    livro1.exibir_informacoes()
    Livros.exibir_informacoes(self=livro1)
    print("Você está na página 1 do livro.")
    print("pressione 'a' para avançar, 'v' para voltar, 'e' para exibir informações ou 's' para sair.")
    opcao = input("")
    while opcao != 's':
        if opcao == 'a':
            Livros.avancar_pagina(self=livro1)
            print("Você avançou uma página.")
            print(f"Você está na página {livro1.pagina_atual} do livro.")
        elif opcao == 'v':
            Livros.voltar_pagina(self=livro1)
            print("Você voltou uma página.")
            print(f"Você está na página {livro1.pagina_atual} do livro.")
        elif opcao == 'e':
            Livros.exibir_informacoes(self=livro1)
        else:
            print("Opção inválida. Tente novamente.")
        opcao = input("")
    
    
elif opcao == 2:
    livro2.exibir_informacoes()
    Livros.exibir_informacoes(self=livro2)
    print("Você está na página 1 do livro.")
    print("pressione 'a' para avançar, 'v' para voltar, 'e' para exibir informações ou 's' para sair.")
    opcao = input("")
    while opcao != 's':
        if opcao == 'a':
            Livros.avancar_pagina(self=livro2)
            print("Você avançou uma página.")
            print(f"Você está na página {livro2.pagina_atual} do livro.")
        elif opcao == 'v':
            Livros.voltar_pagina(self=livro2)
            print("Você voltou uma página.")
            print(f"Você está na página {livro2.pagina_atual} do livro.")
        elif opcao == 'e':
            Livros.exibir_informacoes(self=livro2)
        else:
            print("Opção inválida. Tente novamente.")
        opcao = input("")
elif opcao == 3:   
    livro3.exibir_informacoes()
    Livros.exibir_informacoes(self=livro3)
    print("Você está na página 1 do livro.")
    print("pressione 'a' para avançar, 'v' para voltar, 'e' para exibir informações ou 's' para sair.")
    opcao = input("")
    while opcao != 's':
        if opcao == 'a':
            Livros.avancar_pagina(self=livro3)
            print("Você avançou uma página.")
            print(f"Você está na página {livro3.pagina_atual} do livro.")
        elif opcao == 'v':
            Livros.voltar_pagina(self=livro3)
            print("Você voltou uma página.")
            print(f"Você está na página {livro3.pagina_atual} do livro.")
        elif opcao == 'e':
            Livros.exibir_informacoes(self=livro3)
        else:
            print("Opção inválida. Tente novamente.")
        opcao = input("")