from models.ProdutoAlimenticio import ProdutoAlimenticio
from models.ProdutoEletronico import ProdutoEletronico
from models.ConversorMoeda import ConversorMoeda
from models.MoedaInvalidaError import MoedaInvalidaError

def main():
    nome = input("Digite o nome do produto: ")
    preco = float(input("Digite o preço do produto em BRL: "))
    tipo = input("Digite o tipo do produto (alimenticio/eletronico): ").strip().lower()

    if tipo == "alimenticio":
        produto = ProdutoAlimenticio(nome, preco)
    elif tipo == "eletronico":
        produto = ProdutoEletronico(nome, preco)
    else:
        print("Tipo inválido.")
        return

    conversor = ConversorMoeda()

    try:
        convertido = conversor.converte_preco_para_usd(produto)
        if convertido:
            print("Preço convertido para USD.")
        else:
            print("Produto já estava em USD.")
    except MoedaInvalidaError as e:
        print(f"Erro na conversão: {e}")

    print("Informações do produto:")
    print(produto)

if __name__ == "__main__":
    main()
