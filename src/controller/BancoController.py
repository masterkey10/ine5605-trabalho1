from model.Singleton import Singleton
from model.Banco import Banco
from view.BancoView import BancoView
from config import Config
from exception.FaultyInputException import FaultyInputException


class BancoController(Singleton):
    def __init__(self):
        self._banco: Banco = Banco()
        self._view: BancoView = BancoView()

    @property
    def banco(self) -> Banco:
        return self._banco

    def initialize(self):
        options = {
            # 1: self._show_clientes,
            # 2: self._registrar_cliente,
            # 3: self._remover_cliente,
            # 4: return
        }

        while True:
            try:
                options[self._view.tela_inicial()]()
            except KeyError:
                self._view.show_message(Config.OPCAO_INVALIDA)
            except FaultyInputException:
                pass
