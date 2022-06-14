class Abstract:
    def __new__(cls, *args, **kwargs):
        if cls.__name__ is Abstract.__name__:
            raise TypeError(f"Classe abstrata não deve ser instanciada diretamente!")
        return object.__new__(cls)
