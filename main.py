import socket
from PySide2.QtCore import QThreadPool,Qt
from PySide2.QtWidgets import QApplication, QLabel, QMessageBox
from client_socket.client import Client
from GUI.gui import MainWindow
from receive import ReceiveMessage


class Main(MainWindow):
    client = None
    def __init__(self):
        super().__init__()
        self.threadpool = QThreadPool()

    def closeEvent(self, event) -> None:
        if self.client:
            self.connect_btn_clicked(False)


    def connect_btn_clicked(self,check):
        if check:
            try:
                self.connect_btn.setText("Disconnect")
                host = self.host.text()
                port = int(self.port.text())
                host = socket.gethostbyname(host)
    
                self.client = Client(host,port)
                if self.client.connect():
                    print("Connection Sucessful")
                    self.worker = ReceiveMessage(self.client)
                    self.worker.signal.result.connect(self.print_mess)
                    self.threadpool.start(self.worker)
                else:
                    raise Exception("Host should not be empty")
            
            except ValueError:
                self.error_occur()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERROR")
                msg.setInformativeText("Port number should be a integer")
                msg.setWindowTitle("Error")
                msg.exec_()

            except socket.gaierror:
                self.error_occur()
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERROR")
                msg.setInformativeText("Please a enter a valid ip or host name and try again")
                msg.setWindowTitle("Error")
                msg.exec_()
            except Exception as e:
                self.error_occur()
                self.client = None
                msg = QMessageBox()
                msg.setIcon(QMessageBox.Critical)
                msg.setText("ERROR")
                msg.setInformativeText(str(e))
                msg.setWindowTitle("Error")
                msg.exec_()



        else:
            if self.client:
                self.client.send("xxxclosedxxx")
                self.client._flag = False
                self.client.close()
                del self.client
                self.error_occur()
    
    
    def send_btn_clicked(self):
        if self.client and self.mess.text():
            mess = self.mess.text()
            lab = QLabel(mess)
            lab.setFont(self.font)
            lab.setAlignment(Qt.AlignBottom | Qt.AlignRight)
            self.mess_layout.addWidget(lab,self.rw,1)
            self.rw += 1
            self.client.send(mess)
            self.mess.clear()


    def error_occur(self):
        self.connect_btn.setText("Connect")
        self.connect_btn.setChecked(False)


app = QApplication([])

window = Main()
window.show()
app.exec_()