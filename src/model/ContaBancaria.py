from abc import ABC, abstractmethod

from model.Transferencia import Transferencia

class ContaBancaria(ABC):
    _saldo: float
    _cpf_titular: str
    _numero_conta: int

    @abstractmethod
    def __init__(self, cpf_titular: str):
        pass

    @property
    def cpf_titular(self) -> str:
        return self._cpf_titular

    @property
    def saldo(self) -> float:
        return self._saldo

    @property
    def numero_conta(self) -> int:
        return self._numero_conta

    @abstractmethod
    def transferir(self, transferencia: Transferencia) -> Transferencia | None:
        pass

    def depositar(self, valor: float) -> None:
        self._saldo += valor

    def receber(self, transferencia: Transferencia) -> None:
        self._saldo += transferencia.valor

