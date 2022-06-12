from src.model.Cliente import Cliente
from src.model.ContaBancaria import ContaBancaria


class Banco:
    def __init__(self):
        self._clientes: list[Cliente] = []
        self._contas: list[ContaBancaria] = []

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Banco, cls).__new__(cls)
        return cls.instance
