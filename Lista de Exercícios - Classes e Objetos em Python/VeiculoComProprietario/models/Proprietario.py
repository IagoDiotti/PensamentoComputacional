import re

class Proprietario:
    def __init__(self, nome, cpf, veiculos):
        if not self.validar_cpf(cpf):
            raise ValueError("CPF inválido")
        self.nome = nome
        self.cpf = cpf
        self.veiculos = []  # Lista de placas de veículos
    

    def validar_cpf(self, cpf):
        cpf = re.sub(r'[^0-9]', '', cpf)
        return len(cpf) == 11

    def validar_placa(self, placa):
        padrao = r'^[A-Z]{3}[0-9][0-9A-Z][0-9]{2}$'
        return re.match(padrao, placa) is not None

    def adicionar_veiculo(self, placa):
        if self.validar_placa(placa):
            if placa not in self.veiculos:
                self.veiculos.append(placa)
            else:
                raise ValueError("Veículo já cadastrado para este proprietário.")
        else:
            raise ValueError("Placa inválida")

    def __str__(self):
        infos = f'{self.nome} (CPF: {self.cpf}) - Veículos: {', '.join(self.veiculos)}'
        return infos.rstrip(', ')
    

            
        
