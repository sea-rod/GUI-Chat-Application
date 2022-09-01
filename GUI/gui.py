from PySide2.QtCore import Qt
from PySide2.QtGui import QFont,QPalette,QColor
from PySide2.QtWidgets import QGroupBox,QMainWindow,QApplication,QPushButton,QLabel,QLineEdit,QHBoxLayout,QVBoxLayout,QWidget, QListView,QScrollArea


class MainWindow (QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Chat Application")
        self.resize(500,300)

        self.font = QFont()
        self.font.setPointSize(17)
        self.setFont(self.font)
        self.main_layout = QVBoxLayout()

        self.sty = '''background:qlineargradient(x1:0, y1:0, x2:2, y2:1,stop:0.1 #CBD4C2, stop: 1 #637074,stop:1 rgb(0, 0, 17));
                      color:rgb(0, 0, 17);'''

        self.create_top_layout()

        self.mess_layout()
       
        self.create_bottom_layout()
        

        wid = QWidget()
        wid.setLayout(self.main_layout)
        self.setCentralWidget(wid)


        self.setStyleSheet('''background: qlineargradient(x1:0, y1:0, x2:2, y2:1,
                              stop:0.2 rgb(21, 30, 63), stop: 0.4 rgb(0, 0, 17), stop:1 rgb(99, 112, 116));
                              color:rgb(225, 228, 255)''')      
       


    def create_top_layout(self):
        port_label = QLabel("Port:")
        port_label.setContentsMargins(10,0,10,0)
        port_label.setStyleSheet(self.sty)
        port_label.setFont(self.font)
        port_label.resize(40,10)

        self.port = QLineEdit()
        

        host_label = QLabel("Host:")
        host_label.setStyleSheet(self.sty)
        host_label.setContentsMargins(10,0,10,0)
        host_label.setFont(self.font)
        self.host = QLineEdit()

        self.connect_btn = QPushButton("Connect")
        self.connect_btn.setFixedSize(140,35)
        self.connect_btn.setCheckable(True)
        self.connect_btn.setStyleSheet(self.sty)
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
        self.mess = QLineEdit(self)
        self.mess.setClearButtonEnabled(True)
        self.mess.setPlaceholderText("Enter your Message here")
        
        send_btn = QPushButton("Send")
        send_btn.clicked.connect(self.send_btn_clicked)
        send_btn.setStyleSheet(self.sty)
        send_btn.setFont(self.font)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.mess)
        bottom_layout.addWidget(send_btn)
        self.main_layout.addLayout(bottom_layout)
        

       
    def mess_layout(self):
        self.mess_layout = QVBoxLayout()

        grp = QGroupBox()
        grp.setLayout(self.mess_layout)
        grp.setAlignment(Qt.AlignCenter)
        scroll = QScrollArea()
        scroll.setWidget(grp)
        scroll.setWidgetResizable(True)

        self.main_layout.addWidget(scroll)


    def print_mess(self,mess):
        lab = QLabel(mess)
        lab.setFont(self.font)
        lab.setStyleSheet("background:transparent")
        lab.setAlignment(Qt.AlignBottom)
        self.mess_layout.addWidget(lab)

    def connect_btn_clicked(self,check):...

    
    def send_btn_clicked(self):...
    


if __name__  == "__main__":
    app = QApplication([])

    window = MainWindow()
    window.show()
    app.exec_()