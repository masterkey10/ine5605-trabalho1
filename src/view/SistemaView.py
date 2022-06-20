from model.Singleton import Singleton
from config import Config
from exception.FaultyInputException import FaultyInputException


class SistemaView(Singleton):
    def __init__(self):
        pass

    def tela_inicial(self) -> int:
        print('--------- SISTEMA BANCÁRIO ---------')
        print('Escolha um módulo:')
        print('1 - Registro/Remoção/Consulta de Clientes')
        print('2 - Operaões de Contas')
        print('3 - Sair')

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
