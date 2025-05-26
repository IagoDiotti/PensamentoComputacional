class MoedaInvalidaError(Exception):
    def __init__(self, moeda):
        super().__init__(f"Moeda inválida: {moeda}")
