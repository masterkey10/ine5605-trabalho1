from package.model.Singleton import Singleton
from package.model.Banco import Banco
from package.view.BancoView import BancoView
from package.config import Config
from package.exception.FaultyInputException import FaultyInputException


class BancoController(Singleton):
    def __init__(self, controlador_sistema):
        self._banco: Banco = Banco()
        self._view: BancoView = BancoView()
        self._sistema = controlador_sistema

    @property
    def banco(self) -> Banco:
        return self._banco

    def initialize(self):
        options = {
            1: self._show_clientes,
            2: self._registrar_cliente,
            3: self._remover_cliente,
            4: self._retornar
        }

        while True:
            try:
                options[self._view.tela_inicial()]()
            except KeyError:
                self._view.show_message(Config.OPCAO_INVALIDA)
            except FaultyInputException:
                pass

    def _show_clientes(self):
        for cliente in self._banco.clientes:
            pass

    def _registrar_cliente(self):
        pass

    def _remover_cliente(self):
        pass

    def _retornar(self):
        self._sistema.initialize()
