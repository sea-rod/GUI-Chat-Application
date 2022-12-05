from PySide2.QtCore import QRunnable,Slot,Signal,QObject
from client_socket.client import Client


class WorkerSignal(QObject):
    result = Signal(str)
    error = Signal(str)


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
            while True:
                mess = self.client.receive()
                if not mess:
                    break
                if mess == "xxxclosedxxx":
                    self.signal.error.emit(mess)
                if mess == "xxxuserExistxxx":
                    raise Exception("User exists")
                self.signal.result.emit(mess)

        except ConnectionResetError:
            self.signal.error.emit("Server shut Down")

        except Exception as E:
            self.signal.error.emit("Connection Closed\n"+str(E))

