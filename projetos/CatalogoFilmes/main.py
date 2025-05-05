tamanho = 0
nota_total = 0
def imprime_filmes(filmes):
  for filme in filmes:
    print(f"O filme {filme['nome']} recebeu a nota {filme['nota']} da critica")

def duplicidade(novo, filmes):
  for filme in filmes:
    if novo == filme['nome']:
      return True
    return False

filmes = []

op_string =    "Digite add para adicionar um filme"
op_string += "\n       rm para remover um filme"
op_string += "\n       ed para editar a nota de um filme"
op_string += "\n       sair para sair"

while True:
  print(op_string)
  operacao = input()

  if operacao == "add":
    nome = input("Digite o nome do filme:").strip()
    if nome == "":
      break
    if duplicidade(nome, filmes):
      print("O Filme", nome, "já foi cadastrado")
    else:
      nota = float(input("Digite a nota do filme"))
      tamanho += 1
      nota_total += nota
      filmes.append({'nome': nome, 'nota': nota})
    if tamanho > 1000:
      break
  elif operacao == "rm":
    nome = input("Digite o nome do filme que deseja remover:").strip()
    for filme in filmes:
      if nome == filme['nome']:
        filmes.remove(filme)
        tamanho -= 1
        nota_total -= filme['nota']
        print("Filme", nome, "removido com sucesso")
        break
  elif operacao == "sair":
    print("==========finalizando programa===========")
    break
  elif operacao == "ed":
    nome = input("Digite o nome do filme que deseja editar:").strip()
    for filme in filmes:
      if nome == filme['nome']:
        nota_total -= filme['nota']
        nota = float(input("Digite a nova nota do filme"))
        filme['nota'] = nota
        nota_total += nota
        print("Nota do filme", nome, "alterada com sucesso")
        break
  else:
    print("Operação inválida!")





if tamanho > 0:
  imprime_filmes(filmes)
  print("===========Resumo do catálogo===========")
  print("Possui", tamanho, "filmes e a média das notas é", round(nota_total/tamanho, 1))
  n = len(filmes)
  for i in range(n):
    for j in range(0, n-i-1):
        if filmes[j]['nota'] < filmes[j+1]['nota']:
            filmes[j], filmes[j+1] = filmes[j+1], filmes[j]

  print("\n--- Top 3 Melhores Filmes ---")
  for i in range(min(3, n)):
    print(f"{filmes[i]['nome']} - Nota: {filmes[i]['nota']}")


  n = len(filmes)
  for i in range(n):
    for j in range(0, n-i-1):
        if filmes[j]['nota'] > filmes[j+1]['nota']:
            filmes[j], filmes[j+1] = filmes[j+1], filmes[j]

  print("\n--- Top 3 Piores Filmes ---")
  for i in range(min(3, n)):
    print(f"{filmes[i]['nome']} - Nota: {filmes[i]['nota']}")
  print("===========Programa encerrado===========")
else:
  print("Não possui filmes cadastrados")