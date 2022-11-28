# BY: SEAMUS.F.RODRIGUES
#
# This project can be used freely for all uses, as long as they maintain the
# respective credits only in the Python scripts.
#
# There are limitations on Qt licenses if you want to use your products
# commercially, I recommend reading them on the official website:
# https://doc.qt.io/qtforpython/licenses.html



import socket
from PySide2.QtCore import QThreadPool,Qt,QPropertyAnimation
from PySide2.QtWidgets import QApplication, QLabel, QMessageBox,QSizePolicy,QMainWindow
from PySide2.QtGui import QIcon
import res.res
from PySide2.QtUiTools import QUiLoader
from client_socket.client import Client
from receive import ReceiveMessage

loader = QUiLoader()
class Main(QMainWindow):
    '''
    Intialiezes the GUI part of the main window and connects the buttons to 
    their functions
    '''
    client:socket = None
    def __init__(self):
        super().__init__()
        self.ui = loader.load('./res/untitled.ui',None)
        self.ui.show()

        self.ui.client_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.client))
        self.ui.server_btn.clicked.connect(lambda:self.ui.stackedWidget.setCurrentWidget(self.ui.server))
        self.ui.menu_btn.clicked.connect(self.menu)
        self.threadpool = QThreadPool()
        
    def menu(self,chk):
        print(chk)
        if chk:
            self.animation = QPropertyAnimation(self.ui.side_main,b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(100)
            self.animation.setEndValue(200)
            self.animation.start()
            self.ui.menu_btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            self.ui.server_btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            self.ui.client_btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            
            
        else:
            self.animation = QPropertyAnimation(self.ui.side_main,b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(200)
            self.animation.setEndValue(100)
            self.animation.start()

            self.ui.menu_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
            self.ui.server_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
            self.ui.client_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
            


    def closeEvent(self, event) -> None:
        '''
        Overides the closeEvent of the PyQt module that is called when the    
        application is closed
        '''
        if self.client:
            self.connect_btn_clicked(False)


    def connect_btn_clicked(self,check):
        '''
        This is the callback function of the connect button
        '''
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


    def error_occur(self):
        self.connect_btn.setText("Connect")
        self.connect_btn.setChecked(False)

app = QApplication([])
app.setWindowIcon(QIcon(":/icons/main_icon"))
window = Main()
app.exec_()