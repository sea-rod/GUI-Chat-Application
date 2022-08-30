from PySide2.QtCore import QRunnable,Slot,Signal,QObject
from client_socket.client import Client


class WorkerSignal(QObject):
    result = Signal(str)
    finished = Signal()


class ReceiveMessage(QRunnable):
    '''
    Receiver Thread
    A Thread that recevies the message from the server
    '''

    def __init__(self,client:Client) -> None:
        super().__init__()
        self.signal = WorkerSignal()
        self.client = client

    @Slot()
    def run(self) -> None:
        try:
            while self.client._flag:
                mess = self.client.receive()
                self.signal.result.emit(mess)

        except Exception as E:
            self.signal.result.emit("Connection Closed")

