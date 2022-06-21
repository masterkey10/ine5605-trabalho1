from package.model.Singleton import Singleton
from package.config import Config
from package.controller.BancoController import BancoController
from package.controller.ClienteController import ClienteController
from package.controller.ContaController import ContaController
from package.exception.FaultyInputException import FaultyInputException
from package.view.SistemaView import SistemaView


class SistemaController(Singleton):
    def __init__(self):
        self._banco_controller: BancoController = BancoController(self)
        self._cliente_controller: ClienteController = ClienteController(self)
        self._conta_controller: ContaController = ContaController(self)
        self._view: SistemaView = SistemaView()

        self.initialize()

    def initialize(self):
        options = {
            1: self._banco_controller.initialize,
            2: self._conta_controller.initialize,
            3: self._terminate,
        }

        while True:
            try:
                options[self._view.tela_inicial()]()
            except KeyError:
                self._view.show_message(Config.OPCAO_INVALIDA)
            except FaultyInputException:
                pass

    def _terminate(self):
        exit(0)
