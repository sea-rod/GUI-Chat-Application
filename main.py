import socket
from PySide2.QtCore import QThreadPool
from PySide2.QtWidgets import QApplication
from project.client_socket.client import Client
from project.GUI.gui import MainWindow
from project.receive import ReceiveMessage


class Main(MainWindow):
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()

    def connect_btn_clicked(self,check):
        if check:
            try:
                self.connect_btn.setText("Disconnect")
                host = self.host.text()
                port = int(self.port.text())
                ip = socket.gethostbyname(ip)
    
                self.client = Client(host,port)
                if self.client.connect():
                    print("Connection Sucessful")
                    self.worker = ReceiveMessage(self.client)
                    self.worker.signal.result.connect(self.print_mess)
                    self.threadpool.start(self.worker)
            
            except ValueError:
                self.print_mess("Port number should be a integer")

            except socket.gaierror:
                self.print_mess("Please a enter a valid ip or host name and try again")



        else:
            self.connect_btn.setText("Connect")
            self.client.send("xxxclosedxxx")
            self.client._flag = False
            self.client.close()
            del self.client

    def send_btn_clicked(self):
        self.client.send(self.mess.text())
        self.mess.clear()




app = QApplication([])

window = Main()
window.show()
app.exec_()