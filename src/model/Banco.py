from model.Cliente import Cliente
from model.ContaBancaria import ContaBancaria
from model.Singleton import Singleton

class Banco(Singleton):
    def __init__(self):
        self._clientes: list[Cliente] = []
        self._contas: list[ContaBancaria] = []
