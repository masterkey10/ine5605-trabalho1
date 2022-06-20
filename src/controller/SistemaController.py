from model.Singleton import Singleton
from config import Config
from controller.BancoController import BancoController
from controller.ClienteController import ClienteController
from controller.ContaController import ContaController
from exception.FaultyInputException import FaultyInputException
from view.SistemaView import SistemaView


class SistemaController(Singleton):
    def __init__(self):
        self._banco_controller: BancoController = BancoController()
        self._cliente_controller: ClienteController = ClienteController()
        self._conta_controller: ContaController = ContaController()
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
