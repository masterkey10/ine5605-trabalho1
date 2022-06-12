from model.ContaBancaria import ContaBancaria
from model.Transferencia import Transferencia


class ContaCorrente(ContaBancaria):
    def __init__(self, cpf_titular: str):
        super().__init__(cpf_titular=cpf_titular)

    def transferir(self, transferencia: Transferencia) -> Transferencia | None:
        pass
