from model.Singleton import Singleton
from config import Config
from exception.FaultyInputException import FaultyInputException


class BancoView(Singleton):
    def __init__(self):
        pass

    def tela_inicial(self) -> int:
        print('--------- SISTEMA BANCÁRIO ---------')
        print('Escolha uma operação:')
        print('1 - Consultar Clientes')
        print('2 - Registrar Cliente')
        print('3 - Remover Cliente')
        print('4 - Voltar')

        while True:
            print(Config.OPCAO)
            option = input(Config.PROMPT)
            key = self._parse_int(option)
            if key:
                return key
            print(Config.OPCAO_INVALIDA)
            raise FaultyInputException

    def show_message(self, message: str):
        print(message)

    def _parse_int(self, n: str) -> int | None:
        try:
            res = int(n)
            return res
        except ValueError:
            return None