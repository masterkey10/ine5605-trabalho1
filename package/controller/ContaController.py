from package.model.Singleton import Singleton
from package.model.ContaBancaria import ContaBancaria
from package.model.Cliente import Cliente
from package.config import Config
from package.exception.FaultyInputException import FaultyInputException
from package.view.ContaView import ContaView


class ContaController(Singleton):
    def __init__(self, controlador_sistema):
        self._contas: list[ContaBancaria] = []
        self._view: ContaView = ContaView()
        self._sistema = controlador_sistema

    def initialize(self):
        options = {
            1: self._transferir,
            2: self._depositar,
            3: self._retornar
        }

        while True:
            try:
                options[self._view.tela_inicial()]()
            except KeyError:
                self._view.show_message(Config.OPCAO_INVALIDA)
            except FaultyInputException:
                pass

    def criar_contas(self, cliente: Cliente):
        pass

    def remover_contas(self, cliente: Cliente):
        pass

    def _transferir(self):
        pass

    def _depositar(self):
        pass

    def _retornar(self):
        self._sistema.initialize()
