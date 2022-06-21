from abc import ABC, abstractmethod

from package.model.Abstract import Abstract


class ContaBancaria(ABC, Abstract):
    _id = 0

    def __init__(self, cpf_titular: str):
        self._saldo = 0
        self._cpf_titular = cpf_titular
        self._numero_conta = ContaBancaria._getNumeroConta()

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
    def transferir(self, transferencia):
        pass

    def depositar(self, valor: float) -> None:
        self._saldo += valor

    def receber(self, transferencia) -> None:
        self._saldo += transferencia.valor

    @classmethod
    def _getNumeroConta(cls) -> int:
        cls._id += 1
        return cls._id

