from .Produto import Produto

class ProdutoEletronico(Produto):
    def __str__(self):
        return f"[Eletrônico] {super().__str__()}"
