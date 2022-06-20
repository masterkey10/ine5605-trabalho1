from model.Singleton import Singleton
from model.ContaBancaria import ContaBancaria
from view.ContaView import ContaView


class ContaController(Singleton):
    def __init__(self):
        self._contas: list[ContaBancaria] = []
        self._view: ContaView = ContaView()

    def initialize(self):
        pass
