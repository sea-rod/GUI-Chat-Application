from .ui_interface import Ui_MainWindow
from PySide2.QtWidgets import QMainWindow
from PySide2.QtCore import QPropertyAnimation,Qt

class intergui(QMainWindow,Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.create_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.create_frame))
        self.join_btn.clicked.connect(lambda:self.stackedWidget.setCurrentWidget(self.join_frame))
        self.menu_btn.clicked.connect(self.menu_btn_clicked)
        
        self.send_btn.clicked.connect(self.send_btn_clicked)
        self.connect_btn.clicked.connect(self.connect_btn_clicked)
        self.start_btn.clicked.connect(self.start_btn_clicked)
        self.hst_prt.textChanged.connect(lambda:self.hst_prt.setStyleSheet("color:#f4f0f0;"))

   

    def menu_btn_clicked(self,chk):
        if chk:
            self.animation = QPropertyAnimation(self.side_main,b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(100)
            self.animation.setEndValue(200)
            self.animation.start()
            self.menu_btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            self.create_btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            self.join_btn.setToolButtonStyle(Qt.ToolButtonTextBesideIcon)
            
            
        else:
            self.animation = QPropertyAnimation(self.side_main,b"minimumWidth")
            self.animation.setDuration(500)
            self.animation.setStartValue(200)
            self.animation.setEndValue(100)
            self.animation.start()

            self.menu_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
            self.create_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)
            self.join_btn.setToolButtonStyle(Qt.ToolButtonIconOnly)

    def send_btn_clicked(self):...
    def connect_btn_clicked(self,chk):...
    def start_btn_clicked(self):...
    
    