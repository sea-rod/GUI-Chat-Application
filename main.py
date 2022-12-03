# BY: SEAMUS.F.RODRIGUES
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html



import socket
from PySide2.QtCore import QThreadPool,Qt
from PySide2.QtWidgets import QApplication, QLabel, QMessageBox,QSizePolicy
from PySide2.QtGui import QIcon
import res.res
from GUI import intergui
from GUI.getname_interface import NameWind
from client_socket.client import Client
from create_server import Create_Server 
from receive import ReceiveMessage

class Main(intergui.intergui):
    '''
    Intialiezes the GUI part of the main window and connects the buttons to 
    their functions
    '''
    client:socket = None
    srv:socket = None
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat Application")
        self.threadpool = QThreadPool()
        
        
    
            


    def closeEvent(self, event) -> None:
        '''
        Overides the closeEvent of the PyQt module that is called when the    
        application is closed
        '''
        if self.client:
            self.connect_btn_clicked(False)
        if self.srv:
            self.srv.srv.terminate()


    def connect_btn_clicked(self,check):
        '''
        This is the callback function of the connect button
        '''
        if check:
            try:
                self.connect_btn.setText("Disconnect")
                host = self.host_id.text()
                port = int(self.port_id.text())
                host = socket.gethostbyname(host)
    
                self.client = Client(host,port)
                if self.client.connect():
                    self.namewid = NameWind()
                    self.namewid.closeEvent = self.get_name 
                    self.namewid.show()
                                       
                    
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
                del self.client
                self.error_occur()
    
    def get_name(self,e):
        self.name = self.namewid.name.text()
        self.client.send(self.name)

        
    
    def send_btn_clicked(self):
        '''
        This is the callback funciton of the send button
        '''
        if self.client and self.mess.text():
            mess = self.mess.text()
            lab = QLabel(mess)
            lab.setFont(self.font)
            lab.setMinimumHeight(30)
            lab.setSizePolicy(QSizePolicy.Minimum,QSizePolicy.Maximum)
            lab.setWordWrap(True)
            lab.setAlignment(Qt.AlignBottom | Qt.AlignRight)
            self.mess_layout.addWidget(lab,self.rw,1)
            self.rw += 1
            self.client.send(mess)
            self.mess.clear()


    def start_btn_clicked(self):
        self.srv = Create_Server()
        import socket
        self.threadpool.start(self.srv)
        host = socket.gethostbyname(socket.gethostname())
        port = self.srv.srv.get_port()
        self.hst_prt.setText(f"server started on {host}:{port}")
        self.host_id.setText(host)
        self.port_id.setText(str(port))
        self.connect_btn_clicked(True)

    def print_mess(self,mess):
        try:
            if mess == "xxxclosedxxx":
                raise Exception("User Exist")
            print(mess)
        except Exception as e:
            self.error_occur()
            self.client = None
            msg = QMessageBox()
            msg.setIcon(QMessageBox.Critical)
            msg.setText("ERROR")
            msg.setInformativeText(str(e))
            msg.setWindowTitle("Error")
            msg.exec_()


    def error_occur(self):
        self.connect_btn.setText("Connect")
        self.connect_btn.setChecked(False)

app = QApplication([])
app.setWindowIcon(QIcon(":/icons/main_icon"))
window = Main()
window.show()
app.exec_()