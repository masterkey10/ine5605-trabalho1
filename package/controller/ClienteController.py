from package.model.Cliente import Cliente
from package.model.Singleton import Singleton
from package.config import Config
from package.exception.FaultyInputException import FaultyInputException
from package.view.ClienteView import ClienteView


class ClienteController(Singleton):
    def __init__(self, controlador_sistema):
        self._clientes: list[Cliente] = []
        self._view: ClienteView = ClienteView()
        self._sistema = controlador_sistema

    def initialize(self):
        options = {
            1: self._show_clientes,
            2: self._criar_cliente,
            3: self._remover_cliente,
            4: self._retornar,
        }

        while True:
            try:
                options[self._view.tela_inicial()]()
            except KeyError:
                self._view.show_message(Config.OPCAO_INVALIDA)
            except FaultyInputException:
                pass

    def _show_clientes(self):
        pass

    def _criar_cliente(self):
        pass

    def _remover_cliente(self):
        pass

    def _retornar(self):
        self._sistema.initialize()
