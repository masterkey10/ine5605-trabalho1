from dataclasses import dataclass


from model.Cliente import Cliente
from model.ContaBancaria import ContaBancaria
from model.ContaCorrente import ContaCorrente
from model.ContaPoupanca import ContaPoupanca
from model.Singleton import Singleton

@dataclass
class Registro:
    cliente: Cliente
    contaCorrente: ContaCorrente
    ContaPoupanca: ContaPoupanca

class Banco(Singleton):
    def __init__(self):
        self._clientes: list[Cliente] = []
        self._contas: list[ContaBancaria] = []

    def registrar(self, registro: Registro) -> bool:
        pass

    def remover(self, registro: Registro) -> bool:
        pass

    def get_registros_by_cliente(self, cliente: Cliente) -> Registro:
        pass

    def _check_for_duplicates(self, registro: Registro) -> bool:
        pass
