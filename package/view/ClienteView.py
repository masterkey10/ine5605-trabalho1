from package.model.Singleton import Singleton


class ClienteView(Singleton):
    def __init__(self):
        pass

    def show_message(self, message: str):
        print(message)

