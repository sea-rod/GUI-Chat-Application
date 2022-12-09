from PySide2.QtCore import QRunnable
from server_socket.server import Server


class Create_Server(QRunnable):
    def __init__(self) -> None:
        super().__init__()

    def run(self):
        self.srv = Server()
        self.srv.listen()
        self.srv.accept()
