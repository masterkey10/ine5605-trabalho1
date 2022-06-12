from model.ContaBancaria import ContaBancaria
from model.Transferencia import Transferencia
from enums.TipoContaEnum import TipoContaEnum


class ContaCorrente(ContaBancaria):
    def __init__(self, cpf_titular: str):
        super().__init__(cpf_titular=cpf_titular)
        self._tipo_conta = TipoContaEnum.CONTA_CORRENTE

    @property
    def tipo_conta(self) -> TipoContaEnum:
        return self._tipo_conta

    def transferir(self, transferencia: Transferencia) -> Transferencia | None:
        if (transferencia.valor > self._saldo):
            return
        self._saldo -= transferencia.valor
        return transferencia
