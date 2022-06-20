from model.Cliente import Cliente
from model.Singleton import Singleton
from view.ClienteView import ClienteView

class ClienteController(Singleton):
    def __init__(self):
        self._clientes: list[Cliente] = []
        self._view: ClienteView = ClienteView()

    def initialize(self):
        pass
