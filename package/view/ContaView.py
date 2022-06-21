from package.config import Config
from package.exception.FaultyInputException import FaultyInputException
from package.model.Singleton import Singleton


class ContaView(Singleton):
    def __init__(self):
        pass

    def tela_inicial(self) -> int:
        print('--------- SISTEMA BANCÁRIO ---------')
        print('Escolha uma operação:')
        print('1 - Depósito em Conta')
        print('2 - Transferência entre Conta')
        print('3 - Voltar')

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
