from models.ContaBancaria import ContaBancaria
import time

conta = ContaBancaria("Guilherme", 1000, 500, [])
conta2 = ContaBancaria("João", 0, 0, [])


conta.depositar(150)
time.sleep(1)
conta.transferir(conta, 200, conta2)
time.sleep(2)
conta.sacar(100)
conta.exibirHistorico()

