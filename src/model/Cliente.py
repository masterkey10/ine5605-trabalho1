from enum.ProfissaoEnum import ProfissaoEnum


class Cliente:
    def __init__(self,
                 nome: str,
                 cpf: str,
                 telefone: str,
                 profissao: ProfissaoEnum):
        self._nome=nome
        self._cpf=cpf
        self._telefone=telefone
        self._profissao=profissao

    @property
    def nome(self) -> str:
        return self._nome

    @property
    def cpf(self) -> str:
        return self._cpf

    @property
    def telefone(self) -> str:
        return self._telefone

    @telefone.setter
    def telefone(self, telefone: str) -> None:
        self.telefone = telefone

    @property
    def profissao(self) -> ProfissaoEnum:
        return self._profissao

    @profissao.setter
    def profissao(self, profissao: ProfissaoEnum) -> None:
        self.profissao = profissao

