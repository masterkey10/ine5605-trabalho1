from dataclasses import dataclass

from package.model.Cliente import Cliente
from package.model.ContaBancaria import ContaBancaria
from package.model.ContaCorrente import ContaCorrente
from package.model.ContaPoupanca import ContaPoupanca
from package.model.Singleton import Singleton


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

    @property
    def clientes(self) -> list[Cliente]:
        return self._clientes

    @property
    def contas(self) -> list[ContaBancaria]:
        return self._contas
