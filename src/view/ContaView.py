from model.Singleton import Singleton


class ContaView(Singleton):
    def __init__(self):
        pass

    def show_message(self, message: str):
        print(message)

