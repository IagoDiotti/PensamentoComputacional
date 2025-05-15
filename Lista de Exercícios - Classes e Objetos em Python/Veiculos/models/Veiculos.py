class Veiculos:
    '''
    Classe com as principais funcioalidades do sistema de veiculos, como pl
    '''    
    def __init__(self, placa: str, modelo: str, marca: str, ano: int, cor: str, valor_fipe: float) -> None:
        self.__placa = placa
        self.__modelo = modelo
        self.__marca = marca
        self.__ano = ano
        self.__cor = cor
        self.__valor_fipe = valor_fipe
    
    def __str__(self) -> str:
        ''' Retorna uma string com as informações do veiculo '''
        infos = f"\nPlaca: {self.__placa}"
        infos += f"\nModelo: {self.__modelo}"
        infos += f"\nMarca: {self.__marca}"
        infos += f"\nAno: {self.__ano}"
        infos += f"\nCor: {self.__cor}"
        infos += f"\nValor Fipe: {self.__valor_fipe}"
        return infos
        
        
    def get_placa(self) -> str:
        ''' Retorna a placa do veiculo '''
        return self.__placa
    
    def setValorFipe(self, valor: float) -> None:
        '''Método que altera o valor de fipe do veiculo
        
        Argumento: valor (float): novo valor da fipe
        saída: True se ok
        '''
        self.__valor_fipe = valor
        return True