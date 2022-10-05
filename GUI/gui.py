from GUI.qss import style
from PySide2.QtCore import Qt
from PySide2.QtGui import QFont
from PySide2.QtWidgets import QGridLayout, QGroupBox,QMainWindow,QApplication,QPushButton,QLabel,QLineEdit,QHBoxLayout,QVBoxLayout,QWidget,QScrollArea,QInputDialog


class MainWindow (QMainWindow):
    '''
    Builds the GUI part of the chat application
    '''
    rw = 0
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat Application")
        self.resize(600,300)

        self.font = QFont()
        self.font.setPointSize(15)
        self.setFont(self.font)
        self.main_layout = QVBoxLayout()


        self.create_top_layout()

        self.mess_layout()
       
        self.create_bottom_layout()
        

        wid = QWidget()
        wid.setLayout(self.main_layout)
        self.setCentralWidget(wid)


        self.setStyleSheet(style)      
       


    def create_top_layout(self):
        '''
        Creates the top layer of the chat appplication
        '''
        port_label = QLabel("Port:")
        port_label.setContentsMargins(10,0,10,0)
        port_label.setFont(self.font)

        self.port = QLineEdit()
        

        host_label = QLabel("Host:")
        host_label.setContentsMargins(10,0,10,0)
        host_label.setFont(self.font)
        self.host = QLineEdit()

        self.connect_btn = QPushButton("Connect")
        self.connect_btn.setFixedSize(140,35)
        self.connect_btn.setCheckable(True)
        self.connect_btn.setFont(self.font)
        self.connect_btn.clicked.connect(self.connect_btn_clicked)


        top_layout = QHBoxLayout()
        top_layout.addWidget(port_label)
        top_layout.addWidget(self.port)
        top_layout.addWidget(host_label)
        top_layout.addWidget(self.host)
        top_layout.addWidget(self.connect_btn)
        top_layout.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        

        self.main_layout.addLayout(top_layout)


    def create_bottom_layout(self):
        '''
        Create the bottom layer of the application
        '''
        self.mess = QLineEdit(self)
        self.mess.setClearButtonEnabled(True)
        self.mess.setPlaceholderText("Enter your Message here")
        
        send_btn = QPushButton("Send")
        send_btn.clicked.connect(self.send_btn_clicked)
        send_btn.setFont(self.font)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.mess)
        bottom_layout.addWidget(send_btn)
        self.main_layout.addLayout(bottom_layout)
        

       
    def mess_layout(self):
        '''
        Create the message layout of the chat application
        '''
        self.mess_layout = QGridLayout()
        grp = QGroupBox()
        grp.setLayout(self.mess_layout)
        grp.setAlignment(Qt.AlignCenter)
        scroll = QScrollArea()
        scroll.setWidget(grp)
        scroll.setWidgetResizable(True)

        self.main_layout.addWidget(scroll)


    def print_mess(self,mess):
        '''
        Creates a QInputDialog (Input box) to get the name of the user
        '''
        if mess == "Enter your name":
            while True:
                name, ok = QInputDialog.getText(self,"Text Input",mess)
                if ok and name:
                    self.client.send(name)
                    break
        else:
            lab = QLabel(mess)
            lab.setFont(self.font)
            lab.setAlignment(Qt.AlignBottom)
            self.mess_layout.addWidget(lab,self.rw,0)
            self.rw += 1

    def connect_btn_clicked(self,check):...
    

    
    def send_btn_clicked(self):...
    


if __name__  == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()
    app.exec_()