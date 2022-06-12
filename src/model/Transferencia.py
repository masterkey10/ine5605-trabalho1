from model.ContaBancaria import ContaBancaria


class Transferencia:
    def __init__(self,
                 remetente: ContaBancaria,
                 destinatario: ContaBancaria,
                 valor: float):
         self._remetente = remetente
         self._destinatario = destinatario
         self._valor = valor

    @property
    def remetente(self) -> ContaBancaria:
        return self._remetente

    @property
    def destinatario(self) -> ContaBancaria:
        return self._destinatario

    @property
    def valor(self) -> float:
        return self._valor
