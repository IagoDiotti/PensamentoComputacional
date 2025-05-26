from .Produto import Produto

class ProdutoAlimenticio(Produto):
    def __str__(self):
        return f"[Alimento] {super().__str__()}"
