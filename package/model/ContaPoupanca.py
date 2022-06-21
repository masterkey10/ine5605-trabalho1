from package.config import Config
from package.model.ContaBancaria import ContaBancaria
from package.model.Transferencia import Transferencia
from package.enums.TipoContaEnum import TipoContaEnum


class ContaPoupanca(ContaBancaria):
    def __init__(self, cpf_titular: str):
        super().__init__(cpf_titular=cpf_titular)
        self._tipo_conta = TipoContaEnum.CONTA_POUPANCA

    @property
    def tipo_conta(self) -> TipoContaEnum:
        return self._tipo_conta

    def transferir(self, transferencia: Transferencia) -> Transferencia | None:
        if (transferencia.valor > self._saldo) or \
           (transferencia.valor > Config.VALOR_MAX_TRANSFERENCIA_POUPANCA):
            return
        self._saldo -= transferencia.valor
        return transferencia
